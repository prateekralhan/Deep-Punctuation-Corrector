import streamlit as st
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline
import fitz
import docx
import re

@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def instantiate_model(plain_text):
    tokenizer = AutoTokenizer.from_pretrained("oliverguhr/fullstop-punctuation-multilang-large")
    model = AutoModelForTokenClassification.from_pretrained("oliverguhr/fullstop-punctuation-multilang-large")
    pun = pipeline('ner', model=model, tokenizer=tokenizer)
    return pun(plain_text)

@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def generate_result(output_json):
    s = ''

    for n in output_json:
        result = n['word'].replace('▁',' ') + n['entity'].replace('0','')
        s += result
    return s


@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def extract_text_txt(uploaded_txt_file,downloaded_txt_file):
    with open(uploaded_txt_file) as intxt:
        data = intxt.read()

    data = re.findall('[aA-zZ]+', data)
    with open(downloaded_txt_file, 'w') as outtxt:
        outtxt.write('\n'.join(data))
    return ' '.join(data)


@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def extract_text_pdf(uploaded_pdf_file):
    with fitz.open(uploaded_pdf_file) as intxt:
        text = ""
        for page in intxt:
            text += page.get_text()
    return text


@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def extract_text_docx(uploaded_docx_file):
    doc = docx.Document(uploaded_docx_file)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return ' '.join(fullText)


@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def download_success():
    st.balloons()
    st.success('✅ Punctuation has been applied successfully !!')
