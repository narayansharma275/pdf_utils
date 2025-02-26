# PDF Combiner Script

This Python script combines multiple PDF files from a specified folder into a single PDF. The files are processed in alphabetical or numerical order, and the output is saved in the same folder.

## Features

- Combines all PDFs in a folder into a single PDF.
- Sorts files alphabetically or numerically before combining.
- Allows customization of the output file name.
- Saves the combined PDF in the same folder as the input files.

## Requirements

- Python 3.x
- `pypdf` library

## Installation

1. **Install Python**: Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Install the `pypdf` library**:
   Run the following command to install the required library:
   ```bash
   pip install pypdf
   ```

3. **Download the Script**:
   - Save the script as combine_pdfs.py.
   - Place it in a directory where you can easily run it from the terminal.

## Usage

Run the script from the terminal with the following command:
```bash
python combine_pdfs.py /path/to/your/folder -o OutputFileName.pdf
```

## Arguments

- **`folder_path`**: (Required) The path to the folder containing the PDF files to combine.
- **`-o` or `--output`**: (Optional) The name of the output PDF file. If not provided, the default name `CombinedPDF.pdf` will be used.

## Examples

1. Combine all PDFs in the folder `/home/user/pdfs` and save the output as `MergedPDF.pdf`:
   ```bash
   python combine_pdfs.py /home/user/pdfs -o MergedPDF.pdf
   ```
2.  Combine all PDFs in the folder `/home/user/pdfs` and save the output using the default output file name:
   ```bash
   python combine_pdfs.py /home/user/pdfs
   ```
  
