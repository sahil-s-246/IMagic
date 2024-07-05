import streamlit as st
import io
from PIL import Image
import requests

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": st.secrets["general"]["hftoken"]}

st.title("IMagic Generation using stable diffusion")

"Create stunning and unique images Stable Diffusion's AI-powered image generation tools. Input any prompt and " \
    "generate high-quality images that match your descriptions. Whether you're seeking artistic inspiration or " \
    "generating visuals for projects, Image Generator has you covered. "
prompt = st.text_area("Describe the image here")


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content


if prompt.strip():
    image_bytes = query({
        "inputs": prompt.strip(),
    })

    # You can access the image with PIL.Image for example

    with st.spinner("Loading..."):
        image = Image.open(io.BytesIO(image_bytes))
        st.write("Output")
        st.image(image)
        # with open("result.jpg","wb+") as f:
        #     f.write(image_bytes)
        st.download_button("Download", image_bytes,mime="jpg", file_name="prompt_result.jpg")
else:
    st.info("Type your prompt to get the image")
