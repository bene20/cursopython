import os
from PyP

PDF_ORIGINAL_PATH = os.path.dirname(__file__) + '/pdfs_originais'
PDF_NOVO_PATH = os.path.dirname(__file__) + '/pdfs_novos'


RELATORIO_BACEN = PDF_ORIGINAL_PATH + '/R20240531.pdf'

if not os.path.exists(RELATORIO_BACEN):
    raise FileNotFoundError(f'Arquivo PDF {RELATORIO_BACEN} não encontrado!')

reader = PdfReader(RELATORIO_BACEN)

print(f'O relatório {os.path.basename(RELATORIO_BACEN)} tem {len(reader.pages)} páginas')
# print("Conteúdo da página 1:", reader.pages[0].extract_text(), sep='\n')

# Extraindo imagens da primeira página
page0 = reader.
images = page0.imag

for img in images:
    print(f'Extraindo imagem {img.name}')
    # with open(PDF_NOVO_PATH + '/' + imagem.name, 'wb') as fp:
        # fp.write(imagem.data)

