import os
from pypdf import PdfMerger

# Define the folder containing the PDF files
folder_path = "./AppointmentLetters/"

# List all PDF files in the folder
pdfs = [
    os.path.join(folder_path, file)
    for file in os.listdir(folder_path)
    if file.endswith(".pdf")
]

# Create a PdfMerger object
merger = PdfMerger()

# Append each PDF file to the merger
for pdf in pdfs:
    merger.append(pdf)

# Write the merged PDF to a new file
merger.write("result.pdf")
merger.close()
