from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Advertisement(models.Model):
    GUILD = (
        ('tanks', 'Танки'),
        ('healers', 'Хилы'),
        ('damagers', 'ДД'),
        ('traders', 'Торговцы'),
        ('guildmasters', 'Гилдмастеры'),
        ('questgivers', 'Квестгиверы'),
        ('blacksmiths', 'Кузнецы'),
        ('tanners', 'Кожевники'),
        ('potions', 'Зельевары'),
        ('spellmasters', 'Мастера заклинаний'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    content = models.TextField()
    category = models.CharField(max_length=16, choices=GUILD, default='tanks')
    date = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(upload_to='uploads/', blank=True, null=False)

    def __str__(self):
        return f'{self.title}: {self.category[:16]}'

    def get_absolute_url(self):
        return reverse('adv_detail', args=[str(self.pk)])


class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('adv_detail', args=[str(self.pk)])
