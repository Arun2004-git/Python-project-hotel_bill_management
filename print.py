from PIL import ImageGrab
from tkinter import messagebox

def save_frame_as_image(frame, filename="frame_capture.png"):
    """
    Captures and saves the entire contents of a specified Tkinter frame as an image.

    Parameters:
    - frame: The Tkinter Frame widget to capture.
    - filename: The name of the file to save the image as (default: "frame_capture.png").
    """
    # Ensure the layout is up-to-date before capturing
    frame.update_idletasks()

    # Get the root coordinates and the exact size of the frame
    #x = frame.winfo_rootx()
    # y = frame.winfo_rooty()
    x=1295
    y=110
   
    width = x + 500  # Explicit width of the frame
    height = y + 750  # Explicit height of the frame

    # Adding a small buffer if needed to make sure edges are included
    buffer = 5
    frame_image = ImageGrab.grab(bbox=(x - buffer, y - buffer, width + buffer, height + buffer))
    
    # Save the captured image
    frame_image.save(filename)
    messagebox.showinfo("Success", f"'{filename}' saved successfully.")
