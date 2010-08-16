from django.contrib import admin
from models import TestName

class TestNameAdmin(admin.ModelAdmin):
    model = TestName
    alphabet_filter = 'sorted_name'
    
    ## Testing a custom Default Alphabet
    #DEFAULT_ALPHABET = 'ABC'
    
    ## Testing a blank alphabet-- only shows the characters in the database
    #DEFAULT_ALPHABET = ''
    
    ## Testing a callable
    def DEFAULT_ALPHABET(self):
        return "I D K W"

admin.site.register(TestName, TestNameAdmin)