import vobject

def generate_vcard(firstname, lastname, phone, email, vcard_file):
  # Create a vCard
  vcard = vobject.vCard()
  vcard.add('fn').value = firstname
  vcard.add('ln').value = lastname
  vcard.add('tel').value = phone
  vcard.add('email').value = email

  # Save vCard to a file
  with open(vcard_file, 'w') as file:
    file.write(vcard.serialize())

