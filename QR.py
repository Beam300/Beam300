# Generate QR Code
# import pyqrCode
# import  png
from PIL import image 
link = input("Enter anython to generate QR :  ")
qr_code = pyqrCode.create(link)
qr_code.png ("QRCode.png", scale=5)
image.open("QRCode.png")