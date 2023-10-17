from PyPDF2 import PdfReader
import streamlit as st
import re


from transformers import BertTokenizer, BertForSequenceClassification, pipeline

st.title("PDF Text Extractor")

# File Upload
pdf_file = st.file_uploader("Upload a PDF", type=["pdf"])

# Load the BERT tokenizer and model for summarization
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForSequenceClassification.from_pretrained("bert-base-uncased")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


if pdf_file is not None:
   # Open the PDF file in binary mode
    with open('test-data.pdf', 'rb') as pdf_file:
        # Create a PDF reader object
        pdf_reader = PdfReader(pdf_file)

        # Initialize a variable to store the extracted text
        extracted_text = ''

        # Iterate through each page in the PDF
        for page_num in range(len(pdf_reader.pages)):
            # Get the page
            page = pdf_reader.pages[page_num]

            # Extract text from the page
            page_text = page.extract_text()

            # Remove extra spaces using regular expressions
            page_text = re.sub(r'\s+', ' ', page_text).strip()

            # Append the page text to the extracted_text variable
            extracted_text += page_text
            # print(extracted_text)

            
            summary = summarizer(extracted_text, max_length=150, min_length=30, do_sample=False)

            bert_summary = summary[0]["summary_text"]

    st.write(bert_summary)


