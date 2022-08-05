
# McGregor engine detector

  

Optical Character Recognition which checks NASASpaceflight's McGregor 24/7 stream once a day and reads every test that occured along the day. Then, it writes that information into a premade spreadsheet making use of Google Drive API.

  

## Engineering

CamGear obtains a single frame from the YouTube stream. Then, it gets cropped and only relevant information is saved (the chart containing the tests that occured throughout the day). OpenCV proceeds to crop the chart into smaller, individual test images. Using different methods, these new cropped images get converted into black and white (white background with black text from the original blue background with white text) for a better OCR processing. After that, Pytesseract (Google's OCR API) extracts the text from black and white images which is later inserted into a premade Google Spreadsheet (appended to the last possible row) making use of Google Drive API.

  

## How to run
**On Ubuntu-based distributions**

*Clone the repository*

 1. `git clone https://github.com/fernandoxdev/mcgregor.git`
 2. `cd mcgregor`
 3. Make sure to have Python and PIP installed

*Install required dependencies*
 1. `sudo apt install tesseract-ocr`
 2. `sudo apt install opencv-python`
 3. `pip install opencv-python`
 4. `pip install -U vidgear[core]`
 5. `pip install Pillow`
 6. `pip install pytesseract`
 7. `pip install gspread`

*Run the code*

 1. `python main.py`


## Contribution

Please feel free to contribute to this program. Create a new branch, upload your code and make a pull request to  the main branch. If you have any doubts please contact me.

**Code developed and maintained by fernandoxdev and fernandoxdev alone.**