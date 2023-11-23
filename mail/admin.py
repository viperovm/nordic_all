from django.contrib import admin
from django.db.models import Subquery, OuterRef, PositiveIntegerField
from .models import *
from .tasks import send_message


class SubqueryCount(Subquery):
    template = "(SELECT count(*) FROM (%(subquery)s) _count)"
    output_field = PositiveIntegerField()


class UserListAdmin(admin.ModelAdmin):
    model = UserList
    list_display = ('name', 'last_name', 'test_user', 'email')
    list_display_links = ('name',)


# class MailAdmin(admin.ModelAdmin):
#     model = Mail
#     list_display = ('subject', 'date', 'counter')
#     list_display_links = ('subject',)
#     readonly_fields = ('counter',)
#
#     def save_model(self, request, obj, form, change):
#         obj.counter = 0
#         obj.save()
#         send_message.delay(obj.id)


class MailAdmin(admin.ModelAdmin):
    model = Mail
    list_display = ('subject', 'date', 'get_sended_mails_count')
    list_display_links = ('subject',)
    readonly_fields = ('get_sended_mails_count',)

    def save_model(self, request, obj, form, change):
        obj.save()
        send_message.delay(obj.id)

    def get_queryset(self, request):
        mails_count = Subquery(UserList.objects.filter(mailings=OuterRef('pk')))
        queryset = Mail.objects.annotate(sended_mails_count=SubqueryCount(mails_count)).all()
        return queryset

    @admin.display(description='Писем отправлено')
    def get_sended_mails_count(self, obj):
        return obj.sended_mails_count


admin.site.register(UserList, UserListAdmin)
admin.site.register(Mail, MailAdmin)
