import tkinter as tk
from PIL import Image, ImageTk

# Function to create the image pyramid
def create_image_pyramid(root, image_path, levels=5):
    # Load the image
    img = Image.open(image_path)
    # Resize the image to a manageable size (e.g., 50x50 pixels)
    img = img.resize((50, 50), Image.Resampling.LANCZOS)  # Use Image.Resampling.LANCZOS instead of Image.ANTIALIAS
    photo = ImageTk.PhotoImage(img)

    # Place images in a pyramid shape
    for i in range(1, levels + 1):
        for j in range(i):
            # Calculate the x position to center the pyramid
            x_pos = (levels - i) * 25 + j * 50
            # Create and place a label with the image
            label = tk.Label(root, image=photo)
            label.image = photo  # Keep a reference to avoid garbage collection
            label.place(x=x_pos, y=i * 50)

# Create the main window
root = tk.Tk()
root.title("Image Pyramid")
root.geometry("400x300")

# Path to the image
image_path = "Data/Images/2.jpg"

# Create the image pyramid
create_image_pyramid(root, image_path, levels=5)

# Start the GUI event loop
root.mainloop()
