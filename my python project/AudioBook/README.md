Here's a `README.md` file that you can use to explain how to set up and run the script for text extraction and conversion to speech from a PDF.

---

# Text-to-Speech from PDF

This project converts text from a PDF file into speech and saves the result as an MP3 file using Python. It utilizes the `gTTS` library for text-to-speech conversion and `PyPDF2` (or `pypdf`) for extracting text from PDF files.

## Requirements

- Python 3.x
- Libraries: `gTTS`, `PyPDF2` (or `pypdf` for newer versions), `pytesseract` (optional, for OCR on image-based PDFs), `pdf2image` (optional, for OCR on image-based PDFs)

## Installation

1. **Install Python 3.x**
   - Download and install Python from [https://www.python.org/downloads/](https://www.python.org/downloads/).

2. **Install Required Libraries**
   You can install the required libraries using `pip`. Open a terminal and run the following command:
   
   ```bash
   pip install gTTS PyPDF2 pypdf pytesseract pdf2image
   ```

   If you prefer using `pypdf` instead of `PyPDF2`, run:

   ```bash
   pip install pypdf
   ```

   **Note**: For OCR (Optical Character Recognition) functionality, you'll need Tesseract installed on your system. You can download Tesseract from [here](https://github.com/tesseract-ocr/tesseract). After installation, ensure the `tesseract` command is available in your system's PATH.

## Usage

1. **Prepare Your PDF**
   - Ensure the PDF file is in the same directory as your script. You can use any PDF with text (or an image-based PDF if you're using OCR).

2. **Save the Script**
   - Save the Python script provided in a file (e.g., `Audiobook.py`).

3. **Run the Script**
   - Open the terminal in the directory where your script is saved.
   - Run the script using Python:

   ```bash
   python Audiobook.py
   ```

   The script will extract text from the PDF and convert it into speech. The resulting speech will be saved as `Audio.mp3` in the same directory.

4. **Handling Errors**
   - If you encounter errors such as `EOF marker not found`, it might indicate the PDF is corrupted. You can try to repair the PDF or use another PDF.
   - If the PDF is scanned or image-based, the text extraction might fail. In that case, the script will attempt to use OCR (if you have Tesseract and `pytesseract` installed).

## Code Explanation

### **Main Steps:**
1. **PDF Text Extraction**: The script uses `PyPDF2` or `pypdf` to extract text from each page of the PDF. The text is then concatenated into one string.
   
2. **Text-to-Speech Conversion**: The `gTTS` library converts the extracted text into speech and saves it as an MP3 file.

### **Error Handling:**
- The script includes basic error handling for PDF reading and text extraction. If no text is found or if there is an issue with the PDF, an error message will be displayed.

### **Optional OCR (Tesseract)**:
If the PDF is image-based (e.g., scanned documents), Tesseract OCR will be used to extract text from images. This is done using the `pytesseract` and `pdf2image` libraries.

## Troubleshooting

- **EOF Marker Not Found**: This error occurs when the PDF is corrupted or incomplete. Try using a different PDF or repair the current one using online tools.
- **OCR Not Working**: Ensure that Tesseract is properly installed and available in your system's PATH.
- **No Text Extracted**: If the PDF is image-based, ensure OCR is enabled, or try using a text-based PDF instead.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to copy and paste this `README.md` file into your project folder. If you need any more information or adjustments, let me know!
