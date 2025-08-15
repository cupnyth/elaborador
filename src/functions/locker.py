from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

class Locker:
    def __init__(self):
        
        self.exames_path = "exames"



    def create_exam(self, enterprise: str, colaborator: str, exams: list, passw):
        try:
            os.makedirs(fr"{self.exames_path}\{enterprise}", exist_ok=True)
            os.makedirs(fr"temp", exist_ok=True)
            
            # Criar canvas do PDF
            caminho_pdf = fr"{self.exames_path}\{enterprise}\{colaborator}.pdf"
            c = canvas.Canvas(caminho_pdf, pagesize=A4,encrypt=passw)
            
            # Adicionar cada imagem
            for i, imagem in enumerate(exams):
                if os.path.exists(imagem):
                    # Desenhar imagem ajustada à página
                    c.drawImage(imagem, 0, 0, width=A4[0], height=A4[1], preserveAspectRatio=True)
                    
                    # Nova página (exceto na última)
                    if i < len(exams) - 1:
                        c.showPage()
            
            # Salvar PDF
            c.save()
            
            
        except Exception as e:
            return f"Erro: {e}"