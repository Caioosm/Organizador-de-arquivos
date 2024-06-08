import os
from tkinter.filedialog import askdirectory

diretorio = askdirectory(title="Selecione uma pasta")

lista_arquivos = os.listdir(diretorio)

#pastas e extensões dos arquivos especifícos para cada pasta
locais = {
    "Imagens": [".png", ".jpg", ".jpeg", ".svg", ".webp", '.jfif', '.mp4', '.MPEG'],
    "pdfs": [".pdf"],
    "Slides": [".pptx", ".odp", ".potx"],
    "Winrar": [".zip", ".rar"],
    "word": [".docx", ".doc", ".txt"],
    "executaveis": [".exe", ".msi"],
    "Torrents": [".torrent"],
    "Planilhas": [".xlsx", ".xls", ".csv"],
    "Programacao": [".html", ".css", '.md', '.py', '.ipynb', '.asta'],
    "Aleatorios": [".jar"],
    "Audios": [".mp3", ".WEBM"]
}

for arquivo in lista_arquivos:
    #01. arquivo.pdf
    nome, extensao = os.path.splitext(f"{diretorio}/{arquivo}")

    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{diretorio}/{pasta}"):
                os.mkdir(f"{diretorio}/{pasta}")
            os.rename(f"{diretorio}/{arquivo}", f"{diretorio}/{pasta}/{arquivo}")