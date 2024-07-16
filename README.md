# IMagic
[imagic.streamlit.app](https://imagic.streamlit.app)
 

**Work in Progress**

---

## Image Insight

Harness the power of the Gemini Flash API to effortlessly extract and analyze text from images. This feature is perfect for digitizing documents, extracting information from photos, and much more.

## Image Generator

Create stunning and unique images Stable Diffusion's AI-powered image generation tools. Input any prompt and generate high-quality images that match your descriptions. Whether you're seeking artistic inspiration or generating visuals for projects, Image Generator has you covered.

## Image Compression

Reduce file sizes with the K-means clustering algorithm-based compression feature. Make your images web-friendly and easy to share.

## Image Upscaler

Enhance your images with Stable Diffusion's upscaling tools, leveraging Stable Diffusion to increase resolution and improve quality.
    
    
## Image Format Convertor

Convert your images to pdf to using pdf2image


## Image Background Remover

Remove background images using rembg

--- 
## Steps to Install

- Go your project's directory
- Clone Repo

```
git clone https://github.com/sahil-s-246/IMagic.git
```
- Install requirements
```
pip install -r requirements.txt
```
- Put your api keys in the ```secrets.toml``` file. This file is present in the ```.streamlit``` folder
- Import those API keys using
```python
import streamlit as st
Req_API_Key = st.secrets["general"]["Req_API"]
```
- Run the program on localhost, optionally specify the port number
```
streamlit run streamlit_app.py --server.port 8081
```
---
## Image Insights on CLI
- Create a ```val.cfg``` file. Create a section [Api] and your API as a key value pair
```
[Api]
gemini:<API_KEY>
```
- Open your terminal in the project directory

```
pip install .
```
- Get insights by providing the path of the image
```
imagic -i <Example.jpg>
```



