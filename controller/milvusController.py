"""
@File  : milvusController.py
@Author: Ezra Zephyr
@Date  : 2023/12/5 13:18
@Desc  : This module defines a Flask Blueprint for handling Milvus database operations.
"""

import json
from flask import Blueprint, request, jsonify
import requests
from config.config import Milvus_API_KEY, Milvus_Base, Aliyun_Embedding_API_KEY, Database_NAME
from model.text_embedding_model.text_embedding_v2 import embed_with_str
from service.milvus_base_func import Milvus_Database_base_insert_func

# Create a Flask Blueprint for Milvus Database operations
Milvus_Database = Blueprint('Milvus_Database', __name__)


# TODO Text Embedding Vec写入MongoDB逻辑尚未完成


@Milvus_Database.route('/Milvus_Database/Milvus_Database_insert', methods=['POST'])
def Milvus_Database_insert():
    """
    Endpoint for handling Milvus database insertion using embeddings from a JSON payload.

    Returns:
        JSON response containing the status, message, and Milvus API response.
    """
    # Get JSON data from the POST request
    request_data = request.get_json()

    # Check if required fields are present in the JSON data
    if 'result' in request_data and 'output' in request_data['result'] and 'embeddings' in request_data['result'][
        'output']:
        embeddings = request_data['result']['output']['embeddings']

        # Check if embeddings are present and proceed with the first embedding
        if embeddings:
            vec_embedding = embeddings[0]['embedding']
            response = Milvus_Database_base_insert_func(vec_embedding)

            return jsonify({"status": "success", "message": "Embedding extracted successfully",
                            "response": json.dumps(response.json())})

    return jsonify({"status": "error", "message": "Invalid JSON format or missing required fields"})


@Milvus_Database.route('/Milvus_Database/Milvus_Database_insert_by_string', methods=['POST'])
def Milvus_Database_insert_by_string():
    """
    Endpoint for handling Milvus database insertion using text message from a JSON payload.

    Returns:
        JSON response containing the status, message, and Milvus API response.
    """
    # Get JSON data from the POST request
    request_data = request.get_json()

    # Check if required fields are present in the JSON data
    if 'messages' in request_data and 'text_msg' in request_data['messages']:
        text_msg = request_data['messages']['text_msg']

        # Call the text embedding function with the API key and text message
        resp = embed_with_str(Aliyun_Embedding_API_KEY, text_msg)

        # Check if required fields are present in the API response
        if 'output' in resp and 'embeddings' in resp['output']:
            embeddings = resp['output']['embeddings']

            # Check if embeddings are present and proceed with the first embedding
            if embeddings:
                vec_embedding = embeddings[0]['embedding']
                response = Milvus_Database_base_insert_func(vec_embedding)

                return jsonify({"status": "success", "message": "Embedding extracted successfully",
                                "response": json.dumps(response.json())})

    return jsonify({"status": "error", "message": "Invalid JSON format or missing required fields"})
