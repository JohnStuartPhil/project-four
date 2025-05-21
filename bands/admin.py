from django.contrib import admin
from .models import Band, Opinion
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Band)
class BandAdmin(SummernoteModelAdmin):

    list_display = ('band_name', 'slug', 'status')
    search_fields = ['band_name', 'review']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('band_name',)}
    summernote_fields = ('review',)


admin.site.register(Opinion)
