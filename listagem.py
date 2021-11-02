import os
from datetime import datetime

servdor = input("Local: ")
pasta_servidor = os.listdir(servdor)
compilado = []

for (root, dirs, arquivos) in os.walk(servdor, topdown=True):
    for arquivo in arquivos:
        os.path.splitext(arquivo)
        extensao = os.path.splitext(arquivo)[-1]

        # Ignores Windows files

        if arquivo == "thumbs.db" or arquivo == "Thumbs.db":
            pass

        # Append to list
        else:
            texto = f"{root}${arquivo}${extensao}"
            compilado.append(texto)
            print(f"{arquivo}")

    # Write list to TXT file

    with open('teste.txt', 'w') as f:
        for item in compilado:
            f.write("%s\n" % item)

        # Caso queira ignorar os arquivo .PDF

        # if arquivo.endswith((".pdf", ".PDF")):
        #     pass
        # else:
        #     texto = f"{root}$ {arquivo}"
        #     compilado.append(texto)
        #     hm = datetime.now()
        #     print(f" {arquivo}")
        #
        #     with open('teste.txt', 'w') as f:
        #         for item in compilado:
        #             f.write("%s\n" % item)
