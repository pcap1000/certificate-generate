from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import inch
from reportlab.lib import colors
from datetime import datetime
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import random
import string
import math
from fpdf import FPDF

pdfmetrics.registerFont(TTFont('RivalRegular', r'C:\Users\prane\Downloads\certificategenerator\certificate_generator\fonts\rival-regular-1.otf'))
pdfmetrics.registerFont(TTFont('DateFont', r'C:\Users\prane\Downloads\certificategenerator\certificate_generator\fonts\URW Grotesk Wide Light Oblique.ttf'))

def generate_certificate(name, date, course, selected_company, course_provider="Coursera", instructor_name=None, logo_path=None):
    if course_provider == "Coursera":
        # Existing Coursera certificate generation code
        width, height = A4
        c = canvas.Canvas(f"Certificate_{name.replace(' ', '_')}.pdf", pagesize=(height, width))



    elif course_provider == "Udemy":
        # Udemy certificate generation code
        pdf = FPDF(orientation='L', unit='pt', format='A4')
        pdf.add_page()

        # Add custom fonts
        pdf.add_font("Gunaydin", style="", fname=r"C:\Users\prane\Downloads\certificate_generator_one\certificate_generator\fonts\Gunaydin-Regular.ttf", uni=True)
        pdf.add_font("TimesNewRomanBold", style="", fname=r"C:\Users\prane\Downloads\certificate_generator_one\certificate_generator\fonts\times-new-roman-bold.otf", uni=True)
        pdf.add_font("Touche", style="", fname=r"C:\Users\prane\Downloads\certificate_generator_one\certificate_generator\fonts\Touche-Semibold-BF642a2ebf682d9.otf", uni=True)

        page_width = pdf.w
        page_height = pdf.h
        pdf.set_auto_page_break(auto=False)

        # Add Udemy Logo
        pdf.image(logo_path, x=50, y=40, w=150)

        # Certificate metadata (top-right)
        pdf.set_font("Gunaydin", size=10)
        metadata_text = (
            "Certificate no: UC-3360e4f1-830c-4836-8ea3-80c033fe8f74\n"
            "Certificate url: udemy.com/UC-3360e4f1-830c-4836-8ea3-80c033fe8f74\n"
            "Reference Number: 0009"
        )
        margin_right = 50
        text_box_width = 300
        pdf.set_xy(page_width - text_box_width - margin_right, 50)
        pdf.multi_cell(w=text_box_width, h=14, txt=metadata_text, align="R")

        # Certificate title
        pdf.set_font("Gunaydin", style="", size=12)
        pdf.set_xy(50, 160)
        pdf.set_text_color(128, 128, 128)
        pdf.cell(w=0, h=30, txt="CERTIFICATE OF COMPLETION", align="L")

        # Course Name
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("TimesNewRomanBold", style="", size=40)
        pdf.set_xy(50, 190)
        pdf.cell(w=page_width-100, h=40, txt=course, align="L")

        # Instructor Info
        pdf.set_font("Gunaydin", size=16)
        pdf.set_xy(50, 240)
        pdf.cell(w=page_width-100, h=20, txt=f"Instructor: {instructor_name}", align="L")

        # Student details
        pdf.set_font("Touche", style="", size=40)
        pdf.set_xy(50, 350)
        pdf.cell(w=page_width-100, h=40, txt=name, align="L")

        pdf.set_font("TimesNewRomanBold", style="", size=17)
        pdf.set_xy(50, 390)
        pdf.cell(txt=f"Date {date}", ln=1)

        pdf.set_font("TimesNewRomanBold", style="", size=17)
        pdf.set_xy(50, 410)
        pdf.cell(txt="Length 10 total hours", ln=1)

        # Save PDF
        output_filename = f"Udemy-certificate_{name.replace(' ', '_')}.pdf"
        pdf.output(output_filename)
        print(f"Certificate saved as '{output_filename}'.")

    else:
        print("Unsupported course provider.")