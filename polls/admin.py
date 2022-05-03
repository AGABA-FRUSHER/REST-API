from django.contrib import admin
import datetime
from django.utils import timezone

from .models import Question, Choice
# Register your models here.

#admin.site.register(Question)
class ChoiceInLIne(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    #fieldsets = [
        #(None,         {'fields': ['question_text']}),
        #('Date information', {'fields':['pub_date'], 'classes':['collapse']}),
    #]
    #inlines = [ChoiceInLIne]
    list_display = ('question_text', 'pub_date', 'was_published_recently')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)






#class QuestionAdmin(admin.ModelAdmin):
    #list_display = ('qn',)

    #def qn(self, obj):
        #future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
        #return obj.question_text

#admin.site.register(Question, QuestionAdmin)
