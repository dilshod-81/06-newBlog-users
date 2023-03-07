from django.contrib import admin
from .models import Darsjadval, Izoh

class CommentInLine(admin.TabularInline):
    model = Izoh
    extra = 0

class DarsjadvalAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]

admin.site.register(Darsjadval, DarsjadvalAdmin)
admin.site.register(Izoh)

