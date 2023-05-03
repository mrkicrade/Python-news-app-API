import smtplib, ssl


def send_email(title, message):
    host = "smtp.gmail.com"
    port = 465

    username = "mrkic78@gmail.com"
    password = "YOUR_GMAIL_APP_PASSWORD"

    receiver = "mrkicrade@outlook.com"
    context = ssl.create_default_context()

    message =

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)