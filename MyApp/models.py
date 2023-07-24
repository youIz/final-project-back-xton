from django.db import models
from .models import *
from django.urls import reverse
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
# MODELS USER___________________________________________________________
class Role(models.Model):
    role = models.CharField(max_length=50, default=3)
    def __str__(self):
        return self.role

class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, default=4)
    img_url = models.CharField(max_length=500)
    newsletter = models.BooleanField(default=False)
    country = models.CharField(max_length=80, null=True)
    company = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=150, null=True)
    city = models.CharField(max_length=60, null=True)
    state = models.CharField(max_length=60, null=True)
    postcode = models.CharField(max_length=6, null=True)
    phone = models.CharField(max_length=25, null=True)

# Crée model newsletter pour pouvoir créer un form avec email
class Newsletter(models.Model):
    email = models.EmailField()





# MODELS BLOG____________________________________________________________
class CategoryArticle(models.Model):
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.category

class Tag(models.Model):
    tag = models.CharField(max_length=100)
    def __str__(self):
        return self.tag

class Article(models.Model):
    title = models.CharField(max_length=100)
    img = models.CharField(max_length=1000)
    description = models.TextField()
    category = models.ForeignKey(CategoryArticle, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    validate = models.BooleanField(default=False)
    creation = models.DateField(default=timezone.now)
    update = models.DateField(auto_now=True)
    view = models.IntegerField(default=0)    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('detail_article', args=[str(self.id)])
    def get_comment_count(self):
        return self.note2_set.count()

class Note2(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    anonymous_author = models.ForeignKey('AnonymousUser2', null=True, blank=True, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    titre = models.CharField(max_length=50)
    text = models.TextField(max_length=300, default='valeur_par_défaut')
    created_at = models.DateTimeField(default=timezone.now)

class AnonymousUser2(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()




# MODELS CONTACT________________________________________________________________
class Contact(models.Model):
    tel = models.CharField(max_length=20)
    adresse = models.CharField(max_length=200)
    email = models.EmailField()
    fax = models.CharField(max_length=20)

    def __str__(self):
        return self.email
    
class Contact_mail(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)
    
    def toggle_read(self):
        self.read = not self.read
        self.save()

class Reply(models.Model):
    to = models.ForeignKey(Contact, on_delete=models.CASCADE)
    content = models.TextField()


# MODELS PRODUCT__________________________________________________________________
class Category(models.Model):
    value = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.value

class AnonymousUser(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

class Product(models.Model):
    img1 = models.CharField(max_length=1000)
    img2 = models.CharField(max_length=1000)
    img3 = models.CharField(max_length=1000)
    description = models.TextField(max_length=300, null=True, blank=True)
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    price = models.PositiveIntegerField()
    promo = models.PositiveIntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    stock = models.IntegerField(default=0)
    wish = models.BooleanField(default=False)
    
    def get_stock(self):
        return self.stock
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')
    
    def __str__(self):
        return f"Cart for {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=2, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    def restore_stock(self):
        self.product.stock += self.quantity
        self.product.save()

class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    country = models.CharField(max_length=80)
    company = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    postcode = models.CharField(max_length=6)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    # promo = models.CharField(max_length=10)
    validate = models.BooleanField(default=False)
    def __str__(self):
        return f"Order of {self.cart.user.username} for {self.cart}."

class Note(models.Model):
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    anonymous_author = models.ForeignKey('AnonymousUser', null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    titre = models.CharField(max_length=50, blank=True)
    text = models.TextField(max_length=300, default='valeur_par_défaut')




