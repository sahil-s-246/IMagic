import streamlit as st

import os
import io
import warnings
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

stability_api = client.StabilityInference(
    key=st.secrets["general"]["stability"], # API Key reference.
    upscale_engine="esrgan-v1-x2plus", # The name of the upscaling model we want to use.
                                       # Available Upscaling Engines: esrgan-v1-x2plus
    verbose=True, # Print debug messages.
)
upload = st.file_uploader("Upload your image to be upscaled here",type=['png', 'jpg', 'jpeg', 'svg'])
st.info("Please upload an Image to be upscaled")
if upload:
    img = Image.open(upload)
# St.file_uploader returns IO bytes which can directly be fed to PIL.Image
    answers = stability_api.upscale(
        init_image=img, # Pass our image to the API and call the upscaling process.
        # width=1024, # Optional parameter to specify the desired output width.
    )
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn(
                    "Your request activated the API's safety filters and could not be processed."
                    "Please submit a different image and try again.")
            if artifact.type == generation.ARTIFACT_IMAGE:
                big_img = Image.open(io.BytesIO(artifact.binary))
                st.image(big_img)
                st.download_button("Download", io.BytesIO(artifact.binary), mime="jpg", file_name="up_scaled.jpg")

                big_img.save("imageupscaled" + ".png") # Save our image to a local file.
