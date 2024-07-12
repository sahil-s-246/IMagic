import streamlit as st
import google.generativeai as genai
import PIL.Image
from gtts import gTTS
import requests

st.title("IMagic Insight")

"Harness the power of the Gemini Flash API to effortlessly extract and analyze text from images. " \
    "This feature is perfect for digitizing documents, extracting information from photos, and much more."


def get_img(file="images/example.jpg", overlay=True, language='eng'):
    data = {
        'isOverlayRequired': overlay,
        'apikey': st.secrets["general"]["ocrspace"],
        'language': language,
        'isCreateSearchablePdf': True,
        'OCREngine': 2

    }
    with open(file, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={file: f},
                          data=data,
                          )
    print(r.json()['ParsedResults'][0]['ParsedText'])
    with open("result.pdf", 'wb') as w:
        response = requests.get(r.json()['SearchablePDFURL'])
        w.write(response.content)
    return r.json()['ParsedResults'][0]['ParsedText']


genai.configure(api_key=st.secrets["general"]["gemini"])
image = st.file_uploader("Upload your image")
if image:
    img = PIL.Image.open(image)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(["What is in this photo?", img])
    with st.spinner("Loading"):
        st.markdown(f"###### {response.text}")
        obj = gTTS(text=response.text, lang="en", slow=False)
        obj.save("insight.mp3")
        st.audio("insight.mp3")
