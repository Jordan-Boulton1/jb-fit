from django.contrib import admin
from contact.models import ContactSubmission
# Register your models here.

class ContactSubmissionAdmin(admin.ModelAdmin):
    """
    Admin configuration for the
    Contact submission model.
    """
    # Display these fields in the admin list view
    list_display = ('email', 'message', 'submitted_at')

    # Add filter options in the admin list view for these fields
    list_filter = ('submitted_at',)

    # Enable search functionality for these fields in the admin
    search_fields = ('email',)

    def submitted_at(self, obj):
        """
        Returns the submitted date of the message as 'Submitted At'.

        :param obj: ContactSubmission instance
        :return: DateTime of when the subscription was created
        """
        return obj.submitted_at
    
    # Allows sorting of the 'Submitted At' column
    submitted_at.admin_order_field = 'submitted_at'

    # Renames the column header to 'Subscribed At' in the admin
    submitted_at.short_description = 'Submitted At'

admin.site.register(ContactSubmission, ContactSubmissionAdmin)