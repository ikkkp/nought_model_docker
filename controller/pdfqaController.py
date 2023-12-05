"""
@File  :pdfqaController.py
@Author:Ezra Zephyr
@Date  :2023/12/21:09
@Desc  :
"""

from flask import Blueprint, request, jsonify
from model.pdf2text_model.layoutlm_document_qa import layoutlm_document_qa

PDF_QA_Controller = Blueprint('PDF_QA_Controller', __name__)


@PDF_QA_Controller.route('/PDF_QA_Controller/FacebookNougat_Base', methods=['POST'])
def PDFQA_Controller():
    # Check if the request is a POST request
    if request.method == 'POST':
        try:
            # Access the JSON data from the request body
            request_data = request.get_json()

            # Check if the required fields are present in the JSON data
            if 'messages' in request_data and 'image_path' in request_data['messages'] and 'question' in \
                    request_data['messages']:
                image_path = request_data['messages']['image_path']
                output_token = request_data['messages']['question']

                # Now you can use image_path and output_token as needed
                result = layoutlm_document_qa(image_path, output_token)

                # Return the result as JSON
                return jsonify({"status": "success", "result": result})
            else:
                # Return an error response if the required fields are not present
                return jsonify({"status": "error", "error": "Invalid JSON format"}), 400

        except Exception as e:
            # Handle any exceptions that may occur during processing
            return jsonify({"error": str(e)}), 500
    else:
        # Handle other HTTP methods if necessary
        return 'Method Not Allowed', 405
