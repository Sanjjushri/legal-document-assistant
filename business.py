import re
from PyPDF2 import PdfReader

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

# Print or use the extracted text as needed
print(extracted_text)
