import os
import PyPDF2 as pdf
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load the environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="Application Tracking System", page_icon=":robot:")


#Prompt Template
input_prompt="""
You are a skilled and very experience ATS(Application Tracking System) with a deep understanding of tech field,software engineering,
data science ,data analyst, and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide best assistance for improving thr resumes. 
Assign the percentage Matching based on Job description and the missing keywords with high accuracy
Resume:
Description:

I want the only response in 3 sectors as follows:
• Job Description Match: \n
•  MissingKeywords: \n
• Profile Summary: \n
"""

## streamlit app
st.title("APPLICATION TRACKING SYSTEM")
st.text("Improve Your Resume ATS Score")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        reader=pdf.PdfReader(uploaded_file)
        extracted_text=""
        for page in range(len(reader.pages)):
            page=reader.pages[page]
            extracted_text+=str(page.extract_text())
        response = model.generate_content(input_prompt)
        st.write(response.text)
