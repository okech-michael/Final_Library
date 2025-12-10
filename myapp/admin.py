# Register your models here.
from django.contrib import admin
from .models import UserProfile, Book, Cart, Subscription


# Optional: Make admin pages look nicer
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at')
    search_fields = ('title', 'author', 'category')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'is_subscribed')
    search_fields = ('user__username', 'phone')


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'added_at')
    search_fields = ('user__username', 'book__title')


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'transaction_id', 'is_successful', 'date')
    search_fields = ('user__username', 'transaction_id')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Subscription, SubscriptionAdmin)

