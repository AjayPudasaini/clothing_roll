from django.db import models

# Create your models here.
class Category(models.Model):
    image = models.ImageField(upload_to="category/images")
    name = models.CharField(max_length=200, blank=False, null=True)
    desc = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    @property
    def ImageUrl(self):
        try:
            url = self.image.url
        except:
            url=""
        return url


class Brand(models.Model):
    brand_image = models.ImageField(upload_to="brand/images")
    brand_name = models.CharField(max_length=200, blank=False, null=False)
    brand_desc = models.TextField()
    brand_slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.brand_name


    @property
    def BrandImageUrl(self):
        try:
            url = self.brand_image.url
        except:
            url=""
        return url



class Product(models.Model):
    slug = models.SlugField(unique=True)
    product_name = models.CharField(max_length=500)
    product_desc = models.TextField()
    product_image = models.ImageField(upload_to="product/images")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    display_price = models.FloatField()
    actual_price = models.FloatField()



    def __str__(self):
        return self.product_name

    @property
    def ProductImageUrl(self):
        try:
            url = self.product_image.url
        except:
            url=""
        return url




