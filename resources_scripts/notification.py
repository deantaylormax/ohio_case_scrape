import smtplib

def send_sms_via_email(recipient_number, carrier_gateway, message):
    sender_email = "deantaylor1793@gmail.com"
    sender_password = "!dt27664"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, f"{recipient_number}@{carrier_gateway}", message)

# Example usage
send_sms_via_email("2163742566", "tmomail.net", "testing_text")
