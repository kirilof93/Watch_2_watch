from django.db import models
from Watch_2_watch.accounts.models import UserProfile


class Watch(models.Model):
    TYPE_CHOICE_DIVER = 'diver'
    TYPE_CHOICE_DRESS = 'dress'
    TYPE_CHOICE_SPORT = 'sport'
    TYPE_CHOICE_PILOT = 'pilot'
    TYPE_CHOICE_MECHANICAL = 'mechanical'
    TYPE_CHOICE_QUARTZ = 'quartz'

    TYPE_CHOICES = (
        (TYPE_CHOICE_DIVER, 'Diver'),
        (TYPE_CHOICE_DRESS, 'Dress'),
        (TYPE_CHOICE_SPORT, 'Sport'),
        (TYPE_CHOICE_PILOT, 'Pilot'),
        (TYPE_CHOICE_MECHANICAL, 'Mechanical'),
        (TYPE_CHOICE_QUARTZ, 'Quartz'),
    )

    type = models.CharField(
        max_length=15,
        choices=TYPE_CHOICES,
    )

    brand = models.CharField(max_length=40)
    production_year = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(
        upload_to='watches',
    )
    for_sale_status = models.BooleanField(default=False)

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}; {self.brand}; {self.type}'


class Comment(models.Model):
    watch = models.ForeignKey(Watch, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
