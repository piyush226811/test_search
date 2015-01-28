from django.contrib import admin

from .models import Player, Country, Blog


class PlayerAdmin(admin.ModelAdmin):
    model = Player
admin.site.register(Player, PlayerAdmin)


class CountryAdmin(admin.ModelAdmin):
    model = Country
admin.site.register(Country, CountryAdmin)


class BlogAdmin(admin.ModelAdmin):
    model = Blog
admin.site.register(Blog, BlogAdmin)
