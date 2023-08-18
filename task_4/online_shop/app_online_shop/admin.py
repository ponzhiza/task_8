from django.contrib import admin
from .models import OnlineShop

# Register your models here.
class OnlineShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'creation_time', 'update_time', 'auction']
    list_filter = ['auction', 'creation_time']
    actions = ['make_auction_as_false', 'make_auction_as_true']

    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description')
        }), 
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes':['collapse']
        })
    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)
    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

admin.site.register(OnlineShop, OnlineShopAdmin)