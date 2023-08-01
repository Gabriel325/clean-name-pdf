from . import change_caracter_in_name as change , del_duplicate_space as delete
from . import keep_extension_pdf as keep, clean_final_caracter_in_name as clean_final

def clean_name_pdf(nome):
    lista = list(nome)

    change.change_caracter_in_name(lista)
    keep.keep_extension_pdf(lista)
    clean_final.clean_final_caracter_in_name(lista)
    delete.del_duplicate_space(lista)

    return ''.join(lista)