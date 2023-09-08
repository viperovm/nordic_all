from django.contrib import admin
from .models import *
from .tasks import send_message


class UserListAdmin(admin.ModelAdmin):
    model = UserList
    list_display = ('name', 'last_name', 'test_user', 'email')
    list_display_links = ('name',)


class MailAdmin(admin.ModelAdmin):
    model = Mail
    list_display = ('subject', 'date', 'counter')
    list_display_links = ('subject',)
    readonly_fields = ('counter',)

    def save_model(self, request, obj, form, change):
        obj.counter = 0
        obj.save()
        send_message.delay(obj.id)


admin.site.register(UserList, UserListAdmin)
admin.site.register(Mail, MailAdmin)
