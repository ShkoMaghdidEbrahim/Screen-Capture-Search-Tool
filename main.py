import json
import threading
import tkinter as tk
import webbrowser

import keyboard
import pyautogui
import pytesseract
import requests

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.TESSDATA_PREFIX = r'C:\Program Files\Tesseract-OCR\tessdata'
xPos = 10
yPos = 270
winWidth = 360
winHeight = 100

class TransparentWindow :
    def __init__(self, master, x, y, width, height, border_width = 10, border_color = "black") :
        self.master = master
        self.master.title("Transparent Window")
        self.master.geometry(f"{width}x{height}+{x}+{y}")

        # Make the window transparent
        self.master.attributes("-alpha", 0.5)

        # Remove window decorations (title bar, etc.)
        self.master.overrideredirect(True)

        # Create a frame with a border
        self.border_frame = tk.Frame(self.master, bg = border_color, bd = border_width)
        self.border_frame.pack(fill = "both", expand = True)

        # Set the window to always stay on top
        self.master.attributes("-topmost", True)

        # Add bindings for dragging the window
        self.master.bind("<B1-Motion>", self.drag_window)
        self.master.bind("<ButtonPress-1>", self.start_drag)

        # Variables to store the initial position of the drag
        self.start_x = 0
        self.start_y = 0

    def start_drag(self, event) :
        self.start_x = event.x
        self.start_y = event.y

    def drag_window(self, event) :
        x = self.master.winfo_x() - self.start_x + event.x
        y = self.master.winfo_y() - self.start_y + event.y
        self.master.geometry(f"{winWidth}x{winHeight}+{x}+{y}")
        # Update xPos and yPos
        global xPos, yPos
        xPos, yPos = x, y

    def hide(self) :
        self.master.withdraw()

    def show(self) :
        self.master.update()
        self.master.deiconify()

# Declare window as a global variable
window = None

def read_specified_region(left, top, width, height) :
    screenshot = pyautogui.screenshot(region = (left, top, width, height))
    screenshot.save("screenshot.png")
    tessdata_dir_config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'
    return pytesseract.image_to_string(screenshot, config = "--psm 13")

def google_text_search(query) :
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url, new = 0, autoraise = True)

def process_screenshot_text() :
    global window
    window.hide()  # Hide the Tkinter window before taking the screenshot
    region = (xPos, yPos, winWidth, winHeight)
    region_text = read_specified_region(*region)
    print("Text from the specified region:")
    cleaned_text = region_text.replace('\n', ' ').replace(':', ' ').replace('&', ' and ').replace('_', ' ').replace(
        '   ', ' ').replace('  ', ' ')
    print(cleaned_text)
    google_text_search(cleaned_text)
    window.show()  # Show the Tkinter window again after processing the screenshot

def tkinter_thread() :
    global window
    root = tk.Tk()
    window = TransparentWindow(root, x = xPos, y = yPos, width = winWidth, height = winHeight, border_width = 3,
                               border_color = "black")
    root.mainloop()

def screenshot_specified_region(left, top, width, height) :
    screenshot = pyautogui.screenshot(region = (left, top, width, height))
    screenshot.save("screenshot.png")
    return screenshot

def google_image_search() :
    file_path = "screenshot.png"
    search_url = 'https://yandex.com/images/search'
    files = {'upfile' : ('blob', open(file_path, 'rb'), 'image/jpeg')}
    params = {'rpt' : 'imageview', 'format' : 'json',
              'request' : '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
    response = requests.post(search_url, params = params, files = files)
    query_string = json.loads(response.content)['blocks'][0]['params']['url']
    img_search_url = search_url + '?' + query_string
    webbrowser.open(img_search_url, new = 0, autoraise = True)

def process_screenshot_image() :
    global window
    window.hide()  # Hide the Tkinter window before taking the screenshot
    region = (xPos, yPos, winWidth, winHeight)
    screenshot_specified_region(*region)
    google_image_search()
    window.show()  # Show the Tkinter window again after processing the screenshot

def main_thread() :
    try :
        while True :
            # Wait for a key press
            event = keyboard.read_event(suppress = True)
            print(event)
            # Check for Ctrl+Alt
            if keyboard.KEY_DOWN and event.name == 'alt' :
                process_screenshot_text()

            elif keyboard.KEY_DOWN and event.name == 'ctrl':
                process_screenshot_image()

    except Exception as e :
        print(f"An error occurred: {e}")

if __name__ == "__main__" :
    # Create and start the Tkinter thread
    tkinter_thread = threading.Thread(target = tkinter_thread)
    tkinter_thread.start()

    # Run the main thread for other code
    main_thread()
