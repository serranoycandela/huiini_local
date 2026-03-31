import os
import sys
from pathlib import Path

# Agrega el directorio actual al path si es necesario
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import SessionLocal
from models import Categoria
from cargador_facturas import procesar_xml, cargar_categorias_desde_json

def main():
    # 1. Verificar que el XML existe
    xml_path = "G:\Shared drives\SICAD 2025\Archivo 2025\ARACELI CARRANCO\CONTABILIDAD\2025\02 FEBRERO\EGRESOS\01B2F5BA-DB2A-4E06-8C34-2DDB3D7D17A3@1100000000XX0.xml"  # Cambia por la ruta real
    if not os.path.exists(xml_path):
        print(f"El archivo {xml_path} no existe.")
        return

    # 2. Cargar categorías desde default_cats.json (si existe)
    cats_path = "default_cats.json"
    if os.path.exists(cats_path):
        cargar_categorias_desde_json(cats_path)
        print("Categorías cargadas.")
    else:
        print("No se encontró default_cats.json, se usarán solo categorías existentes.")

    # 3. Procesar el XML
    try:
        procesar_xml(xml_path)
        print("Factura procesada e insertada correctamente.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()