from django.contrib import admin

# Register your models here.s
from .models import Customer, Category, Course
#admin.site.register(Course)
#admin.site.register(Category)
#admin.site.register(Customer)
#admin.site.register(Price)
#admin.site.register(Age)

class CustomerAdmin(admin.ModelAdmin):
    ...

admin.site.register(Customer, CustomerAdmin)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("category", "name", "kid_age", "price", "data_price", "image")
    list_filter = ("category", "name")




