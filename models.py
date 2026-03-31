from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey, Index, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import inspect

Base = declarative_base()

class Categoria(Base):
    __tablename__ = 'categorias'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True, nullable=False)
    tipo = Column(String, nullable=False)  # 'ingreso' o 'gasto'
    patrones = Column(JSON)  # lista de strings (patrones de ClaveProdServ)

    conceptos = relationship("Concepto", back_populates="categoria")

class Factura(Base):
    __tablename__ = 'facturas'
    id = Column(Integer, primary_key=True)
    uuid = Column(String, unique=True, nullable=False)
    fecha = Column(Date, nullable=False)
    folio = Column(String)
    serie = Column(String)
    forma_pago = Column(String)
    metodo_pago = Column(String)
    lugar_expedicion = Column(String)
    subtotal = Column(Float)
    descuento = Column(Float, default=0.0)
    total = Column(Float, nullable=False)
    tipo_comprobante = Column(String)
    emisor_rfc = Column(String)
    emisor_nombre = Column(String)
    receptor_rfc = Column(String)
    receptor_nombre = Column(String)
    receptor_uso_cfdi = Column(String)
    regimen_fiscal_emisor = Column(String)
    no_certificado = Column(String)
    no_certificado_sat = Column(String)
    sello = Column(String)
    sello_cfd = Column(String)
    sello_sat = Column(String)
    archivo_origen = Column(String, nullable=False)
    mes = Column(Integer, nullable=False)
    anio = Column(Integer, nullable=False)

    conceptos = relationship("Concepto", back_populates="factura", cascade="all, delete-orphan")
    impuestos = relationship("Impuesto", back_populates="factura", cascade="all, delete-orphan")

    __table_args__ = (
        Index('idx_facturas_fecha', 'fecha'),
        Index('idx_facturas_mes_anio', 'mes', 'anio'),
    )

class Concepto(Base):
    __tablename__ = 'conceptos'
    id = Column(Integer, primary_key=True)
    factura_id = Column(Integer, ForeignKey('facturas.id'), nullable=False)
    clave_prod_serv = Column(String)
    descripcion = Column(String)
    cantidad = Column(Float)
    unidad = Column(String)
    valor_unitario = Column(Float)
    importe = Column(Float)
    descuento = Column(Float, default=0.0)
    categoria_id = Column(Integer, ForeignKey('categorias.id'), nullable=True)

    factura = relationship("Factura", back_populates="conceptos")
    categoria = relationship("Categoria", back_populates="conceptos")

    __table_args__ = (
        Index('idx_conceptos_factura', 'factura_id'),
    )

class Impuesto(Base):
    __tablename__ = 'impuestos'
    id = Column(Integer, primary_key=True)
    factura_id = Column(Integer, ForeignKey('facturas.id'), nullable=False)
    tipo = Column(String, nullable=False)     # 'IVA', 'ISR', etc.
    ambito = Column(String, nullable=False)   # 'traslado', 'retencion', 'traslado_local', 'retencion_local'
    tasa = Column(Float)                      # puede ser None si es tasa 0 o no aplica
    importe = Column(Float, nullable=False)

    factura = relationship("Factura", back_populates="impuestos")

    __table_args__ = (
        Index('idx_impuestos_factura', 'factura_id'),
    )