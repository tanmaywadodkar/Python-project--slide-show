from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title("Image Sideshow Viewer")

# list of image paths
image_paths = [
    r"C:\Users\tanma\Downloads\WhatsApp Image 2026-05-17 at 11.45.32 AM.jpeg",
    r"C:\Users\tanma\Downloads\WhatsApp Image 2026-05-17 at 11.45.11 AM.jpeg",
    r"C:\Users\tanma\Downloads\WhatsApp Image 2026-05-13 at 12.40.58 PM.jpeg",
    r"C:\Users\tanma\Downloads\WhatsApp Image 2026-05-17 at 11.44.31 AM.jpeg",
    r"C:\Users\tanma\Downloads\WhatsApp Image 2026-05-17 at 12.11.02 PM.jpeg",
    r"C:\Users\tanma\Downloads\WhatsApp Image 2026-05-17 at 12.11.03 PM.jpeg",
    r"C:\Users\tanma\Downloads\WhatsApp Image 2026-05-17 at 12.11.02 PM (1).jpeg"
]

# resize the images to 1080x1080
image_size = (1080, 1080)
images =[Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

image_cycle = cycle(photo_images)

def update_image():
    next_image = next(image_cycle)
    label.config(image=next_image)
    label.image = next_image
    root.after(1500, update_image)

def start_slideshow():
    update_image()
    play_button.config(state=tk.DISABLED)

play_button = tk.Button(root, text="Start Slideshow", command=start_slideshow)
play_button.pack()

root.mainloop() 