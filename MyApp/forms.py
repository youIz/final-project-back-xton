from django import forms
from .models import *

# FORMS BLOG_____________________________________________
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'img', 'description', 'category']

class ArticleCategorieForm(forms.ModelForm):
    class Meta:
        model = CategoryArticle
        fields = '__all__'

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'




# FORMS CONNEXION______________________________________________________
class UserFormRole(forms.ModelForm):
    class Meta:
        model = User
        fields = ['role']
        
class UserFormAll(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username',  'email', "newsletter"]
        exclude = ['role', ] 




# FORMS CONTACT_______________________________________________________
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']




# FORMS PRODUCT_______________________________________________________
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ProductStockForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['stock']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'