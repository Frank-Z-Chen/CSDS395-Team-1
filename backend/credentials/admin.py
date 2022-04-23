from django.contrib import admin
from django.db.models.query import QuerySet
from django.db.models.functions import Length
from . import models
from string import ascii_lowercase

# Register your models here.

class user_name_filter(admin.SimpleListFilter):
    title = 'user name initial'
    parameter_name = 'user_name'
    
    def lookups(self, request, model_admin):
        result = []
        for letter in ascii_lowercase:  
            result.append(tuple([letter, letter]))

        return result

    def queryset(self, request, queryset:QuerySet):
        for letter in ascii_lowercase:
            if self.value() == letter:
                return queryset.filter(user_name__istartswith = letter)

class password_strongness_filterr(admin.SimpleListFilter):
    title = 'password strongness'
    parameter_name = 'pass_word'

    def lookups(self, request, model_admin):
        return [
            ('High', 'High'),
            ('Low', 'Low')
        ]

    def queryset(self, request, queryset:QuerySet):
        if self.value() == 'High':
            return queryset.annotate(text_length = Length('pass_word')).filter(text_length__gte = 10)
        elif self.value() == 'Low':
            return queryset.annotate(text_length = Length('pass_word')).filter(text_length__lt = 10)


@admin.register(models.login_credentials)
class credential_admin(admin.ModelAdmin):
    actions = ['reset_password']
    list_display = ['user_name', 'pass_word', 'password_strongness']
    list_editable = ['pass_word']
    list_per_page = 10
    list_filter = [user_name_filter, password_strongness_filterr]
    search_fields = ['user_name__istartswith']

    @admin.display(ordering='pass_word')
    def password_strongness(self, credential):
        if len(credential.pass_word) < 10:
            return 'Low'
        else:
            return 'High'

    @admin.action(description='set the selcted user password to default of 123123')
    def reset_password(self, request, queryset):
        updated_password = queryset.update(pass_word = '123123')
        self.message_user(
            request,
            f'{updated_password} we reset your password to 123123, hahahahaha!'
        )

