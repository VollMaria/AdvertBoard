from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Response
from .views import response_good


@receiver(post_save, sender=response_good)
def response_accepted(instance, created, **kwargs):
    if not created:
        return

    emails = instance.response.author.email
    subject = f'Ваш отклик принят!'
    text_content = (
        f'Объявление: {instance.advertisement.title}\n'
        f'Отклик: {instance.text}\n'
    )

    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.send()

