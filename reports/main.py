from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth 
import datetime

PAGE_WIDTH = A4[0]
PAGE_HEIGHT = A4[1]
font_default = 'Helvetica'
font_body = 'Helvetica'

#Create the main page
class Relatorio(canvas.Canvas):
    def __init__(self, path):
        super().__init__(path,pagesize=A4 )

        self.cover()


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
        self.line(PAGE_WIDTH*0.10, 250*mm, PAGE_WIDTH*0.90, 250*mm)
        # self.line(20, 240*mm, 10, 240*mm)
        
        #nome relatorio
        self.setFillColorRGB(0,0,0)
        self.setFont(font_body, 32)
        nome = f"Relatorio do mes {datetime.datetime.now().month}/{datetime.datetime.now().year}"
        size_nome = stringWidth(nome, fontName=font_body, fontSize=32)
        position_nome= PAGE_WIDTH/2 - size_nome/2
        self.drawString(position_nome , PAGE_HEIGHT/2, nome)

        #Footer
        self.setFillColorRGB(0.6,0.6,0.6)
        self.setFont(font_default, 16)
        footer = f"Itapevi, São Paulo {datetime.datetime.now().year}"
        size_footer = stringWidth(footer, fontName=font_default, fontSize=16)
        position_footer= PAGE_WIDTH/2 - size_footer/2
        self.drawString(position_footer , 16*mm, footer)

    def generatePDF(self):
        self.save()

relatorio = Relatorio('./reports/testClass.pdf')
relatorio.generatePDF()

