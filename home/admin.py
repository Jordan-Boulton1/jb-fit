from django.contrib import admin
from home.models import Newsletter

# Register your models here.
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    list_filter = ('created_at',)
    search_fields = ('email',)

    def subscribed_at(self, obj):
        return obj.created_at
    subscribed_at.admin_order_field = 'created_at'  # Allows column sorting
    subscribed_at.short_description = 'Subscribed At'  # Renames the column header in the admin

admin.site.register(Newsletter, NewsletterAdmin)
