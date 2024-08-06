import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from password import sixteen_letters

# Define your email details here
SENDER_EMAIL = 'makambientryx@gmail.com'
PASSWORD = sixteen_letters
RECIPIENTS = ['mactheegreat@gmail.com',
              'vacancies@flysafarilink.com',' jobs@astral-aviation.com',
              'careers@alternativeairlines.com','careers@airkenya.com',
              'careers@skywardexpress.co.ke','admin@eaaircharters.co.ke',
              'careers@phoenixaviation.co.ke','hr@jambojet.com',
              'info@jetwaysairlines.com','info@flydoc.org',
              'info@dragonflyafrica.co.ke','careers@flysafarilink.com',
              'alex@flysafarilink.com',
              'hr@astral-aviation.com'
             # 'hr@freedomairexpress.com'
              
              ]  # Add more recipients as needed
SUBJECT = 'Application for internship program'
MESSAGE = """Hope this email finds you well, 

I am writing to express my interest in joining your engineering maintenance department as an intern.
Below are my credentials with hope that you will be considerate of my request upon upcoming openings at your organization.
"""

# Define attachments
ATTACHMENTS = [
    {'filename': 'Makambi_Entrix_resume.docx', 'path': r'.\credentials\Makambi_Entrix_resume.docx'},
    {'filename': 'Cover letter.docx', 'path': r'.\credentials\Cover letter.docx'},
    {'filename': 'EASA clearance_letter.pdf', 'path': r'.\credentials\EASA clearance_letter.pdf'},
    {'filename': 'Good conduct certificate.pdf', 'path': r'.\credentials\Good conduct certificate.pdf'},
    {'filename': 'KCSE KNEC Cert.pdf', 'path': r'.\credentials\KCSE KNEC Cert.pdf'},
    {'filename': 'Recommendation letter.pdf', 'path': r'.\credentials\Recommendation letter.pdf'},
    {'filename': 'knec transcript.pdf', 'path': r'.\credentials\knec transcript.pdf'},
    {'filename': 'National id.pdf', 'path': r'.\credentials\National id.pdf'},
    {'filename': 'Fire-Training-Fire-Certificate.pdf', 'path': r'.\credentials\Fire-Training-Fire-Certificate.pdf'},
    {'filename': 'Protective-Equipment-Certificate.pdf', 'path': r'.\credentials\Protective-Equipment-Certificate.pdf'}
]  # Add more attachments as needed

def configure(smtp_obj, sender_email, password):
    ''' Configure the SMTP object and login '''
    smtp_obj.starttls()
    smtp_obj.login(sender_email, password)
    print("Login successful")

def add_attachments(msg):
    for attachment in ATTACHMENTS:
        try:
            with open(attachment['path'], "rb") as attach_file:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attach_file.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename={attachment['filename']}")
                msg.attach(part)
        except Exception as e:
            print(f"Failed to attach {attachment['filename']}: {e}")
    return msg

def send_email(smtp_obj, sender_email, recipient_email, subject, message):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))
    msg = add_attachments(msg)

    try:
        smtp_obj.sendmail(sender_email, recipient_email, msg.as_string())
        print(f'Email sent to {recipient_email}')
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")

def main():
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as smtp_obj:
            configure(smtp_obj, SENDER_EMAIL, PASSWORD)

            for recipient in RECIPIENTS:
                send_email(smtp_obj, SENDER_EMAIL, recipient, SUBJECT, MESSAGE)
    except Exception as e:
        print(f"Failed to configure SMTP server or send emails: {e}")

if __name__ == "__main__":
    main()
