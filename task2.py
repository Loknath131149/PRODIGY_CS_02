import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


# Function to load an image via file dialog
def load_image_via_gui():
    file_path = filedialog.askopenfilename()  # Opens file dialog for selecting an image
    if file_path:
        img = Image.open(file_path)  # Open the image
        img.show()  # Display the original image
        return img
    return None


# Function to encrypt the image using XOR operation
def encrypt_image(img, key):
    encrypted_img = img.copy()  # Make a copy of the image
    pixels = encrypted_img.load()  # Access the pixel data
    width, height = img.size  # Get image size

    # Loop through each pixel and apply XOR operation to encrypt
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]  # Get the pixel values (RGB)
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)  # Apply XOR with key

    encrypted_img.show()  # Display the encrypted image
    return encrypted_img


# Function to decrypt the image (just apply XOR again with the same key)
def decrypt_image(img, key):
    return encrypt_image(img, key)  # Reuse the encrypt function for decryption


# Function to save an image to a file
def save_image(img, file_name):
    img.save(file_name)


# Function that handles the encryption and decryption process
def start_encryption():
    img = load_image_via_gui()  # Load the image via the GUI file dialog
    if img:
        key = 123  # Example key (you can change it)

        # Encrypt the image
        encrypted_img = encrypt_image(img, key)
        save_image(encrypted_img, 'encrypted_image.jpg')  # Save encrypted image

        # Decrypt the image
        decrypted_img = decrypt_image(encrypted_img, key)
        decrypted_img.show()  # Show the decrypted image
        save_image(decrypted_img, 'decrypted_image.jpg')  # Save decrypted image

        print("Encryption and Decryption complete. Images saved.")


# Main Tkinter GUI
if __name__ == "__main__":
    # Create a Tkinter window
    root = tk.Tk()
    root.title("Image Encryption Tool")

    # Add a button to start the encryption process
    load_btn = tk.Button(root, text="Select and Encrypt Image", command=start_encryption)
    load_btn.pack(pady=20)

    # Run the Tkinter event loop
    root.mainloop()
