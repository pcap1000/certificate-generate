from flask import Flask, render_template, request, send_file
from maincode import generate_certificate
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        name = data['name']
        date = data['date']
        course = data['course']
        selected_company = data['selected_company']
        course_provider = data['course_provider']
        instructor_name = data.get('instructor_name', None)
        logo_path = data.get('logo_path', None)

        # Generate PDF
        generate_certificate(name, date, course, selected_company, course_provider, instructor_name, logo_path)
        
        # Send back the generated PDF
        if course_provider == "Coursera":
            filename = f"Certificate_{name.replace(' ', '_')}.pdf"
        else:
            filename = f"Udemy-certificate_{name.replace(' ', '_')}.pdf"

        return send_file(
            filename,
            as_attachment=True,
            download_name=filename,
            mimetype='application/pdf'
        )
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run()