from huggingface_hub import hf_hub_download
import re
from PIL import Image
from transformers import NougatProcessor, VisionEncoderDecoderModel
from datasets import load_dataset
import torch

'''
@File  :nougat_model_base.py
@Author:Ezra Zephyr
@Date  :2023/11/260:23
@Desc  :
'''


# https://huggingface.co/docs/transformers/main/en/model_doc/nougat

def nougatProcessor_base(filepath, model_name="facebook/nougat-base", max_tokens=200):
    """
        Process the given image file using the Nougat model.

        Args:
            filepath (str): The path to the image file.
            model_name (str): The name of the pre-trained model to use.
            max_tokens (int): The maximum number of tokens to generate.

        Returns:
            str: The generated sequence.
        """
    processor = NougatProcessor.from_pretrained(model_name)
    model = VisionEncoderDecoderModel.from_pretrained(model_name)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)
    # prepare PDF image for the model filepath
    # filename="*.png", repo_type="dataset")
    try:
        image = Image.open(filepath)
    except IOError:
        return "Error: Unable to open the image file."
    pixel_values = processor(image, return_tensors="pt").pixel_values
    outputs = model.generate(
        pixel_values.to(device),
        min_length=1,
        max_new_tokens=max_tokens,
        bad_words_ids=[[processor.tokenizer.unk_token_id]],
    )

    sequence = processor.batch_decode(outputs, skip_special_tokens=True)[0]
    sequence = processor.post_process_generation(sequence, fix_markdown=False)
    # note: we're using repr here such for the sake of printing the \n characters, feel free to just print the sequence

    return repr(sequence)



