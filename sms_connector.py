```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def connectSMS(user_credentials, message):
    # Extracting the user's email and password from the credentials
    email = user_credentials['email']
    password = user_credentials['password']

    # Setting up the server and port
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Logging in to the server
    server.login(email, password)

    # Creating the message
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = email
    msg['Subject'] = 'SMS Notification'
    msg.attach(MIMEText(message, 'plain'))

    # Sending the message
    server.send_message(msg)

    # Closing the server
    server.quit()
```