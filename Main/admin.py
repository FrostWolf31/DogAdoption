from django.contrib import admin
from .models import Dog


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
	list_display = ('name', 'age_text', 'gender', 'is_available', 'order')
	list_editable = ('is_available', 'order')
	search_fields = ('name', 'description', 'age_text')
	list_filter = ('is_available', 'gender')
