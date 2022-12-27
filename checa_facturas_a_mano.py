
import os
import FacturasLocal as F
path = "C:\\Dropbox\\SICAD 2022\\SISA HERMES CONSTRUCCION\\Contabilidad\\2022\\11 NOVIEMBRE\\EGRESOS"

# for file in os.listdir(path):
#     if file.endswith("xml"):
#         print(file)
#         esta_fac = F.FacturaLocal(os.path.join(path,file))
#         if esta_fac.tipoDeComprobante == "P":

#             print(esta_fac.IdDocumento)

file = "5d0bfce6-6615-4965-b4e9-cb84c80a44e5.xml"
esta_fac = F.FacturaLocal(os.path.join(path,file))
print(esta_fac.UUID)
