from rembg import remove
import streamlit as st
import io
from PIL import Image

st.title("IMagic Background Remover")
"Remove background using rembg "

upload = st.file_uploader("Upload your image here",type=['png', 'jpg', 'jpeg', 'svg'])
st.info("Please upload an Image to be whose bg is to be removed")
if upload:
    img = Image.open(upload)
    file_name = upload.name.split(".")[0]
# St.file_uploader returns IO bytes which can directly be fed to PIL.Image
    rem = remove(img)
    # image = Image.open(io.BytesIO(rem))
    st.write("Result")
    st.image(rem)
    img_byte_arr = io.BytesIO()
    rem.save(img_byte_arr, format='PNG')  # You can change 'PNG' to the format you need
    img_byte_arr = img_byte_arr.getvalue()
    st.download_button("Download", img_byte_arr, mime="png", file_name=f"{file_name}.jpg")
