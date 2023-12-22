from email_module import send_email
from file_reader import csv_reader, html_reader, json_reader, attachments_reader, env_loader

try:
    config = json_reader('app.config.json')
    template_dir = config['templateDir']
    [attachments, html_content] = attachments_reader(f"{template_dir}/images", html_reader(f"{template_dir}/index.html"))
    recipients = csv_reader(config['recipientsCSV'])
    env = env_loader()
    send_email(
        env['SENDER_EMAIL'], 
        env['SENDER_NAME'], 
        env['SENDER_SMTP_HOST'], 
        env['SENDER_SMTP_PORT'],
        env['SENDER_PASSWORD'], 
        config['subject'], 
        html_content, 
        recipients, 
        attachments
        )

except Exception as e:
    print(f"An error occurred: {e}")
