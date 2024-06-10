from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    tel = models.CharField(max_length=15)
    msg = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія курсу", null=True)
    name = models.CharField(max_length=100)
    kid_age = models.IntegerField(help_text="Вік учня", verbose_name="Вік учня", null=True)
    price = models.IntegerField(help_text="Вкажіть вартість", null=True, verbose_name='Вартість')
    data_price = models.IntegerField(verbose_name='Дата')
    image = models.ImageField(verbose_name='Картинка', upload_to = "images_courses")
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reversed('couse-detail', args = [str(self.id)])
    
    

 

#m1 = Customer.objects.create(name="Oleg", email="olegos@gmail.com", tel="+389066505672", msg="Hello!")







































#        |          -----------------
#        |          |
#        |          |
#        |          |
#        |          |
#        -----------|------------|
#                   |            |
#                   |            |
#                   |            |
#                   |            |
#        ------------