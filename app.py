import os
from tkinter.filedialog import askdirectory

caminho = askdirectory()

arquivos = os.listdir(caminho)


locais = {'Documentos De Texto': '.txt',
          'Arquivo Power Point': '.pptx',
          'Planilhas Excel': '.xlsx',
          'Aplicativos': '.url',
          'PDFs': '.pdf',
          'Imagens': ['.png','.jpg']}

contador = len(arquivos)

while len(arquivos) > 0:
    for arquivo in arquivos:
        nome, formato = os.path.splitext(arquivo)
        for pasta in locais:
            if formato in locais[pasta]:
                try:
                    os.mkdir(f'{caminho}/{pasta}')
                except FileExistsError:
                    os.rename(f'{caminho}/{arquivo}', f'{caminho}/{pasta}/{arquivo}')
                    arquivos.remove(arquivo)
                else:
                    os.rename(f'{caminho}/{arquivo}', f'{caminho}/{pasta}/{arquivo}')
                    arquivos.remove(arquivo)
