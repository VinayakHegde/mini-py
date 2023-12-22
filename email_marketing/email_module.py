import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def create_image_attachment(file_path, content_id):
    with open(file_path, "rb") as image_file:
        image = MIMEImage(image_file.read(), name=f"image-{content_id}")
        image.add_header("Content-ID", f"<{content_id}>")
        return image

def send_email(sender_email, sender_name, smtp_host, smtp_port, password, subject, html_content, recipients, attachments):
  try:
    message = MIMEMultipart()
    message['From'] = sender_name
    message['Subject'] = subject

    # Establish a connection to the SMTP server
    with smtplib.SMTP_SSL(smtp_host, smtp_port) as server:
        # Login to the email account
        server.login(sender_email, password)

        # Send emails to each recipient
        for recipient in recipients:
            recipient_email = recipient['email']
            message['To'] = recipient_email
            body = html_content.replace("{recipient}", recipient['name']).replace("{sender}", sender_name)
            message.attach(MIMEText(body, "html"))

            # Attach images to the message
            for attachment in attachments:
              message.attach(attachment)

            # Send the email
            server.sendmail(sender_email, recipient_email, message.as_string())
            print(f"Email sent to {recipient_email}")

        server.quit()
    print("All emails sent successfully!")
  
  except smtplib.SMTPAuthenticationError as e:
      print(f"SMTP Authentication Error: {e}")
