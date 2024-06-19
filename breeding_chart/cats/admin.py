from django.contrib import admin
from .models import Cat, Tomcat, Kitten, Color


class CatAdmin(admin.ModelAdmin):
    list_display = ("cats_name", "breeder_name", "color", "mothers_name", "fathers_name", "birth_date")

class TomcatAdmin(admin.ModelAdmin):
    list_display = ("cats_name", "breeder_name", "color","mothers_name", "fathers_name","birth_date")

class KittenAdmin(admin.ModelAdmin):
    list_display = ("cats_name", "breeder_name", "color","mothers_name", "fathers_name","birth_date")


admin.site.register(Cat, CatAdmin)
admin.site.register(Tomcat, TomcatAdmin)
admin.site.register(Kitten, KittenAdmin)
admin.site.register(Color)
