from modules import env_loader, create_directory, csv_reader, generate_vcard, generate_qrcode, Configuration
from datetime import datetime

def main():
  env = env_loader()
  config = Configuration()
  outdir = env.get('CONTACT_OUTDIR', config.qr_img_outdir_default)
  create_directory(outdir)
  contacts = csv_reader(env['CONTACTS_CSV'])
  for contact in contacts:
    firstname = contact['firstname']
    lastname = contact['lastname']
    phone = contact['phone']
    email = contact['email']
    # Get the current date and time
    current_datetime = datetime.now().strftime(config.date_time_format)
  
    vcard_file = f"{outdir}/{firstname}_{lastname}-{current_datetime}.vcf"
    qrcode_file = f"{outdir}/{firstname}_{lastname}-{current_datetime}.png"

    generate_vcard(firstname, lastname, phone, email, vcard_file)
    generate_qrcode(vcard_file, qrcode_file)

if __name__ == "__main__":
  main()