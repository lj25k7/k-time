'''
Program to extract files 2-levels-deep
and move them on a directory on the desktop
'''

#       IMPORT MODULES

import shutil
import os

#       ASK FOR INPUTS and DEFINITION OF MAIN VARIABLES

cartella = input("\n\nNome della cartella in Download dalla quale devo copiare i file:\n\n> ")
source = os.listdir(f"C:/Users/Louis/Downloads/{cartella}")
                        # CREO UNA LISTA DEGLI ELEMENTI PRESENTI NEL PATH

des = input("\nNome della cartella di destinazione sul Desktop:\n\n> ")
destination = f"C:/Users/Louis/Desktop/{des}"
                        # SETTO LA CATELLA DI DESTINAZIONE

#       ELABORATE IMPUTS

for files in source:
                        # PER OGNI SINGOLO ELEMENTO PRESENTE NELLA LISTA DI PRIMA
    if files.startswith("customer"):
                        # SE LA CARTELLA COMINCIA CON "customer"
        source_2 = os.listdir(f"C:/Users/Louis/Downloads/{cartella}/{files}")
                        # CREA UNA LISTA DEGLI ELEMENTI PRESENTI DDENTRO QUELLA CARTELLA
        for files_2 in source_2:
                        # E PER OGNI ELEMENTO DI QUESTA NUOVA LISTA
            if files_2.startswith("customer_"):
                        # SE QUEST'ULTIMO COMINCIA CON "customer_"
                print (f"copying files... {files_2}")
                        # SCRIVI IL LOG
                shutil.copy(f"C:/Users/Louis/Downloads/{cartella}/{files}/{files_2}", destination)
                        # E COPIA IL FILE NELLA CARTELLA DI DESTINAZIONE
