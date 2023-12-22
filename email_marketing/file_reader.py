import csv
import os
import json
from dotenv import load_dotenv
from email_module import create_image_attachment

def csv_reader(file_path):
  # Read recipient emails from CSV file
  with open(file_path, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    return [row for row in reader]
  
def html_reader(file_path):
  # Open the HTML file in read mode ('r')
  with open(file_path, 'r', encoding='utf-8') as html_file:
    # Read the content of the file
    return html_file.read()

def json_reader(file_path):
  # Read JSON data from the file
  with open(file_path, 'r') as config_file:
    return json.load(config_file)
  
def attachments_reader(img_dir, html_content):
  # Collect all the images
  image_files = [f for f in os.listdir(img_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

  # Attach images to the message
  attachments = [
    create_image_attachment(os.path.join(img_dir, image_file), f"image-{i}")
    for i, image_file in enumerate(image_files, start=1)
  ]

  # Update html_content with image content IDs
  for i, image_file in enumerate(image_files, start=1):
    html_content = html_content.replace(f"images/{image_file}", f"cid:image-{i}")

  return attachments, html_content

def env_loader():
  # This line brings all environment variables from .env into os.environ
  load_dotenv()
  return os.environ