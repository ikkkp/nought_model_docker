'''
@File  :trocr_base_handwritten.py
@Author:Ezra Zephyr
@Date  :2023/11/260:19
@Desc  :手写体识别
'''
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import requests


def trocr_base_handwritten(url, model_name='microsoft/trocr-base-handwritten'):
    """
    Perform OCR on a handwritten image using TrOCR.

    Args:
        url (str): The URL of the image to be processed.
        model_name (str): The name of the pre-trained TrOCR model.

    Returns:
        str: The generated text from the image.
    """
    # Load image from the provided URL
    image = Image.open(requests.get(url, stream=True).raw).convert("RGB")

    # Initialize TrOCR processor and model
    processor = TrOCRProcessor.from_pretrained(model_name)
    model = VisionEncoderDecoderModel.from_pretrained(model_name)

    # Process the image and generate text
    pixel_values = processor(images=image, return_tensors="pt").pixel_values
    generated_ids = model.generate(pixel_values)
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

    return generated_text

# Example Usage:
# url = 'https://fki.tic.heia-fr.ch/static/img/a01-122-02-00.jpg'
# result = trocr_base_handwritten(url)
# print(result)
