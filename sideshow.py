from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title("Image Sideshow Viewer")

# list of image paths
image_paths = [
    r"https://res.cloudinary.com/dliruejpu/image/upload/v1779131263/WhatsApp_Image_2026-05-17_at_12.11.03_PM_voa2pd.jpg",
    r"https://res.cloudinary.com/dliruejpu/image/upload/v1779131262/WhatsApp_Image_2026-05-17_at_12.11.02_PM_1_ampyey.jpg",
    r"https://res.cloudinary.com/dliruejpu/image/upload/v1779131262/WhatsApp_Image_2026-05-17_at_11.45.32_AM_aa7b9e.jpg",
    r"https://res.cloudinary.com/dliruejpu/image/upload/v1779131261/WhatsApp_Image_2026-05-17_at_11.45.11_AM_qaqvtk.jpg"
    r"https://res.cloudinary.com/dliruejpu/image/upload/v1779131260/WhatsApp_Image_2026-05-13_at_12.40.58_PM_syu6l6.jpg"
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