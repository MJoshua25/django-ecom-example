from django.db import models
from core.models import Standard_model
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	stock = models.IntegerField()
	image = models.ImageField(upload_to='product_images/')

	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categorys"

	def __str__(self):
		pass


class Product(Standard_model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	stock = models.IntegerField()
	image = models.ImageField(upload_to='product_images/')
	is_on_promotion = models.BooleanField(default=False)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Product"
		verbose_name_plural = "Products"

	def __str__(self):
		pass


class Cart(Standard_model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	products = models.ManyToManyField(Product)
	total_price = models.DecimalField(max_digits=10, decimal_places=2)

	class Meta:
		verbose_name = "Cart"
		verbose_name_plural = "Carts"

	def __str__(self):
		pass


class Order(Standard_model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	products = models.ManyToManyField(Product)
	date = models.DateTimeField(auto_now_add=True)
	total_price = models.DecimalField(max_digits=10, decimal_places=2)
	# status = models.CharField(max_length=255, choices=ORDER_STATUS)

	class Meta:
		verbose_name = "Order"
		verbose_name_plural = "Orders"

	def __str__(self):
		pass
