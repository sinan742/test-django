from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Employee

@receiver(post_save, sender=Employee)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        # 1. This will show in your terminal if the signal is working
        print(f"SIGNAL TRIGGERED: Sending email to {instance.name} at {instance.email}")
        
        subject = 'Welcome to the Team!'
        message = f'Hi {instance.name}, How are you!'
        recipient_list = [instance.email]
        
        try:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                recipient_list,
                fail_silently=False,
            )
            print("EMAIL STATUS: Sent Successfully!")
        except Exception as e:
            print(f"EMAIL STATUS: Failed! Error: {e}")