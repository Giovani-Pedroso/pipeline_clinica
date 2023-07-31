from numpy import random
import pandas as pd
import seaborn as sns

# d1 = "1/1/2022"
# d2 = "30/6/2023"

# print(test.random_date(d1, d2, random.random()))
# test.create_mock(10)
# print("Hello from read excel")

class AnaliseClinica():
    def __init__(self, planilha):
        self.atendimentos_5_meses= {'Janeiro': 20, 'Fevereiro':10, 'Março':15, 'Abril':22, 'Maio':17}
