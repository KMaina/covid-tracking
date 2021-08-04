# type:ignore
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(username,email):
    subject = 'Welcome to Covid19 Tracker'
    sender = 'contechkenya7@gmail.com'

    text_content = render_to_string('email/welcome.txt',{"username":username})
    html_content = render_to_string('email/welcome.html',{"username":username})

    msg = EmailMultiAlternatives(subject,text_content,sender,[email])
    msg.attach_alternative(html_content,'text/html')
    msg.send()