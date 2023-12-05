
from flask import Flask

from controller.pdf2textController import Ocean_PDF2Text
from controller.pdfqaController import PDF_QA_Controller

app = Flask(__name__)

app.config.from_pyfile('config.py')

# 使用配置中的密钥
secret_key = app.config['SECRET_KEY']
api_key = app.config['API_KEY']

app.register_blueprint(Ocean_PDF2Text)
app.register_blueprint(PDF_QA_Controller)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8980, debug=True)

