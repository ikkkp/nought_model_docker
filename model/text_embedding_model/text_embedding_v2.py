"""
File   : text_embedding_v2.py
Author : Ezra Zephyr
Date   : 2023/11/25 22:23
Desc   : Alibaba Cloud General Text Embedding - Universal Language Model-based Multilingual Text Unified Vector Model.
         Quickly converts text data into high-quality vector data.
         More information: https://help.aliyun.com/zh/dashscope/developer-reference/text-embedding-quick-start?disableWebsiteRedirect=true
"""

import dashscope

def embed_with_str(api_key, input_str):
    """
    Embeds the input string using the Alibaba Cloud General Text Embedding API.

    Args:
        api_key (str): The API key for accessing the DashScope Text Embedding API.
        input_str (str): The input text to be embedded.

    Returns:
        None: Prints the API response.
    """

    resp = dashscope.TextEmbedding.call(
        model=dashscope.TextEmbedding.Models.text_embedding_v1,
        input=input_str,
        api_key=api_key
    )

    return repr(resp)


# Example Usage:
# api_key = "your_api_key"
# input_text = "your_input_text"
# embed_with_str(api_key, input_text)
