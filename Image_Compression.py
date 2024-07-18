import streamlit as st
import joblib
from model import load_and_flatten_image
from PIL import Image
import io

st.title("IMagic Compression")
"Reduce file sizes with the K-means clustering algorithm-based compression feature. Make your images web-friendly and "\
    "easy to share "

img = st.file_uploader("Upload your file to be compressed: ")
comp = st.selectbox("Choose the type of compression:", ["Low", "High"], placeholder="High or Low",index=None)
if img:
    if comp == "Low":
        compressed_data = load_and_flatten_image(img)
        model = joblib.load("kmeans_model.pkl")
        new_data = model.cluster_centers_[model.predict(compressed_data)]
        new_image = new_data.reshape(Image.open(img).size[1], Image.open(img).size[0], 3).astype('uint8')
        result = Image.fromarray(new_image)
        with st.spinner("Compressing..."):
            c1, c2 = st.columns(2)
            c1.write("Original")
            c1.image(img)
            c2.write("Compressed")
            c2.image(result)
            img_byte_arr = io.BytesIO()
            result.save(img_byte_arr, format='JPEG')  # You can change 'PNG' to the format you need
            img_byte_arr = img_byte_arr.getvalue()
            c2.download_button("Download Result", img_byte_arr, f"{img.name.split('.')[0]}.jpg")
            c1.download_button("Download Original", img, f"{img.name.split('.')[0]}.jpg")
    elif comp == "High":
        st.info("Work in Progress!")
    else:
        st.info(
            "Low Quality utilizes a trained model while High Quality refers to the fitting of the model "
            "on the image data")
# todo PNG, more clusters