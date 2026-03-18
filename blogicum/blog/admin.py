from django.contrib import admin

from .models import Category, Location, Post, Comment

admin.site.register(Category)
admin.site.register(Location)
#admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'category',
        'location',
        'pub_date',
        'is_published',
        'created_at',
    )
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published', 'pub_date')
    search_fields = ('title', 'text', 'author__username')
    date_hierarchy = 'pub_date'
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'text', 'author', 'category', 'location', 'image')
        }),
        ('Даты', {
            'fields': ('pub_date', 'created_at'),
        }),
        ('Публикация', {
            'fields': ('is_published',),
        }),
    )
    
    readonly_fields = ('created_at',)

admin.site.register(Comment)