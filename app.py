import logging
from flask import Flask, jsonify

from controller.milvusController import Milvus_Database
from controller.pdf2textController import Ocean_PDF2Text
from controller.pdfqaController import PDF_QA_Controller
from controller.textembController import Text_Emb_Controller
from config.config import Logger_Mapper

# 创建 Flask 应用实例
app = Flask(__name__)

# 配置日志级别为 INFO
app.logger.setLevel(logging.INFO)

# 将日志输出到文件
file_handler = logging.FileHandler(Logger_Mapper)
app.logger.addHandler(file_handler)

# 注册蓝图（Blueprints）以组织和模块化路由
app.register_blueprint(Ocean_PDF2Text)
app.register_blueprint(PDF_QA_Controller)
app.register_blueprint(Text_Emb_Controller)
app.register_blueprint(Milvus_Database)


# 定义全局异常处理函数
@app.errorhandler(Exception)
def handle_exception(error):
    app.logger.error(f'An error occurred: {str(error)}')
    response = jsonify({"status": "error", "message": "An unexpected error occurred"})
    response.status_code = 500
    return response


# 启动 Flask 应用
if __name__ == '__main__':
    # 启动应用，监听所有可用的网络接口，端口设置为 8980，开启调试模式
    app.run(host='0.0.0.0', port=8980, debug=True)
