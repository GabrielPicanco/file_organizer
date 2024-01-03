import os
from tkinter.filedialog import askdirectory

caminho = askdirectory()

os.chdir(caminho)

arquivos_pasta = (os.listdir(caminho))

arquivos_files = []


locais = {'Documentos De Texto': '.txt',
          'Arquivos Power Point': '.pptx',
          'Planilhas Excel': '.xlsx',
          'Imagens': ['.png', '.jpg'],
          'GIFs': '.gif',
          'Documentos Word': '.docx',
          'Aplicativos e jogos': '.url'}

while True:
    for arquivo in arquivos_pasta:
        if os.path.isfile(arquivo):
            arquivos_files.append(arquivo)

    for file in arquivos_files:
        nome, formato = os.path.splitext(file)
        for pasta in locais:
            if formato in locais[pasta]:
                try:
                    os.mkdir(f'{caminho}/{pasta}')
                except FileExistsError:
                    print('')
                    os.rename(f'{caminho}/{file}', f'{caminho}/{pasta}/{file}')
                    arquivos_files.remove(file)
                except FileNotFoundError:
                    print('')
                else:
                    os.rename(f'{caminho}/{file}', f'{caminho}/{pasta}/{file}')
                    arquivos_files.remove(file)
