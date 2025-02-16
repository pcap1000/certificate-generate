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

# Register custom fonts for Coursera certificates
pdfmetrics.registerFont(TTFont('RivalRegular', r'fonts/rival-regular-1.otf'))
pdfmetrics.registerFont(TTFont('DateFont', r'fonts/URW Grotesk Wide Light Oblique.ttf'))

def generate_certificate(name, date, course, selected_company, course_provider="Coursera", instructor_name=None, logo_path=None):
    if course_provider == "Coursera":
        # Generate Coursera certificate
        width, height = A4  # Original portrait dimensions
        c = canvas.Canvas(f"Certificate_{name.replace(' ', '_')}.pdf", pagesize=(height, width))  # Landscape

        # Draw border image
        try:
            border_path = r"static/Border.png"
            border_img = ImageReader(border_path)
            c.drawImage(border_img, 0, 0, width=height, height=width)
        except Exception as e:
            print(f"Could not load border image: {e}")
            # Fallback to original border design if image fails
            c.setStrokeColor(colors.HexColor("#1F618D"))
            c.setLineWidth(3)
            c.rect(30, 30, height-60, width-60)
            c.setDash(6, 4)
            c.rect(40, 40, height-80, width-80)
            c.setDash()

        # Logo handling based on selected_company
        if selected_company == "IBM":
            c.setFont("RivalRegular", 10)
            x = height/2 - 350
            y = (width - 480) + 130
            first_line = "an online non-credit course authorized by IBM and offered "
            c.drawString(x, y, first_line)
            second_line = "through Coursera."
            c.drawString(x, y - 12, second_line)
            try:
                logo_path_left = r"static/purepng.com-ibm-logologobrand-logoiconslogos-251519939176ka7y8.png"
                img_left = ImageReader(logo_path_left)
                l_width = 2.0*inch
                aspect_left = img_left.getSize()[1] / img_left.getSize()[0]
                l_height = l_width * aspect_left
                c.drawImage(logo_path_left, 60, width - 60 - l_height, width=l_width, height=l_height, mask='auto')
            except Exception as e:
                print(f"Could not load left logo: {e}")

        elif selected_company == "Johns Hopkins":
            c.setFont("RivalRegular", 10)
            x = height/2 - 350
            y = (width - 480) + 130
            first_line = "an online non-credit course authorized by Johns Hopkins and"
            c.drawString(x, y, first_line)
            second_line = "offered through Coursera."
            c.drawString(x, y - 12, second_line)
            try:
                logo_path_left = r"static/Johns_Hopkins_University_Logo-1536x258.png"
                img_left = ImageReader(logo_path_left)
                l_width = 3.5*inch
                aspect_left = img_left.getSize()[1] / img_left.getSize()[0]
                l_height = l_width * aspect_left
                c.drawImage(logo_path_left, 60, width - 70 - l_height, width=l_width, height=l_height, mask='auto')
            except Exception as e:
                print(f"Could not load left logo: {e}")

        elif selected_company == "Duke University":
            c.setFont("RivalRegular", 10)
            x = height/2 - 350
            y = (width - 480) + 130
            first_line = "an online non-credit course authorized by Duke University and"
            c.drawString(x, y, first_line)
            second_line = "offered through Coursera."
            c.drawString(x, y - 12, second_line)
            try:
                logo_path_left = r"static/duke_university.jpg"
                img_left = ImageReader(logo_path_left)
                l_width = 2.0*inch
                aspect_left = img_left.getSize()[1] / img_left.getSize()[0]
                l_height = l_width * aspect_left
                c.drawImage(logo_path_left, 60, width - 60 - l_height, width=l_width, height=l_height, mask='auto')
            except Exception as e:
                print(f"Could not load left logo: {e}")

        elif selected_company == "Wharton University":
            c.setFont("RivalRegular", 10)
            x = height/2 - 350
            y = (width - 480) + 130
            first_line = "an online non-credit course authorized by Wharton University and"
            c.drawString(x, y, first_line)
            second_line = "offered through Coursera."
            c.drawString(x, y - 12, second_line)
            try:
                logo_path_left = r"static/Wharton_Logo_Small.png"
                img_left = ImageReader(logo_path_left)
                l_width = 3.5*inch
                aspect_left = img_left.getSize()[1] / img_left.getSize()[0]
                l_height = l_width * aspect_left
                c.drawImage(logo_path_left, 60, width - 60 - l_height, width=l_width, height=l_height, mask='auto')
            except Exception as e:
                print(f"Could not load left logo: {e}")

        elif selected_company == "Yonsei University":
            c.setFont("RivalRegular", 10)
            x = height/2 - 350
            y = (width - 480) + 130
            first_line = "an online non-credit course authorized by Yonsei University and"
            c.drawString(x, y, first_line)
            second_line = "offered through Coursera."
            c.drawString(x, y - 12, second_line)
            try:
                logo_path_left = r"static/yonsei.png"
                img_left = ImageReader(logo_path_left)
                l_width = 3.5*inch
                aspect_left = img_left.getSize()[1] / img_left.getSize()[0]
                l_height = l_width * aspect_left
                c.drawImage(logo_path_left, 60, width - 60 - l_height, width=l_width, height=l_height, mask='auto')
            except Exception as e:
                print(f"Could not load left logo: {e}")

        elif selected_company == "Edinburgh University":
            c.setFont("RivalRegular", 10)
            x = height/2 - 350
            y = (width - 480) + 130
            first_line = "an online non-credit course authorized by Edinburgh University and"
            c.drawString(x, y, first_line)
            second_line = "offered through Coursera."
            c.drawString(x, y - 12, second_line)
            try:
                logo_path_left = r"static/eidenburgh.png"
                img_left = ImageReader(logo_path_left)
                l_width = 3.9*inch
                aspect_left = img_left.getSize()[1] / img_left.getSize()[0]
                l_height = l_width * aspect_left
                c.drawImage(logo_path_left, 60, width - 60 - l_height, width=l_width, height=l_height, mask='auto')
            except Exception as e:
                print(f"Could not load left logo: {e}")

        else:
            c.setFont("RivalRegular", 10)
            x = height/2 - 350
            y = (width - 480) + 130
            first_line = "an online non-credit course authorized by Wharton University and"
            c.drawString(x, y, first_line)
            second_line = "offered through Coursera."
            c.drawString(x, y - 12, second_line)
            try:
                logo_path_left = r"static/university_of_london.jpeg"
                img_left = ImageReader(logo_path_left)
                l_width = 1.5*inch
                aspect_left = img_left.getSize()[1] / img_left.getSize()[0]
                l_height = l_width * aspect_left
                c.drawImage(logo_path_left, 60, width - 60 - l_height, width=l_width, height=l_height, mask='auto')
            except Exception as e:
                print(f"Could not load left logo: {e}")

        try:
            logo_path_right = r"static/Coursera-MZYLUZ38AX27-1536x1187.jpg"
            img_right = ImageReader(logo_path_right)
            r_width = 2.5*inch
            aspect_right = img_right.getSize()[1] / img_right.getSize()[0]
            r_height = r_width * aspect_right
            c.drawImage(logo_path_right, height - 75 - r_width, width - 16 - r_height, width=r_width, height=r_height, mask='auto')
        except Exception as e:
            print(f"Could not load right logo: {e}")

        # Signature
        try:
            signature_path = r"static/sign.png"
            img_signature = ImageReader(signature_path)
            sig_width = 2.0 * inch
            aspect_ratio = img_signature.getSize()[1] / img_signature.getSize()[0]
            sig_height = sig_width * aspect_ratio
            x_position = 65
            y_position = 60
            c.drawImage(signature_path, x_position, y_position, width=sig_width, height=sig_height, mask='auto')
        except Exception as e:
            print(f"Could not load signature: {e}")

        # Certificate content
        text_color = colors.HexColor("#2C3E50")
        c.setFillColor(text_color)

        # Completion date
        date_obj = datetime.strptime(date, "%B %d, %Y")
        formatted_date = date_obj.strftime("%m/%d/%Y")
        c.setFont("DateFont", 10)
        c.drawString(height/2-350, (width - 200)-10, formatted_date)

        # Fake URL
        base_url = "https://www.coursera.org"
        params = {
            'ref': ''.join(random.choices(string.ascii_lowercase + string.digits, k=4)),
            'utm_source': ''.join(random.choices(string.ascii_lowercase, k=3)),
            'utm_medium': random.choice(['e', 's', 'o', 'b']),
            'utm_content': ''.join(random.choices(string.ascii_lowercase + string.digits, k=5)),
            'rand': ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        }
        params_list = list(params.items())
        random.shuffle(params_list)
        query = '&'.join([f"{k}={v}" for k, v in params_list])
        shorter_url = f"{base_url}?{query}"

        # Split the URL into three lines
        tokens = shorter_url.split('&')
        total_length = len(shorter_url)
        target_length = total_length / 3.0
        groups = []
        current_group = []
        current_length = 0

        for token in tokens:
            token_str = token if not current_group else '&' + token
            token_length = len(token_str)
            if current_group and (current_length + token_length > target_length) and (len(groups) < 2):
                groups.append(''.join(current_group))
                current_group = [token]
                current_length = len(token)
            else:
                current_group.append(token_str)
                current_length += token_length

        groups.append(''.join(current_group))
        while len(groups) < 3:
            groups.append("")

        # Draw the URL on the canvas
        c.setFont("RivalRegular", 10)
        x = height/2 + 150
        y = (width - 420) - 100
        line_spacing = 12
        c.drawString(x, y, groups[0])
        c.drawString(x, y - line_spacing, groups[1])
        c.drawString(x, y - 2 * line_spacing, groups[2])
        c.drawString(height/2+150, (width -420)-85, "Verify at")

        # Recipient section
        c.setFont("RivalRegular", 10)
        c.drawString(height/2-350, (width - 350)+65, "has successfully completed")
        text_object = c.beginText()
        text_object.setTextOrigin(height/2-350, (width - 280)+30)
        text_object.setFont("RivalRegular", 26)
        text_object.setCharSpace(2.0)
        text_object.textOut(name.title())
        c.drawText(text_object)

        # Course details
        c.setFont("RivalRegular", 18)
        text = f"{course}"
        c.drawString(height/2-350, (width - 420)+100, text)

        # Signature section
        offset = -550
        signature_x = height - 220 + offset
        c.setFont("RivalRegular", 8)
        c.drawString(signature_x, 50, "Authorized Signature")

        c.save()
        print(f"Certificate for {name} generated successfully!")

    elif course_provider == "Udemy":
        # Generate Udemy certificate
        pdf = FPDF(orientation='L', unit='pt', format='A4')
        pdf.add_page()

        # Add custom fonts
        # pdfmetrics.registerFont(TTFont('Gunaydin', r'fonts/Gunaydin-Regular.ttf'))
        # pdfmetrics.registerFont(TTFont('TimesNewRomanBold', r'fonts/times-new-roman-bold.otf'))
        # pdfmetrics.registerFont(TTFont('Touche', r'fonts/Touche-Semibold-BF642a2ebf682d9.ttf'))
        #pdf.add_font("Gunaydin", style="", fname=r"fonts/rival-regular-1.otf", uni=True)
        #pdf.add_font("TimesNewRomanBold", style="", fname=r"fonts/rival-regular-1.otf", uni=True)
        #pdf.add_font("Touche", style="", fname=r"fonts/rival-regular-1.otf", uni=True)
        pdf.add_font("Gunaydin", style="", fname=r"fonts/Gunaydin-Regular.ttf", uni=True)
        pdf.add_font("TimesNewRomanBold", style="", fname=r"fonts/times-new-roman-bold.otf", uni=True)  # Ensure it's .ttf
        pdf.add_font("Touche", style="", fname=r"fonts/Touche-Semibold-BF642a2ebf682d9.ttf", uni=True)


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

        output_filename = f"Udemy-certificate_{name.replace(' ', '_')}.pdf"
        pdf.output(output_filename)
        print(f"Certificate saved as '{output_filename}'.")

    else:
        print("Unsupported course provider.")
