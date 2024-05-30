from django.db import models
from django.conf import settings
from django.templatetags.static import static

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/product', default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # How do I add same products faster?
    # quantity = models.IntegerField()
    is_selling = models.BooleanField(default=False)
    # How do I do this efficiently?
    # min_quantity = models.IntegerField(default=0)
    # max_quantity = models.IntegerField(default=0)
    expiration_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return static('images/product/default.jpg')