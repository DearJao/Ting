import os
import sys


def txt_importer(path_file):
    if not os.path.exists(path_file):
        return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)

    _, file_ext = os.path.splitext(path_file)
    if file_ext.lower() != ".txt":
        return print("Formato inválido", file=sys.stderr)

    with open(path_file, "r") as file:
        return file.read().split("\n")
