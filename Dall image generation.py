# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 09:13:05 2023

@author: Administrator
"""

import openai
import urllib.request
from PIL import Image
import Streamlit as st


openai.api_key = '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'


def generate_image(image_description):
    
    image_response = openai.Image.create(
        prompt = image_description,
        n=1,
        size = '512x512')
    
    img_url = image_response['data'][0]['url']
    urllib.request.urlretrieve(img_url,'img.png')
    img = Image.open('img.png')
    return img 


#page titile
st.title('DALL E- Image Generation- openAI')

# text input box for image recoginiton
img_description = st.text_input('image_description')


if st.button('Generate Image '):
    generated_image = generate_image(img_description)
    st.Image(generated_image)


