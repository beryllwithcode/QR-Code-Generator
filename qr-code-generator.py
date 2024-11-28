import pyqrcode
from pyqrcode import QRCode

# String which represent the QR code

s = "https://www.linkedin.com/in/beryll-pradana-ramadhan-58044a212/"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
url.png('myQRCode.png', scale=6)