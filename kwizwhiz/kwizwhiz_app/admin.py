from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['selection']
admin.site.register(Category, CategoryAdmin)

class TopicAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Topic, TopicAdmin)

class QuizAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = ['answer_text', 'is_right']

admin.site.register(Quiz, QuizAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'quiz']
    inlines = [AnswerInlineModel]
admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_text', 'is_right', 'question']
admin.site.register(Answer, AnswerAdmin)

# Register your models here.
