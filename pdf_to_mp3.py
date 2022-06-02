from gtts import gTTS
from pathlib import Path
import PyPDF2


def pdf_to_mp3(file_path, file_name):
    # check pdf file
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        # create reader and read pdf file
        reader = PyPDF2.PdfReader(file_path)
        number_of_pages = len(reader.pages)
        pages_list = []
        for enumerate_page in range(number_of_pages):
            page = reader.pages[enumerate_page]
            pages_list.append(page.extract_text())
        # create variable with all text
        all_text = ''.join(pages_list)
        all_text.replace('\n', '')
        # create and save mp3 file
        music_file = gTTS(all_text)
        music_file.save(f'{file_name}.mp3')
    else:
        return 'File not exsists... Try again, please'


if __name__ == '__main__':
    file_path = input('Enter path to your file: ').strip()
    file_name = input('Enter file name: ').strip()

    pdf_to_mp3(file_path=file_path, file_name=file_name)
