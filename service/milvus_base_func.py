"""
@File  : milvus_base_fun.py
@Author: Ezra Zephyr
@Date  : 2023/12/5 15:01
@Desc  : This module provides helper functions for interacting with Milvus database.
"""

import json
import requests

from config.config import Database_NAME, Milvus_Base, Milvus_API_KEY


def Milvus_Database_base_insert_func(vec_embedding):
    """
    Perform Milvus database insertion.

    Args:
        vec_embedding (list): The embedding vector to be inserted into the Milvus database.

    Returns:
        response (Response): The HTTP response object from the Milvus database API.
    """
    new_data = {
        "collectionName": Database_NAME,
        "data": [
            {
                "vector": vec_embedding
            }
        ]
    }

    url = Milvus_Base + "insert"
    new_data_json = json.dumps(new_data)
    headers = {
        "Authorization": "Bearer " + Milvus_API_KEY,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    response = requests.post(url, data=new_data_json, headers=headers)
    return response


def Milvus_Database_base_search_func(vec_embedding):
    """
    Perform Milvus database search.

    Args:
        vec_embedding (list): The embedding vector to be used for searching in the Milvus database.

    Returns:
        response (Response): The HTTP response object from the Milvus database API.
    """
    new_data = {
        "collectionName": Database_NAME,
        "vector": vec_embedding
    }

    url = Milvus_Base + "search"
    new_data_json = json.dumps(new_data)
    headers = {
        "Authorization": "Bearer " + Milvus_API_KEY,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    response = requests.post(url, data=new_data_json, headers=headers)
    return response


def Milvus_Database_base_get_func(vec_embedding):
    """
    Perform Milvus database retrieval.

    Args:
        vec_embedding (list): The embedding vector ID to be used for retrieving data from the Milvus database.

    Returns:
        response (Response): The HTTP response object from the Milvus database API.
    """
    new_data = {
        "collectionName": Database_NAME,
        "id": vec_embedding
    }

    url = Milvus_Base + "get"
    new_data_json = json.dumps(new_data)
    headers = {
        "Authorization": "Bearer " + Milvus_API_KEY,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    response = requests.post(url, data=new_data_json, headers=headers)
    return response
