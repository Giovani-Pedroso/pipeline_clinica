import os
from reports.main import Relatorio
from clinica.analise import AnaliseClinica
from concorrentes.analise import AnaliseConcorrentes
from dotenv import load_dotenv 
load_dotenv()

DB_PATH = os.getenv('DB_PATH')
PLANINHA_PATH = os.getenv('PLANINHA_CLIENTES')
PATH_REPORT = os.getenv('PATH_REPORT')

analise_clinica = AnaliseClinica(PLANINHA_PATH)
analise_concorrentes = AnaliseConcorrentes(DB_PATH)

relatorio = Relatorio(f"{PATH_REPORT}/test.pdf", 
                        analise_clinica,
                        analise_concorrentes)

relatorio.generatePDF()