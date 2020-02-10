import os
import smtplib

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')


class MailHandler:

    def notify(email):
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            
            subject = email["subject"]
            body = email["body"]
            msg = f'Subject: {subject}\n\n{body}'
            
            smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)