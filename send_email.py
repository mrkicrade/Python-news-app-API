import smtplib, ssl


def send_email(message):
    # print(message)
    host = "smtp.gmail.com"
    port = 465

    username = "mrkic78@gmail.com"
    password = "aczcvczgcgdklnzy"

    receiver = "mrkic78@gmail.com"
    context = ssl.create_default_context()
    #
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
