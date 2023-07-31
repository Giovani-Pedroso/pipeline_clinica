import os
from dotenv import load_dotenv 
from reportlab.pdfgen import canvas 
from reportlab.lib.pagesizes import A4
# load_dotenv()
# REPORTS_PATH = os.getenv('REPORTS_PATH')

#convernt mm to points
def mm2p(mm):
    return mm / 0.352777

print("testing the pdf generation")

cnv = canvas.Canvas(f"./meu_pdf_test.pdf", pagesize=A4)
cnv.drawString(0, 0, "text")


cnv.save()
