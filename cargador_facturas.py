# cargador_facturas.py
import os
import json
import logging
from datetime import datetime
from pathlib import Path

from sqlalchemy.orm import Session
from database import SessionLocal
from models import Factura, Concepto, Impuesto, Categoria
from FacturasLocal import FacturaLocal

# Configurar logging básico (opcional)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def cargar_categorias_desde_json(json_path):
    """
    Carga las categorías desde un archivo JSON en la tabla 'categorias'.
    Espera una estructura como:
    {
        "Alimentos": {"tipo": "gasto", "patrones": ["5021", "5019"]},
        "Combustible": {"tipo": "gasto", "patrones": ["1510", "1511"]},
        ...
    }
    Si ya existe una categoría con el mismo nombre, se actualizan tipo y patrones.
    """
    if not os.path.exists(json_path):
        logging.warning(f"No se encontró el archivo de categorías: {json_path}")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        cats = json.load(f)

    session = SessionLocal()
    try:
        for nombre, datos in cats.items():
            # Buscar si ya existe
            categoria = session.query(Categoria).filter_by(nombre=nombre).first()
            if categoria:
                categoria.tipo = datos.get('tipo', 'gasto')
                categoria.patrones = datos.get('patrones', [])
            else:
                categoria = Categoria(
                    nombre=nombre,
                    tipo=datos.get('tipo', 'gasto'),
                    patrones=datos.get('patrones', [])
                )
                session.add(categoria)
        session.commit()
        logging.info(f"Categorías cargadas desde {json_path}")
    except Exception as e:
        session.rollback()
        logging.error(f"Error al cargar categorías: {e}")
        raise
    finally:
        session.close()


def obtener_categoria_id(clave_prod_serv: str, session: Session) -> int:
    """
    Devuelve el ID de la categoría que coincide con el patrón (prefijo) de clave_prod_serv.
    Si no coincide ninguna, se asigna a la categoría 'Otros' (si existe), de lo contrario None.
    """
    categorias = session.query(Categoria).all()
    for cat in categorias:
        if cat.patrones:
            for patron in cat.patrones:
                if clave_prod_serv.startswith(patron):
                    return cat.id
    # Por defecto, buscar 'Otros'
    otros = session.query(Categoria).filter_by(nombre='Otros').first()
    return otros.id if otros else None


def procesar_xml(xml_path: str):
    """
    Procesa un archivo XML de factura y guarda sus datos en la base de datos.
    """
    # Validar existencia
    if not os.path.exists(xml_path):
        raise FileNotFoundError(f"No se encuentra el archivo: {xml_path}")

    # Parsear con FacturasLocal
    factura_obj = FacturaLocal(xml_path)

    # Verificar que tenga UUID (timbre fiscal)
    if not hasattr(factura_obj, 'UUID') or not factura_obj.UUID:
        raise ValueError("El XML no contiene un UUID (posiblemente no timbrado)")

    # Obtener fecha de timbrado
    fecha_str = getattr(factura_obj, 'fechaTimbrado', None)
    if not fecha_str:
        raise ValueError("No se encontró fechaTimbrado en el XML")
    fecha = datetime.strptime(fecha_str, "%Y-%m-%dT%H:%M:%S").date()

    session = SessionLocal()
    try:
        # Crear registro de factura
        factura = Factura(
            uuid=factura_obj.UUID,
            fecha=fecha,
            folio=getattr(factura_obj, 'folio', None),
            serie=getattr(factura_obj, 'serie', None),
            forma_pago=getattr(factura_obj, 'formaDePago', None),
            metodo_pago=getattr(factura_obj, 'metodoDePago', None),
            lugar_expedicion=getattr(factura_obj, 'LugarExpedicion', None),
            subtotal=getattr(factura_obj, 'subTotal', 0.0),
            descuento=getattr(factura_obj, 'descuento', 0.0),
            total=getattr(factura_obj, 'total', 0.0),
            tipo_comprobante=getattr(factura_obj, 'tipoDeComprobante', None),
            emisor_rfc=getattr(factura_obj, 'EmisorRFC', None),
            emisor_nombre=getattr(factura_obj, 'EmisorNombre', None),
            receptor_rfc=getattr(factura_obj, 'ReceptorRFC', None),
            receptor_nombre=getattr(factura_obj, 'ReceptorNombre', None),
            receptor_uso_cfdi=getattr(factura_obj, 'ReceptorUsoCFDI', None),
            regimen_fiscal_emisor=getattr(factura_obj, 'EmisorRegimen', None),
            no_certificado=getattr(factura_obj, 'noCertificado', None),
            no_certificado_sat=getattr(factura_obj, 'noCertificadoSAT', None),
            sello=getattr(factura_obj, 'sello', None),
            sello_cfd=getattr(factura_obj, 'selloCFD', None),
            sello_sat=getattr(factura_obj, 'selloSAT', None),
            archivo_origen=str(Path(xml_path).absolute()),
            mes=fecha.month,
            anio=fecha.year
        )
        session.add(factura)
        session.flush()  # Para obtener factura.id

        # Insertar conceptos
        for concepto in factura_obj.conceptos:
            # Obtener categoría
            categoria_id = obtener_categoria_id(concepto.get('clave_concepto', ''), session)

            # Convertir valores a float si es necesario
            cantidad = concepto.get('cantidad')
            if cantidad is not None:
                cantidad = float(cantidad)
            valor_unitario = concepto.get('valorUnitario')
            if valor_unitario is not None:
                valor_unitario = float(valor_unitario)

            c = Concepto(
                factura_id=factura.id,
                clave_prod_serv=concepto.get('clave_concepto', ''),
                descripcion=concepto.get('descripcion', ''),
                cantidad=cantidad,
                unidad=concepto.get('unidad', ''),
                valor_unitario=valor_unitario,
                importe=float(concepto.get('importeConcepto', 0)),
                descuento=float(concepto.get('descuento', 0)),
                categoria_id=categoria_id
            )
            session.add(c)

        # Insertar impuestos (traslados y retenciones)
        # Traslados (del impuestosTag)
        for imp, datos in factura_obj.traslados.items():
            if datos.get('importe', 0) != 0:
                tasa = datos.get('tasa')
                if tasa is not None:
                    try:
                        tasa = float(tasa)
                    except:
                        tasa = None
                impuesto = Impuesto(
                    factura_id=factura.id,
                    tipo=imp,
                    ambito='traslado',
                    tasa=tasa,
                    importe=float(datos['importe'])
                )
                session.add(impuesto)

        # Retenciones
        for imp, importe in factura_obj.retenciones.items():
            if importe != 0:
                impuesto = Impuesto(
                    factura_id=factura.id,
                    tipo=imp,
                    ambito='retencion',
                    tasa=None,
                    importe=float(importe)
                )
                session.add(impuesto)

        # Traslados locales
        if hasattr(factura_obj, 'trasladosLocales'):
            for imp, datos in factura_obj.trasladosLocales.items():
                if datos.get('importe', 0) != 0:
                    tasa = datos.get('tasa')
                    if tasa is not None:
                        try:
                            tasa = float(tasa)
                        except:
                            tasa = None
                    impuesto = Impuesto(
                        factura_id=factura.id,
                        tipo=imp,
                        ambito='traslado_local',
                        tasa=tasa,
                        importe=float(datos['importe'])
                    )
                    session.add(impuesto)

        # Retenciones locales
        if hasattr(factura_obj, 'retencionesLocales'):
            for imp, datos in factura_obj.retencionesLocales.items():
                if datos.get('importe', 0) != 0:
                    tasa = datos.get('tasa')
                    if tasa is not None:
                        try:
                            tasa = float(tasa)
                        except:
                            tasa = None
                    impuesto = Impuesto(
                        factura_id=factura.id,
                        tipo=imp,
                        ambito='retencion_local',
                        tasa=tasa,
                        importe=float(datos['importe'])
                    )
                    session.add(impuesto)

        session.commit()
        logging.info(f"Factura {factura.uuid} insertada correctamente.")
        return True

    except Exception as e:
        session.rollback()
        logging.error(f"Error procesando {xml_path}: {e}")
        raise
    finally:
        session.close()