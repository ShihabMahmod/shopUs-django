from django.db import models
from base.models import BaseModel
from django.utils.text import slugify


class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True , null=True , blank=True)
    category_image = models.ImageField(upload_to="catgories")


    def save(self , *args , **kwargs):
        self.slug = slugify(self.category_name)
        super(Category ,self).save(*args , **kwargs)


    def __str__(self) -> str:
        return self.category_name
    
 
class Brand(BaseModel):
    brand_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True , null=True , blank=True)
    brand_image = models.ImageField(upload_to="brands")


    def save(self , *args , **kwargs):
        self.slug = slugify(self.brand_name)
        super(Brand ,self).save(*args , **kwargs)


    def __str__(self) -> str:
        return self.brand_name        


class ColorVariant(BaseModel):
    color_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.color_name

class SizeVariant(BaseModel):
    size_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.size_name




class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True  , null=True , blank=True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , related_name="products")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="products", default=1)
    price = models.IntegerField()
    product_desription = models.TextField()
    color_variant = models.ManyToManyField(ColorVariant , blank=True)
    size_variant = models.ManyToManyField(SizeVariant , blank=True)

    def save(self , *args , **kwargs):
        self.slug = slugify(self.product_name)
        super(Product ,self).save(*args , **kwargs)


    def __str__(self) -> str:
        return self.product_name

class ProductImage(BaseModel):
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name="product_images")
    image =  models.ImageField(upload_to="product")