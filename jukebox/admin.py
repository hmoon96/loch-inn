from django.contrib import admin
from .models import Music_Embed, Global_List, Local_List


# Register your models here.
@admin.register(Music_Embed)
class Music_EmbedAdmin(admin.ModelAdmin):
    list_display = ('song_name', 'artist_name', 'album_name', 'published_date')
    search_fields = ('song_name', 'artist_name', 'album_name', 'published_date')
    list_filter = ('song_name', 'artist_name', 'album_name')
    ordering = ('song_name')


@admin.register(Global_List)
class Global_ListAdmin(admin.ModelAdmin):
    list_display = ('embed_id', 'user_id', 'datetime_added')
    search_fields = ('embed_id', 'user_id', 'datetime_added')
    list_filter = ('embed_id', 'user_id')
    ordering = ('datetime_added')


@admin.register(Local_List)
class Local_ListAdmin(admin.ModelAdmin):
    list_display = ('embed_id', 'user_id', 'datetime_added')
    search_fields = ('embed_id', 'user_id', 'datetime_added')
    list_filter = ('embed_id', 'user_id')
    ordering = ('datetime_added')

