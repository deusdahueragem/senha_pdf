from PyPDF2 import PdfFileWriter, PdfFileReader
from PySimpleGUI import PySimpleGUI as sg
import os

sg.theme('Reddit')

layout = [
    [sg.Text('Arquivo PDF'), sg.Input(key='pdf_path'), sg.FileBrowse('Buscar', button_color='green')],
    [sg.Text('Senha'), sg.Input(key='pdf_pass'), sg.Button('Proteger PDF', button_color='green')]
]

janela = sg.Window('Proteger PDF', layout, icon='C:/Users/eduardo/Documents/Criptografar PDF/lock_icon.ico')

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if valores['pdf_path'] != "" and valores['pdf_pass'] != "":
        outputfile = PdfFileWriter()

        #file_path = valores['pdf_path']
        

        with open(valores['pdf_path'], "rb") as file:
            pdffile = PdfFileReader(file)
            numOfPages = pdffile.numPages

            for i in range(numOfPages):
                page = pdffile.getPage(i)

                outputfile.addPage(page)

            password = valores['pdf_pass']

            outputfile.encrypt(password)

            file_name = os.path.basename(valores['pdf_path'])
            new_namefile = ("/protegido_"+file_name)
            new_namefile2 = (os.path.dirname(valores['pdf_path'])+new_namefile)
            with open(new_namefile2, "wb") as f:
                outputfile.write(f)
            sg.popup('PDF foi salvo na mesma pasta do anterior', title='PDF Protegido', button_color='green')
    else:
        sg.popup('Você precisa preencher todos os campos para continuar', title='Preencha todos os campos', button_color='red')