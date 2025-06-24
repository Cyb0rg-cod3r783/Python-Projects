# Import the PdfWriter class from the PyPDF2 library to work with PDF files
from PyPDF2 import PdfWriter

# Create a PdfWriter object that will be used to merge the PDFs
merger = PdfWriter()

# Initialize an empty list to hold the names of the PDF files to be merged
pdfs = []

# Ask the user how many PDFs they want to merge and convert the input to an integer
n = int(input("How many pdfs do you want to merge? : "))

# Loop to collect the filenames of the PDFs to be merged
for i in range(0, n):
    pdf_name = input("Enter the name of the pdf : ")  # Prompt user for each PDF file name
    pdfs.append(pdf_name)  # Add the file name to the list

# Loop through the list of PDF filenames and append each to the merger object
for pdf in pdfs:
    merger.append(pdf)  # Add the current PDF file to the merger

# Write out the merged PDF to a new file named "merged-pdf.pdf"
merger.write("merged-pdf.pdf")

# Close the merger to free up system resources
merger.close()