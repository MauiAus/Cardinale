from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
	item = models.CharField(max_length=50)
	price = models.IntegerField(default='0')
	quantity = models.IntegerField(default='0')
	model_pic = models.ImageField(upload_to = 'product_img', default = 'product_img/None/no-img.png')
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		abstract=True

	def __str__(self):
		return 'Item: {0} Price: {1}'.format(self.item, self.price)

class Beverage(Product):
	pass

class Snack(Product):
	pass

class Can(Product):
	pass