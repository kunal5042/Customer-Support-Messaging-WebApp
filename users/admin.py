from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from .models import *
from django.utils.html import format_html, urlencode
from django.urls import reverse


# Register your models here.

class UrgencyFilter(SimpleListFilter):
    title = "Urgency Status"
    parameter_name = 'Urgency'

    def lookups(self, request, model_admin):
        return (
            ('LOW', 'Low'),
            ('MEDIUM', 'Medium'),
            ('HIGH', 'High')
        )

    def queryset(self, request, queryset):
        if self.value() == 'LOW':
            return queryset.filter(urgency_status='LOW')
        elif self.value() == 'MEDIUM':
            return queryset.filter(urgency_status='MEDIUM')
        elif self.value() == 'HIGH':
            return queryset.filter(urgency_status='HIGH')
    


@admin.register(UserQuery)
class UserQueryAdmin(admin.ModelAdmin):
    list_display = ('userID', 'timestamp', 'messageBody', 'urgency', 'resolved', 'action')
    ordering = ('urgency_status', '-timestamp',)
    list_per_page = 20
    search_fields = ['userID', 'messageBody', 'urgency_status']
    list_filter = [UrgencyFilter, 'resolved']
    
    def urgency(self, obj):
        return obj.urgency_status

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def action(self, obj):
        if obj.resolved == 'Open':
            obj.resolved = True
            return format_html(f'<a href="/user/userquery/{obj.id}/resolve">Resolve</a>')
        elif obj.resolved == 'Assigned':
            return format_html(f'<div><a href="/user/userquery/{obj.id}/resolve">Resolve</a></div><hr style="margin:5px 0"><div><a href="/user/userquery/{obj.id}/transfer">Transfer</a></div>')
        else:
            obj.resolved = False
            return format_html(f'<a href="/user/userquery/{obj.id}/unresolve">Unresolve</a>')



@admin.register(AgentResponse)
class AgentResponseAdmin(admin.ModelAdmin):
    list_display = ('agent_name', 'userID', 'ID_of_queries_resolved', 'query_response')
    list_filter = ['agent_name']

    def ID_of_queries_resolved(self, collection):
        list_of_urls = []

        for q in collection.queries_handled:
            url = reverse('admin:users_userquery_change', args={q})
            print(url)

            list_of_urls.append(format_html('<a href="{}">{}</a>', url, q))

        return format_html(' | '.join(list_of_urls))

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

