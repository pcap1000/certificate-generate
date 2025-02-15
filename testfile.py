from fpdf import FPDF

def generate_certificate(student_name, completion_date, course_name, instructor_name, logo_path):
    pdf = FPDF(orientation='L', unit='pt', format='A4')
    pdf.add_page()
    
    # Add custom font
    pdf.add_font("Gunaydin", style="", fname=r"C:\Users\prane\Downloads\certificate_generator_one\certificate_generator\fonts\Gunaydin-Regular.ttf", uni=True)
    pdf.add_font("TimesNewRomanBold", style="", fname=r"C:\Users\prane\Downloads\certificate_generator_one\certificate_generator\fonts\times-new-roman-bold.otf", uni=True)
    pdf.add_font("TThoves", style="", fname=r"C:\Users\prane\Downloads\certificate_generator_one\certificate_generator\fonts\TT_Hoves_Pro_Bold.ttf", uni=True)
    pdf.add_font("Touche", style="", fname=r"C:\Users\prane\Downloads\certificate_generator_one\certificate_generator\fonts\Touche-Semibold-BF642a2ebf682d9.otf", uni=True)
    pdf.add_font("Altone", style="", fname=r"C:\Users\prane\Downloads\certificate_generator_one\certificate_generator\fonts\Altone Trial-Regular.ttf", uni=True)

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
    pdf.cell(w=page_width-100, h=40, txt=course_name, align="L")

    # Instructor Info
    pdf.set_font("Gunaydin", size=16)
    pdf.set_xy(50, 240)
    pdf.cell(w=page_width-100, h=20, txt=f"Instructor: {instructor_name}", align="L")

    # Student details
    pdf.set_font("Touche", style="", size=40)
    pdf.set_xy(50, 350)
    pdf.cell(w=page_width-100, h=40, txt=student_name, align="L")

    pdf.set_font("TimesNewRomanBold", style="", size=17)
    pdf.set_xy(50, 390)
    pdf.cell(txt=f"Date {completion_date}", ln=1)

    pdf.set_font("TimesNewRomanBold", style="", size=17)
    pdf.set_xy(50, 410)
    pdf.cell(txt="Length 10 total hours", ln=1)

    # Save PDF
    output_filename = "Udemy-certificate.pdf"
    pdf.output(output_filename)
    print(f"Certificate saved as '{output_filename}'.")

if __name__ == "__main__":
    student_name_input = "David D Raja"
    completion_date_input = "Dec. 31, 2005"
    course_name_input = "Python"
    instructor_name_input = "Steven pual Jobs"
    logo_path = r"C:\Users\prane\Downloads\certificate_generator_one\certificate_generator\static\udemylogo-removebg-preview.png"

    generate_certificate(student_name_input, completion_date_input, course_name_input, instructor_name_input, logo_path)
