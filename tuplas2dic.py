import glob
import json
for x in glob.glob('C:/Dropbox (LANCIS)/**/categorias_huiini.json', recursive=True):
    print(x)
    with open(x, "r", encoding="utf-8") as jsonfile:
        lista_de_tuplas = json.load(jsonfile)

    dicc_de_categorias = {}
    for tupla in lista_de_tuplas:
        if not tupla[1] in dicc_de_categorias:
            dicc_de_categorias[tupla[1]] = []
        dicc_de_categorias[tupla[1]].append(tupla[0])

    dicc_path = x.replace("categorias_huiini", "categorias_dicc_huiini")
    with open(dicc_path, "w", encoding="utf-8") as jsonfile:
        json.dump(dicc_de_categorias, jsonfile)
