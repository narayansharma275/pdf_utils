import os
import argparse
from pypdf import PdfWriter

def combine_pdfs(folder_path, output_filename="CombinedPDF.pdf"):
    writer = PdfWriter()

    sorted_files = sorted(os.listdir(folder_path))
    
    # Iterate through all files in the folder
    for ele in sorted_files:
        if ele.endswith('.pdf'):
            writer.append(os.path.join(folder_path, ele))

    # Define the output path
    output_path = os.path.join(folder_path, output_filename)

    # Write the combined PDF to the output file
    with open(output_path, "wb") as output_pdf:
        writer.write(output_pdf)

    print(f"Combined PDF saved as {output_path}")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Combine PDFs in a folder into a single PDF.")
    parser.add_argument("folder_path", help="Path to the folder containing PDFs to combine.")
    parser.add_argument("-o", "--output", help="Name of the output PDF file (default: CombinedPDF.pdf).", default="CombinedPDF.pdf")

    # Parse arguments
    args = parser.parse_args()

    # Call the function to combine PDFs
    combine_pdfs(args.folder_path, args.output)
