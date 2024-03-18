from django.contrib import admin
from home.models import *

# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname','username','phone','email','password','testattempted','points']

class QuestionsAdmin(admin.ModelAdmin):
    list_display=['qid','ans']
admin.site.register(Users,UsersAdmin)
admin.site.register(Questions,QuestionsAdmin)
admin.site.register(Result)
