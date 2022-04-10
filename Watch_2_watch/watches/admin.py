from django.contrib import admin


from Watch_2_watch.watches.models import Watch


class WatchAdmin(admin.ModelAdmin):
    list_display = ['type', 'brand', 'production_year']
    list_filter = ['for_sale_status']


admin.site.register(Watch, WatchAdmin)

