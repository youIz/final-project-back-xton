"""
URL configuration for xton project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from MyApp.views import *
from MyApp.views import *
from MyApp.views import *
from MyApp.views import *
from MyApp.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('product/', product, name='product'),
    path('blog/', blog, name='blog'),
    path('contact/', contact_mail, name='contact'),
    path('checkout/', checkout, name='checkout'),
    path('login/', connexion, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', deconnexion),
    path('cart/', cart, name='cart'),
    path('cart/item/delete/<int:item_id>/', cart_item_delete, name='cart_item_delete'),

    path('products/<int:category_id>/', product, name='product_category'), 
    path('product/<int:id>', readProduct, name='detail_Product'),
    path('product/edit/<int:id>', updateProduct),
    path('product/stock/edit/<int:id>', updateStockProduct),
    path('product/destroy/<int:id>', destroy_Product),
    path('contact_mail/destroy/<int:id>', destroyContact_mail),
    
    
    
    path('comment/create/<int:id>/', comment_create, name='comment_create'),
    path('create/product/', createProduct, name='create_Product'),    
    
    
    path('article/<int:id>', readArticle, name='detail_article'),
    path('comment/create2/<int:id>/', comment_create2, name='comment_create2'),
    path('article/edit/<int:id>', updateArticle),
    path('article/destroy/<int:id>', destroy_Article),
    path('create/article/', createArticle, name='create_article'),
    path('backoffice/', backoffice, name='backoffice'),
    path('user/destroy/<int:id>', destroy_User),
    path('user/editRole/<int:id>', updateUserRole),
    path('allPost/', allPost, name='allPost'),
    path('article/destroy/<int:id>', destroy_Article),
    path('article/edit/<int:id>', updateArticle),
    path('user/editAll/<int:id>', updateUserAll),
    path('allProduct/', allProduct, name='allProduct'),
    path('contact/edit', updateContact, name='update_contact'),
    path('allCategorie/', allCategorie, name='allCategorie'),
    path('create/categorie/', createProductCategorie, name='create_product_categorie'),
    path('product/destroy/<int:id>', destroyProductCategorie),
    path('create/categorieBlog/', createBlogCategorie, name='create_blog_categorie'),
    path('categorieBlog/destroy/<int:id>', destroyBlogCategorie),
    path('tag/destroy/<int:id>', destroyTag),
    path('allTag/', allTag, name='allTag'),
    path('create/tag/', createTag, name='create_tag'),
    path('update_wish/', update_wish, name='update_wish'),
    path('articles/tag/<str:tag>/', articles_by_tag, name='articles_by_tag'),
    path('mailbox/', mailbox, name='mailbox'),
    path('mailbox/mark_as_read/<int:mail_id>/', mark_as_read, name='mark_as_read'),
    path('reply/<int:id>', reply, name='reply'),
    path('newsletter/', subscribe_newsletter, name='newsletter'),
    path('order/', order, name='order'),
    path('confirm-order/<int:order_id>/', ConfirmOrderView.as_view(), name='confirm_order'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('accounts/login/',connexion , name='login'),  # Vue de connexion
    path('article/validate/<int:article_id>/', validate_article, name='validate_article'),
]
