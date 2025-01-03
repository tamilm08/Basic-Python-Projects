from gtts import gTTS
from pypdf import PdfReader

# Path to your PDF file
pdf_file_path = 'name.pdf'

try:
    # Open and read the PDF
    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)
        text_list = []

        # Extract text from each page
        for page_num in range(num_pages):
            try:
                page = pdf_reader.pages[page_num]
                text_list.append(page.extract_text())
            except Exception as e:
                print(f"Error extracting text from page {page_num}: {e}")
                continue

        text_string = " ".join(text_list)

        if not text_string.strip():
            print("No text extracted from the PDF.")
        else:
            print(text_string)  # Print extracted text

            # Set language for speech
            language = 'en'

            # Generate speech and save as an MP3 file
            my_audio = gTTS(text=text_string, lang=language, slow=False)
            my_audio.save("Audio.mp3")
            print("Audio file 'Audio.mp3' created successfully.")

except FileNotFoundError:
    print(f"The file '{pdf_file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
