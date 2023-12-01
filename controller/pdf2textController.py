'''
@File  :pdf2textController.py
@Author:Ezra Zephyr
@Date  :2023/12/20:50
@Desc  :
'''
from flask import Blueprint, request, jsonify

from model.pdf2text_model.nougat_model_base import nougatProcessor_base
from model.pdf2text_model.nougat_model_small import nougatProcessor_small

Ocean_PDF2Text = Blueprint('Ocean_PDF2Text', __name__)


@Ocean_PDF2Text.route('/Ocean_PDF2Text/FacebookNougat_Base', methods=['POST'])
def OceanPDF2Text_Base():
    # Check if the request is a POST request
    if request.method == 'POST':
        try:
            # Access the JSON data from the request body
            request_data = request.get_json()

            # Check if the required fields are present in the JSON data
            if 'messages' in request_data and 'image_path' in request_data['messages'] and 'output_token' in \
                    request_data['messages']:
                image_path = request_data['messages']['image_path']
                output_token = int(request_data['messages']['output_token'])

                # Now you can use image_path and output_token as needed
                result = nougatProcessor_base(image_path, "facebook/nougat-base", output_token)

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


@Ocean_PDF2Text.route('/Ocean_PDF2Text/FacebookNougat_Small', methods=['POST'])
def OceanPDF2Text_Small():
    # Check if the request is a POST request
    if request.method == 'POST':
        try:
            # Access the JSON data from the request body
            request_data = request.get_json()

            # Check if the required fields are present in the JSON data
            if 'messages' in request_data and 'image_path' in request_data['messages'] and 'output_token' in \
                    request_data['messages']:
                image_path = request_data['messages']['image_path']
                output_token = int(request_data['messages']['output_token'])

                # Now you can use image_path and output_token as needed
                result = nougatProcessor_small(image_path, "facebook/nougat-small", output_token)

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
