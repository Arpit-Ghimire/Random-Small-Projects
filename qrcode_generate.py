import qrcode as qr

data = input("Enter URL or text to generate QR code: ")
filename = input("Enter file name (with .png): ")

img = qr.make(data)
img.save(filename)

print("QR code generated and saved successfully.")
