# Import the qrcode library
import qrcode

# Request user inputs
user_data = input("Enter text or URL to generate QR Code for: ").strip
user_filename = input("Provide a name for the file: ").strip

# Generate QR Code and its image
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(user_data)
image = qr.make_image(fill_color= 'black', back_color = 'white')
image.save(user_filename)
print(f"QRCode was saved as {user_filename}")