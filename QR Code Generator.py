import qrcode
import os

data = input("Type the link or the text you want: ")
img_name = input("Name the QR code: ")
path = input("Choose the path: ")

# Validate and sanitize the inputs if needed

img = qrcode.make(data)
img_path = os.path.join(path, f"{img_name}.png")

try:
    img.save(img_path)
    print("QR code saved at:", img_path)
except Exception as e:
    print("Error saving QR code:", e)
