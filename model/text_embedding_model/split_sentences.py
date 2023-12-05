import re
'''
@File  :__init__.py.py
@Author:Ezra Zephyr
@Date  :2023/11/2523:52
@Desc  :
'''
def split_sentences(text):
    """
    Split a text into sentences using regular expressions for both Chinese and English.

    Args:
        text (str): The input text containing sentences.

    Returns:
        list: A list of sentences.
    """
    # 使用正则表达式切分中英文文本
    sentence_delimiters = r'[。？！；;.]\s*'
    sentences = re.split(sentence_delimiters, text)

    # 去除空字符串
    sentences = [s.strip() for s in sentences if s.strip()]

    return sentences
