import streamlit as st
import os
from PIL import Image
from app_funcs import *
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Punctuation Corrector",
    page_icon="🛠",
    layout="centered",
    initial_sidebar_state="auto",
)

top_image = Image.open('static/banner_top.png')
bottom_image = Image.open('static/banner_bottom.png')
main_image = Image.open('static/main_banner.png')

upload_path = "uploads/"
download_path = "downloads/"

st.sidebar.image(top_image,use_column_width='auto')
format_type = st.sidebar.selectbox('Apply Punctuation for? 🎯',["Plain Text","Documents"])
st.sidebar.image(bottom_image,use_column_width='auto')

st.image(main_image,use_column_width='auto')
st.title("📄 Deep Punctuation Corrector 🛠")

if format_type == "Plain Text":
    text = st.text_area("Enter your text here: 🎯", height=300)

    if st.button("Fix  Punctuation ✨"):
        with st.spinner(f"Fixing Punctuation... 💫"):
            output_json = instantiate_model(text)
            final_text = generate_result(output_json)

        if final_text:
            st.markdown(final_text)
            download_success()
    else:
        st.warning("Please enter the text and choose \"Fix Punctuation ✨\"")

if format_type == "Documents":
    st.info('Supports all popular document formats 📄 - TXT, PDF, DOCX 😉')
    uploaded_file = st.file_uploader("Upload Document 📃", type=["txt","pdf","docx"])
    if uploaded_file is not None:
        with open(os.path.join(upload_path,uploaded_file.name),"wb") as f:
            f.write((uploaded_file).getbuffer())
        if uploaded_file.name.endswith('.txt') or uploaded_file.name.endswith('.TXT'):
            with st.spinner(f"Fixing Punctuation... 💫"):
                uploaded_txt_file = os.path.abspath(os.path.join(upload_path,uploaded_file.name))
                downloaded_txt_file = os.path.abspath(os.path.join(download_path,str("processed_"+uploaded_file.name)))
                txt = extract_text_txt(uploaded_txt_file,downloaded_txt_file)
                output_json = instantiate_model(txt)
                final_text = generate_result(output_json)
                if final_text:
                    st.markdown(final_text)
                    download_success()

        if uploaded_file.name.endswith('.pdf') or uploaded_file.name.endswith('.PDF'):
            with st.spinner(f"Fixing Punctuation... 💫"):
                uploaded_pdf_file = os.path.abspath(os.path.join(upload_path,uploaded_file.name))
                txt = extract_text_pdf(uploaded_pdf_file)
                output_json = instantiate_model(txt)
                final_text = generate_result(output_json)
                if final_text:
                    st.markdown(final_text)
                    download_success()

        if uploaded_file.name.endswith('.docx') or uploaded_file.name.endswith('.DOCX'):
            with st.spinner(f"Fixing Punctuation... 💫"):
                uploaded_docx_file = os.path.abspath(os.path.join(upload_path,uploaded_file.name))
                txt = extract_text_docx(uploaded_docx_file)
                output_json = instantiate_model(txt)
                final_text = generate_result(output_json)
                if final_text:
                    st.markdown(final_text)
                    download_success()

    else:
        st.warning('⚠ Please upload your document 😯')



st.markdown("<br><hr><center>Made with ❤️ by <a href='mailto:ralhanprateek@gmail.com?subject=Deep Punctuation Corrector WebApp!&body=Please specify the issue you are facing with the app.'><strong>Prateek Ralhan</strong></a></center><hr>", unsafe_allow_html=True)
