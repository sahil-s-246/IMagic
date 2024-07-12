import streamlit as st

pg = st.navigation([st.Page("Home.py"),
                    st.Page("Image_Insight.py"),
                    st.Page("Image_Generator.py"),
                    st.Page("Image_Upscaler.py"),
                    st.Page("Image_Compression.py")])
pg.run()