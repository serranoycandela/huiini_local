# cargar_una.py
import os
from cargador_facturas import procesar_xml, cargar_categorias_desde_json

if __name__ == "__main__":
    # Opcional: cargar categorías si tienes el JSON
    if os.path.exists("default_cats.json"):
        cargar_categorias_desde_json("default_cats.json")
    # Procesar el XML
    procesar_xml("G:\Shared drives\SICAD 2025\Archivo 2025\ARACELI CARRANCO\CONTABILIDAD\2025\02 FEBRERO\EGRESOS\01B2F5BA-DB2A-4E06-8C34-2DDB3D7D17A3@1100000000XX0.xml")