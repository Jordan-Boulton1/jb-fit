from django.contrib import admin
from home.models import Newsletter

# Register your models here.


class NewsletterAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Newsletter model.
    """
    # Display these fields in the admin list view
    list_display = ('email', 'subscribed_at')

    # Add filter options in the admin list view for these fields
    list_filter = ('created_at',)

    # Enable search functionality for these fields in the admin
    search_fields = ('email',)

    def subscribed_at(self, obj):
        """
        Returns the creation date of the subscription as 'Subscribed At'.

        :param obj: Newsletter instance
        :return: DateTime of when the subscription was created
        """
        return obj.created_at

    # Allows sorting of the 'Subscribed At' column
    subscribed_at.admin_order_field = 'created_at'

    # Renames the column header to 'Subscribed At' in the admin
    subscribed_at.short_description = 'Subscribed At'


# Register the Newsletter model with the custom admin configuration
admin.site.register(Newsletter, NewsletterAdmin)
