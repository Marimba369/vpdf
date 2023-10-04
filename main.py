# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import PyPDF2
import sys


#get the file name from terminal
path = sys.argv[1]

# Abrir o arquivo PDF em modo de leitura binária
# open the file PDF in read mode
with open(path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Ler o texto de cada página
    #read the text line by line
    text = ""
    for page in pdf_reader.pages:
         text += page.extract_text()


# Imprimir o texto extraído
# print in terminal the file extract
print(text)