def exists_word(word, instance):
    results = []
    for file in instance.queue:
        occurrences = []
        for i, row in enumerate(file["linhas_do_arquivo"]):
            if word in row.lower():
                occurrences.append({
                    "linha": i + 1
                    })

        if len(occurrences) > 0:
            results.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrences
            })
    return results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
