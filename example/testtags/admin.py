from django.contrib import admin
from models import TestName

class TestNameAdmin(admin.ModelAdmin):
    model = TestName
    alphabet_filter = 'sorted_name'

admin.site.register(TestName, TestNameAdmin)