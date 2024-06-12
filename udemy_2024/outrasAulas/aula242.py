from contextlib import contextmanager

@contextmanager
def meuOpen(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf-8')
        yield arquivo
    except Exception as e:
        print('Erro: ', e)
    finally:
        print('Fechando arquivo')
        arquivo.close()

with meuOpen('meuarq.txt', 'w') as arq:
    arq.write('Adicionei conteúdo')
    print('No with')    