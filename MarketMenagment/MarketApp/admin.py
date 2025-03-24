from django.contrib import admin
from .models import Market,Proizvod,Kontakt,MarketProizvod,Vrabotena

class MarketProizvodInline(admin.TabularInline):
    model = MarketProizvod
    extra = 0

class MarketAdmin(admin.ModelAdmin):
    list_display = ("ime","kontakt")
    inlines = [MarketProizvodInline]
    exclude = ("user",)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(MarketAdmin, self).save_model(request, obj, form, change)


class VrabotenaAdmin(admin.ModelAdmin):
    list_display = ("ime","prezime")
    exclude = ("user",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(VrabotenaAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

class ProzivodAdmin(admin.ModelAdmin):
    list_display = ("ime","vid")

    list_filter = ('vid','domasen')


admin.site.register(Market,MarketAdmin)
admin.site.register(Kontakt)
admin.site.register(Vrabotena,VrabotenaAdmin)
admin.site.register(Proizvod,ProzivodAdmin)
