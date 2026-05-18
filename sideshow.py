from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk
import requests
from io import BytesIO

# ----------------------------- #
# IMAGE URLS
# ----------------------------- #

image_paths = [
    "https://res.cloudinary.com/dliruejpu/image/upload/v1779135975/pexels-sevde-sen-48864333-16767121_roeyt8.jpg",
    "https://res.cloudinary.com/dliruejpu/image/upload/v1779135972/pexels-osviel91-32162196_gy5moc.jpg",
    "https://res.cloudinary.com/dliruejpu/image/upload/v1779135922/pexels-juan-diavanera-2150627805-32211894_e79s24.jpg",
    "https://res.cloudinary.com/dliruejpu/image/upload/v1779135908/pexels-sb42-4022697_bkzyy9.jpg",
    "https://res.cloudinary.com/dliruejpu/image/upload/v1779135885/pexels-musstashy-35445399_t5ivfq.jpg",
    "https://res.cloudinary.com/dliruejpu/image/upload/v1779135982/pexels-pit0chka-9854061_s5kcje.jpg"
]

# ----------------------------- #
# SETTINGS
# ----------------------------- #

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

IMAGE_SIZE = (1000, 600)

SLIDESHOW_DELAY = 2500
FADE_STEPS = 12
FADE_DELAY = 50

# ----------------------------- #
# LOAD IMAGE FUNCTION
# ----------------------------- #

def load_image(path, size=IMAGE_SIZE, timeout=15):
    """
    Loads image from URL or local path
    and resizes it.
    """

    if path.lower().startswith("http"):
        response = requests.get(path, timeout=timeout)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
    else:
        img = Image.open(path)

    return img.resize(size)


# ----------------------------- #
# MAIN GUI FUNCTION
# ----------------------------- #

def build_gui():

    root = tk.Tk()

    root.title("✨ Premium Image Slideshow Viewer")
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    root.configure(bg="#0f172a")

    # ----------------------------- #
    # TITLE
    # ----------------------------- #

    title = tk.Label(
        root,
        text="✨ IMAGE SLIDESHOW APP ✨",
        font=("Poppins", 24, "bold"),
        bg="#0f172a",
        fg="white"
    )

    title.pack(pady=15)

    # ----------------------------- #
    # IMAGE FRAME
    # ----------------------------- #

    image_frame = tk.Frame(
        root,
        bg="#1e293b",
        bd=5,
        relief="ridge"
    )

    image_frame.pack(pady=10)

    # ----------------------------- #
    # LOAD IMAGES
    # ----------------------------- #

    pil_images = [load_image(path) for path in image_paths]

    label = tk.Label(
        image_frame,
        bg="#1e293b"
    )

    label.pack()

    image_cycle = cycle(pil_images)

    current_image = [next(image_cycle)]

    # Display first image
    first_photo = ImageTk.PhotoImage(current_image[0])
    label.config(image=first_photo)
    label.image = first_photo

    # ----------------------------- #
    # FADE TRANSITION FUNCTION
    # ----------------------------- #

    def fade_to_next():

        next_pil_image = next(image_cycle)

        for alpha in range(0, FADE_STEPS + 1):

            blended = Image.blend(
                current_image[0],
                next_pil_image,
                alpha / FADE_STEPS
            )

            photo = ImageTk.PhotoImage(blended)

            label.config(image=photo)
            label.image = photo

            root.update()
            root.after(FADE_DELAY)

        current_image[0] = next_pil_image

        root.after(SLIDESHOW_DELAY, fade_to_next)

    # ----------------------------- #
    # START BUTTON
    # ----------------------------- #

    def start_slideshow():

        start_button.config(
            text="Slideshow Running...",
            bg="#16a34a",
            fg="white",
            state=tk.DISABLED
        )

        fade_to_next()

    # Hover Effects
    def on_enter(e):
        start_button.config(
            bg="#38bdf8",
            fg="black"
        )

    def on_leave(e):
        start_button.config(
            bg="#2563eb",
            fg="white"
        )

    start_button = tk.Button(
        root,
        text="▶ Start Slideshow",
        font=("Poppins", 16, "bold"),
        bg="#2563eb",
        fg="white",
        activebackground="#38bdf8",
        activeforeground="black",
        padx=25,
        pady=12,
        bd=0,
        relief="flat",
        cursor="hand2",
        command=start_slideshow
    )

    start_button.pack(pady=25)

    start_button.bind("<Enter>", on_enter)
    start_button.bind("<Leave>", on_leave)

    # ----------------------------- #
    # FOOTER
    # ----------------------------- #

    footer = tk.Label(
        root,
        text="Developed using Python, Tkinter & Pillow",
        font=("Arial", 10),
        bg="#0f172a",
        fg="#94a3b8"
    )

    footer.pack(side="bottom", pady=10)

    return root


# ----------------------------- #
# MAIN PROGRAM
# ----------------------------- #

if __name__ == "__main__":

    app = build_gui()
    app.mainloop()