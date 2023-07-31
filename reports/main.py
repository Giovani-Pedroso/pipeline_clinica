from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth 
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

PAGE_WIDTH = A4[0]
PAGE_HEIGHT = A4[1]
font_default = 'Helvetica'
font_body = 'Helvetica'
color_title = (46/255,117/255,181/255)
padding_page = PAGE_WIDTH*0.10
title_style = {'color':[46/255,117/255,181/255],
                'size': 30,
                'font':'Helvetica'}

#Create the main page
class Relatorio(canvas.Canvas):
    def __init__(self, path, analise_clinica, analise_concorrentes):
        super().__init__(path,pagesize=A4 )

        self.atendimentos_5m = analise_clinica.atendimentos_5_meses 
        self.cover()
        self.clientes_ultimos_meses()

    def clientes_ultimos_meses(self):
        self.setFillColorRGB(*title_style['color'])
        self.setFont(title_style['font'], title_style['size'])
        self.drawString(PAGE_WIDTH*0.10 , 260*mm, "Número de atendimentos")

        #Cria o grafico
        plot = sns.barplot(x=list(self.atendimentos_5m.keys()),
                           y=list(self.atendimentos_5m.values()),
                            color='steelblue',
                          )
        plt.title('Conparativo de atendimentos nos ultimos 5 meses', fontsize=16)
        plt.ylabel('Atendimentos')
        fig = plot.get_figure()
        #save the plot in a temporary folder
        path_img ="./reports/tmp_imgs/clientes_por_mes.png"
        fig.savefig(path_img) 

        self.drawImage(path_img, 0,0)
        self.showPage()

    def cover(self):
        #Header
        self.setFont(font_default, 40)
        self.setFillColorRGB(46/255,117/255,181/255)
        title = "Clinica EficazMente"
        size_title = stringWidth(title, fontName=font_default, fontSize=40)
        position_title= PAGE_WIDTH/2 - size_title/2
        self.drawString(position_title , 260*mm, title)
        self.setStrokeColorRGB(0.8,0.8,0.8)
        self.setLineWidth(1)
        self.line(padding_page, 250*mm, PAGE_WIDTH*0.90, 250*mm)
        # self.line(20, 240*mm, 10, 240*mm)
        
        #nome relatorio
        self.setFillColorRGB(0,0,0)
        self.setFont(font_body, 32)
        nome = f"Relatório do mês {datetime.datetime.now().month}/{datetime.datetime.now().year}"
        size_nome = stringWidth(nome, fontName=font_body, fontSize=32)
        position_nome= PAGE_WIDTH/2 - size_nome/2
        self.drawString(position_nome , PAGE_HEIGHT/2, nome)

        #Footer
        self.setFillColorRGB(0.6,0.6,0.6)
        self.setFont(font_default, 16)
        footer = f"Itapevi, São Paulo {datetime.datetime.now().year}"
        position_footer= self.getPositionCenterText(footer, font_default, 16 )
        self.drawString(position_footer , 16*mm, footer)

        #Go to the next page
        self.showPage()
    def getPositionCenterText(self, text, fontName, fontSize):
        size = stringWidth(text, fontName=fontName, fontSize=fontSize)
        position= PAGE_WIDTH/2 - size/2
        return position

    def generatePDF(self):
        self.save()
