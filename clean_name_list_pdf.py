import glob
import os
from dependence import clean_name_pdf as clean


def listar_pdf_no_diretorio():
   
    diretorio = os.getcwd()
    pdfs_do_diretorio = glob.glob(f"*pdf")

    return pdfs_do_diretorio

lista_pdf = listar_pdf_no_diretorio()


for pdf in lista_pdf:
    os.rename(pdf, clean.clean_name_pdf(pdf))