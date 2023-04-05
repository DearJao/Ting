from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for item in range(len(instance)):
        if instance.search(item)["nome_do_arquivo"] == path_file:
            return None

    file = txt_importer(path_file)
    if file:
        file_data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file
        }
    instance.enqueue(file_data)
    print(file_data)


def remove(instance):
    file = instance.dequeue()
    if len(file) <= 0:
        return print("Não há elementos")

    return print(f"Arquivo {file['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        return print(file)
    except IndexError:
        return print("Posição inválida", file=sys.stderr)
