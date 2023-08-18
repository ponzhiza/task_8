from django.db import models
from django.contrib import admin
from django.utils.html import format_html

# Create your models here.

class OnlineShop(models.Model):
    # def __str__(self): 
    #     return f'<Onlineshop: Onlineshop(id={self.id}, title={self.title}, price={self.price})>'

    id = models.CharField('id', max_length=10, primary_key=True)

    title = models.CharField('Заголовок', max_length=128)

    description = models.TextField('Описание')

    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    auction = models.BooleanField('Торг', help_text='Отметьте, уместен ли торг')

    creation_time = models.DateTimeField(auto_now_add=True)

    update_time = models.DateTimeField(auto_now=True)

    @admin.display(description='дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.creation_time.date() == timezone.now().date():
            created_time = self.creation_time.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: red; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.creation_time.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='дата последнего обновления')
    def updated_date(self):
        from django.utils import timezone
        if self.update_time.date() == timezone.now().date():
            created_time = self.update_time.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: red; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.update_time.strftime("%d.%m.%Y в %H:%M:%S")

    def __str__(self):
        return f'Onlineshop(id={self.id}, title={self.title}, price={self.price})'

    class Meta: 
        db_table = 'online_shop'


    