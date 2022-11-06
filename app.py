import PyPDF2
import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/rotatePdf',methods = ['POST'])  
def login_page():
    if request.method=='POST':
        PageNumber = request.form['PageNumber']
        RotationDegree = request.form['RotationDegree']
        PdfFile = request.files['file']
        global destination
        target = os.path.join(APP_ROOT, 'static/Input_Pdfs/')
        filename = PdfFile.filename
        destination = "/".join([target, filename])
        PdfFile.save(destination)
        FileLocation = "D:/INTERNSHIP_ASSESMENT/static/Input_Pdfs/"+filename
        pdf_in = open(FileLocation, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_in)
        pdf_writer = PyPDF2.PdfFileWriter()
        for pagenum in range(pdf_reader.numPages):
            page = pdf_reader.getPage(pagenum)
            if pagenum+1 == int(PageNumber):
                page.rotateClockwise(int(RotationDegree))
            pdf_writer.addPage(page)

        FileLocation = "D:/INTERNSHIP_ASSESMENT/static/Output_Pdfs/"+filename
        pdf_out = open(FileLocation, 'wb')
        pdf_writer.write(pdf_out)
        pdf_out.close()
        pdf_in.close()
        print(PageNumber+" "+RotationDegree)
        return render_template('success.html',filename=filename,PageNumber=PageNumber,RotationDegree=RotationDegree)


if __name__=="main":
    app.run(debug==True)