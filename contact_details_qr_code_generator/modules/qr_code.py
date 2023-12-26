import qrcode
from .app_config import Configuration

def generate_qrcode(vcard_file, qrcode_file):
  # Read vCard data from file
  with open(vcard_file, 'r') as file:
    vcard_data = file.read()

  config = Configuration()
  # Generate QR code from vCard data
  qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=config.qr_img_box_size, border=config.qr_img_border)
  qr.add_data(vcard_data)
  qr.make(fit=True)

  # Create an image from the QR code
  qr_img = qr.make_image(fill_color=config.qr_img_fill_color, back_color=config.qr_img_back_color)

  # Save the QR code image
  qr_img.save(qrcode_file)
  print(f"QR code saved to: {qrcode_file}")

