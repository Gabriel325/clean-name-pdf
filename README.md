# Clean Name PDF

O projeto surgiu de um problema onde recebi um conjunto de pdfs que chegaram do meu trabalho e precisava limpa-los para adequa-las no servidor para utiliza-los na url. Usei Python pela versatilidade e porque sou mais familarizado com a linguagem.

## clean_name_list_pdf.py

Neste script contém 2 propósitos:
- listar os arquivos pdfs no repositório onde está localizado;
	- utilizei o módulo [glob.glob()](https://docs.python.org/3/library/os.html#os.rename) para listar.
- e renomear os pdfs listados na váriavel lista_pdf.
	- utilizei a função [os.rename()](https://docs.python.org/3/library/os.html#os.rename) para renomear.

```python
import  glob
import  os
from dependence import  clean_name_pdf  as  clean

def  listar_pdf_no_diretorio():
	pdfs_do_diretorio = glob.glob(f"*pdf")
	return  pdfs_do_diretorio
	
lista_pdf = listar_pdf_no_diretorio()

for  pdf  in  lista_pdf:
	os.rename(pdf, clean.clean_name_pdf(pdf))
```
A função clean.clean_name_pdf() é irei fazer a limpeza do nome dos arquivos

## clean_name_pdf.py

No clean_name_pdf é por onde faz as 4 etapas da limpeza:
1- Mudar as letras com acentos e pontuação para formatos sem acento e somente hifen;
2- Manter a extensão ".pdf" pois o código faz a remoção de pontuação;
3- Limpeza entre o nome e o ".pdf", para que não haja hifen/espaçamento;
4- e deletar espaços duplicados, no caso 2 hifens.

No código, cada tarefa citada anteriormente tornou-se uma função, onde a entrada da váriavel nome é do tipo string que é convertida para um list pois será necessário trabalhar com a posição dos caracteres do nome do arquivo. 

```python
from . import  change_caracter_in_name  as  change , del_duplicate_space  as  delete
from . import  keep_extension_pdf  as  keep, clean_final_caracter_in_name  as  clean_final

def  clean_name_pdf(nome):
	lista = list(nome)
	
	change.change_caracter_in_name(lista)
	keep.keep_extension_pdf(lista)
	clean_final.clean_final_caracter_in_name(lista)
	delete.del_duplicate_space(lista)

	return  ''.join(lista)
```
