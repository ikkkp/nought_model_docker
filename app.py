from flask import Flask

from controller.pdf2textController import Ocean_PDF2Text
from controller.pdfqaController import PDF_QA_Controller

app = Flask(__name__)
app.register_blueprint(Ocean_PDF2Text)
app.register_blueprint(PDF_QA_Controller)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
