import os
import csv
from dotenv import load_dotenv

def env_loader():
  # This line brings all environment variables from .env into os.environ
  load_dotenv()
  return os.environ

def create_directory(directory_path):
  # Create the directory if it doesn't exist
  os.makedirs(directory_path, exist_ok=True)
  if os.path.exists(directory_path):
    print(f"Directory '{directory_path}' created or already exists.")
  else:
    print(f"Failed to create directory '{directory_path}'.")


def csv_reader(file_path):
  try: 
    # Read recipient emails from CSV file
    with open(file_path, 'r') as csv_file:
      reader = csv.DictReader(csv_file)
      return [row for row in reader]
  except FileNotFoundError:
    print(f"CSV file not found: {file_path}")
    return []