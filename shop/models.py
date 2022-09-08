from django.db import models
from django.contrib.auth.models import User



class Product(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    price=models.IntegerField()
    slug=models.SlugField()
    is_new=models.BooleanField(default=False)
    is_discounted=models.BooleanField(default=False)
    thumb=models.ImageField(default='default_product.png', null=True)
    brand=models.ForeignKey('Brand', default=None, on_delete=models.CASCADE)
    category=models.ForeignKey('Category', default=None, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    
    def sale_product_price(self):
        if self.is_discounted:
            return self.price * 0.8

    class Meta:
        db_table='shop_products'




class Brand(models.Model):
    name=models.CharField(max_length=200)
    icon=models.ImageField(upload_to='brands')

    def __str__(self):
        return self.name

    class Meta:
        db_table='shop_brands'




class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table='shop_categories'


    


class Slide(models.Model):
    image=models.ImageField(default='slide.jpg')






class CartItem(models.Model):
    customer=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField()

    def __str__(self):
        return self.product.title

    def total_price(self):
        return self.product.price * self.quantity




class Order(models.Model):
    address=models.CharField(max_length=300)
    phone=models.CharField(max_length=300) 
    total_price=models.IntegerField()
    customer=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Order # %s' % (str(self.id))





class OrderProduct(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_products')
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    amout=models.IntegerField()
    total=models.IntegerField()

    def __str__(self):
        return '%s x%s - %s' % (self.product, self.amout, self.order.customer.username)


