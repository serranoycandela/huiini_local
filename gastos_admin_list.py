from os.path import join
import json
appDataDirectory = "C:/Users/serra/GitHub/huiini_local/huiini_aux_files"
with open(join(appDataDirectory,"conceptos.json"), "r") as jsonfile:
    concepto = json.load(jsonfile)

for i in range(84110000,84120000): 
    if i != 84111505:
        if str(i) in concepto:
            print('"'+str(i)+'",')
        