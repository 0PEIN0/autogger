from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'email',
                    'first_name',
                    'last_name',)
    search_fields = ('id',
                     'email',
                     'first_name',
                     'last_name',)
    readonly_fields = ('id',)

    def save_model(self,
                   request,
                   obj,
                   form,
                   change):
        if 'password' in form.changed_data:
            obj.set_password(obj.password)
        obj.save()
