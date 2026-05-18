from itertools import cycle
from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk
import requests
from io import BytesIO

# list of image paths (fixed missing comma)
image_paths = [
    r"https://res.cloudinary.com/dliruejpu/image/upload/v1779131263/WhatsApp_Image_2026-05-17_at_12.11.03_PM_voa2pd.jpg",
    r"https://res.cloudinary.com/dliruejpu/image/upload/v1779131262/WhatsApp_Image_2026-05-17_at_12.11.02_PM_1_ampyey.jpg",
    r"https://res.cloudinary.com/dliruejpu/image/upload/v1779131262/WhatsApp_Image_2026-05-17_at_11.45.32_AM_aa7b9e.jpg",
    r"https://res.cloudinary.com/dliruejpu/image/upload/v1779131261/WhatsApp_Image_2026-05-17_at_11.45.11_AM_qaqvtk.jpg",
    r"https://res.cloudinary.com/dliruejpu/image/upload/v1779131260/WhatsApp_Image_2026-05-13_at_12.40.58_PM_syu6l6.jpg"
]

# resize the images to 1080x1080
image_size = (1080, 1080)

def load_image(path, size=image_size, timeout=15):
    if str(path).lower().startswith("http"):
        resp = requests.get(path, timeout=timeout)
        resp.raise_for_status()
        img = Image.open(BytesIO(resp.content))
    else:
        img = Image.open(path)
    return img.resize(size)

def build_gui():
    root = tk.Tk()
    root.title("Image Sideshow Viewer")

    # load PIL Images (may take a moment for remote downloads)
    pil_images = [load_image(p) for p in image_paths]

    # convert to PhotoImage after root exists
    photo_images = [ImageTk.PhotoImage(image) for image in pil_images]

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

    return root

if __name__ == '__main__':
    app = build_gui()
    app.mainloop()