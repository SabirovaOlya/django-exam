import os
from celery import shared_task, Celery
from django.core.mail import send_mail
from dotenv import load_dotenv


load_dotenv('.env')
HOST_EMAIL = os.getenv('HOST_EMAIL')


@shared_task
def send_notification_mail(target_mail, message):
    mail_subject = "Welcome to my site)))"
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=HOST_EMAIL,
        recipient_list=[target_mail],
        fail_silently=False,
    )
    return "Email sent!"
