import PIL.Image
import streamlit as st
from PIL import Image
from pdf2image import convert_from_bytes
import svgwrite
import shutil


# Function to convert image to PDF
def image_to_pdf(image_path, output_path):
    im = Image.open(image_path)
    im.save(output_path, 'PDF', resolution=100.0)


# Function to convert image to SVG
def image_to_svg(image_path, output_path):
    im = Image.open(image_path)
    width, height = im.size
    dwg = svgwrite.Drawing(output_path, size=(width, height))
    dwg.add(dwg.image(image_path, insert=(0, 0), size=(width, height)))
    dwg.save()


# Function to convert PDF to images
def pdf_to_image(pdf_path, output_folder):
    pages = convert_from_bytes(pdf_path, 300,fmt="png")  # 300 DPI resolution
    for i, page in enumerate(pages):
        page.save(f'{output_folder}/page_{i}.png', 'PNG')


st.title('Imagic - Image Format Converter')

st.info("Image includes formats 'png', 'jpg', 'jpeg")
option = st.selectbox('Select Conversion Option', ('Image to PDF', 'Image to SVG', 'PDF to Image'))

if option == 'Image to PDF':
    uploaded_file = st.file_uploader('Upload an image', type=['png', 'jpg', 'jpeg'])
    if uploaded_file:
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        if st.button('Convert to PDF'):
            image_to_pdf(uploaded_file, 'output.pdf')
            file_name = uploaded_file.name.split(".")[0]
            with open("output.pdf", "rb") as pdf_file:
                PDFbyte = pdf_file.read()
            st.success('Conversion successful. Click to download.')
            st.download_button(label="Download",
                               data=PDFbyte,
                               file_name=f"{file_name}.pdf",
                               mime='application/octet-stream')


elif option == 'Image to SVG':
    uploaded_file = st.file_uploader('Upload an image', type=['png', 'jpg', 'jpeg'])
    if uploaded_file:
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        if st.button('Convert to SVG'):
            image_to_svg(uploaded_file, 'output.svg')
            st.success('Conversion successful. Click to download.')
            st.download_button(label='Download SVG', data='output.svg')

elif option == 'PDF to Image':
    uploaded_file = st.file_uploader('Upload a PDF file', type=['pdf'])
    if uploaded_file:
        if st.button('Convert to Image'):
            pdf_to_image(uploaded_file.getvalue(), 'output images')
            st.success('Conversion successful. Images saved in "output_images" folder.')
            shutil.make_archive("result", 'zip', "output images")
            with open("result.zip", "rb") as fp:
                btn = st.download_button(
                    label="Download",
                    data=fp,
                    file_name="result.zip",
                )



