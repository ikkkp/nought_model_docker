"""
File     : text_emb_controller.py
Author   : Ezra Zephyr
Date     : 2023/12/5 10:38
Desc     : Text embedding controller for Flask app.
"""

from flask import Blueprint, request, jsonify
from model.text_embedding_model.text_embedding_v2 import embed_with_str
from config.config import Aliyun_Embedding_API_KEY

Text_Emb_Controller = Blueprint('Text_Emb_Controller', __name__)


@Text_Emb_Controller.route('/Text_Emb_Controller/text_embedding_v2', methods=['POST'])
def text_embedding_v2():
    try:
        request_data = request.get_json()

        # Check if the required fields are present in the JSON data
        if 'messages' in request_data and 'text_msg' in request_data['messages']:
            text_msg = request_data['messages']['text_msg']

            # Call the text embedding function with the API key and text message
            resp = embed_with_str(Aliyun_Embedding_API_KEY, text_msg)

            # Return JSON response with success status and result
            return jsonify({"status": "success", "result": resp})
        else:
            # Return JSON response with error status if required fields are missing
            return jsonify({"status": "error", "message": "Required fields are missing in the JSON data"}), 400
    except Exception as e:
        # Return JSON response with error status and exception details
        return jsonify({"status": "error", "message": str(e)}), 500
