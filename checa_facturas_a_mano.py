
import os
import FacturasLocal as F
path = "C:\\Dropbox\\SICAD 2022\\INTEGRADORA\\CONTABILIDAD\\2022\\07 JULIO\\INGRESOS"

# for file in os.listdir(path):
#     if file.endswith("xml"):
#         print(file)
#         esta_fac = F.FacturaLocal(os.path.join(path,file))
#         if esta_fac.tipoDeComprobante == "P":

#             print(esta_fac.IdDocumento)

file = "38db9394-efef-4138-918a-756d732512c1.xml"
esta_fac = F.FacturaLocal(os.path.join(path,file))
print(esta_fac.IdDocumento)
