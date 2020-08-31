from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
from nested_inline.admin import NestedModelAdmin, NestedTabularInline

# Register your models here.
class QuestionInline(NestedTabularInline):
	model = Question
	# list_display = ('election', 'name')


class StoryAdmin(NestedModelAdmin):
	inlines = [QuestionInline]
	# prepopulated_fields = {'slug' : ('name', )}
	# list_display = ('name', 'start_date', 'end_date')



admin.site.register(Story, StoryAdmin)
admin.site.unregister(Group)