from os.path import join
import json
appDataDirectory = "C:/Users/serra/GitHub/huiini_local/huiini_aux_files"
with open(join(appDataDirectory,"conceptos.json"), "r") as jsonfile:
    concepto = json.load(jsonfile)
n = 0
for i in range(841316,841317):
    for j in range(1,100):
        ij = str(i)+str(j).rjust(2, '0') 
        if ij != "84131602":
            if ij in concepto:
                n += 1
                print('"'+str(ij)+'",')






print(n)      