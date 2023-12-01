'''
@File  :layoutlm_document_qa.py
@Author:Ezra Zephyr
@Date  :2023/11/260:23
@Desc  :基于transformer的OCR的PDF读取问答
'''
from transformers import pipeline


def layoutlm_document_qa(image_url, question, model_name='impira/layoutlm-document-qa'):
    """
    Perform document-based question answering using LayoutLM.

    Args:
        image_url (str): The URL of the image containing the document.
        question (str): The question related to the document.
        model_name (str): The name of the pre-trained LayoutLM model.

    Returns:
        dict: A dictionary containing the model's answer, score, start, and end positions.
    """
    nlp = pipeline("document-question-answering", model=model_name)

    result = nlp(image_url, question)
    return result

# Example Usage:
# image_url = "https://templates.invoicehome.com/invoice-template-us-neat-750px.png"
# question = "What is the invoice number?"
# result = layoutlm_document_qa(image_url, question)
# print(result)
