# Screen Capture Search Tool

## Overview
This Python application creates a transparent, draggable window that users can position over a screen area to capture text or images. Once captured, it automatically performs a Google search with the extracted text or an image search on Yandex. The tool is particularly useful for quickly looking up information based on screen content, such as in presentations, documents, or web pages.

## Key Features
- **Transparent, Movable Window**: Provides a resizable window that can be moved over the area of interest on the screen.
- **Text Capture and Google Search**: Captures text from the specified region using `pytesseract` for Optical Character Recognition (OCR) and conducts a Google search with the extracted text.
- **Image Capture and Yandex Search**: Takes a screenshot of the defined area and performs an image search using Yandex.
- **Hotkey Triggered Actions**: The tool captures text or images based on specific keyboard shortcuts for quick operation.
- **Customizable Window Size and Position**: Allows setting the initial size and position of the capture window.

## Running the Program
To run this tool, follow these steps:

1. **Environment Setup**:
   - Ensure Python is installed on your system along with the necessary libraries: `tkinter`, `pyautogui`, `keyboard`, `pytesseract`, `requests`.
   - Install Tesseract OCR and set the `tesseract_cmd` path in the script.
   - Install any missing libraries using pip (e.g., `pip install pytesseract`).

2. **Run the Script**:
   - Execute the script using Python: `python Main.py`.
   - A transparent window will appear, which can be moved and resized as needed.

3. **Usage**:
   - Position the transparent window over the desired screen area.
   - Press `Alt` to capture text and search on Google.
   - Press `Ctrl` to capture an image and search on Yandex.

## Note
- The initial size and position of the window can be adjusted in the script.
- Ensure the correct paths are set for Tesseract OCR's executable and data.

## Contribution
Contributions are welcome to improve this tool, such as adding support for different search engines, optimizing performance, or enhancing user experience.

## License
Free To Use.
