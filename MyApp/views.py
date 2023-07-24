from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.db.models import F
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.db.models import Count
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.db.models import ProtectedError
import random
from django.urls import reverse
from django.views.generic.base import View


# Create your views here.

# __________________________________________________________________________
def home(request):
    cart_items = CartItem.objects.all()[:4]
    contacts = Contact.objects.all()
    products = Product.objects.order_by('-id')[:6]
    allProducts = Product.objects.all()
    popular_products = Product.objects.annotate(comment_count=Count('note')).order_by('-comment_count')[:6]
    latest_articles = Article.objects.all().order_by('-id')[:3]
    return render(request, 'MyApp/frontend/home.html', {'contacts' : contacts, 'products': products, 'popular_products': popular_products, 'latest_articles': latest_articles, 'allProducts': allProducts, "cart_items": cart_items})

def product(request, category_id=None):
    cart_items = CartItem.objects.all()[:4]
    allProducts = Product.objects.all()
    products = Product.objects.all()
    active_category = None
    search_query = request.GET.get('q')
    if category_id is not None:
        category = Category.objects.get(id=category_id)
        products = products.filter(category=category)
        active_category = category
    # Filtrer les articles en fonction du nom recherché (search_query)
    if search_query:
        products = products.filter(name__icontains=search_query)
    categories = Category.objects.all()
    paginator = Paginator(products, 10)  # Spécifiez le nombre de produits par page (ici, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'MyApp/frontend/products-left-sidebar-2.html', {
        'products': page_obj,
        'categories': categories,
        'active_category': active_category,
        'allProducts': allProducts,
        "cart_items": cart_items
    })

def blog(request):
    cart_items = CartItem.objects.all()[:4]
    allProducts = Product.objects.all()
    category_id = request.GET.get('category_id')
    search_query = request.GET.get('q')
    allTags = Tag.objects.all()
    if category_id == "tous":
        articles = Article.objects.all()
    elif category_id is not None:
        category = CategoryArticle.objects.get(pk=category_id)
        articles = Article.objects.filter(category=category)
    else:
        articles = Article.objects.all()
    # Filtrer les articles en fonction du nom recherché (search_query)
    if search_query:
        articles = articles.filter(title__icontains=search_query)
    categories = CategoryArticle.objects.all()
    # Récupérer les articles avec le plus de commentaires
    popular_articles = Article.objects.annotate(comment_count=Count('note2')).order_by('-comment_count')[:3]
    # Vérifier s'il y a des articles avec des commentaires
    if len(popular_articles) == 0:
        # Récupérer les trois premiers articles
        popular_articles = Article.objects.all()[:3]
    paginator = Paginator(articles, 6)  # Spécifiez le nombre de produits par page (ici, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'MyApp/frontend/blog-5.html', {
        'articles': page_obj, 
        'categories': categories, 
        'popular_articles': popular_articles,
        'allProducts': allProducts,
        'allTags': allTags,
        "cart_items": cart_items
        })

def articles_by_tag(request, tag):
    articles = Article.objects.filter(tag__tag=tag)
    context = {
        'articles': articles,
        'tag': tag,
    }
    return render(request, 'MyApp/frontend/blog-5.html', context)

def contact(request):
    cart_items = CartItem.objects.all()[:4]
    allProducts = Product.objects.all()
    contacts = Contact.objects.all()
    return render(request, 'MyApp/frontend/contact.html', {'contacts': contacts, 'allProducts': allProducts, "cart_items": cart_items})

def checkout(request):
    allProducts = Product.objects.all()
    cart_items = []
    total = 0
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = cart.cartitem_set.all()
        user = request.user
        for cart_item in cart_items:
            cart_item.total = cart_item.quantity * cart_item.product.price
            total += cart_item.total
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            user.country = request.POST['country']
            user.company = request.POST['company']
            user.address = request.POST['address']
            user.city = request.POST['city']
            user.state = request.POST['state']
            user.postcode = request.POST['postcode']
            email = request.POST['email']
            user.phone = request.POST['phone']
            user.save()
            order = Order(
                cart=cart,
                first_name=first_name,
                last_name=last_name,
                country=user.country,
                company=user.company,
                address=user.address,
                city=user.city,
                state=user.state,
                postcode=user.postcode,
                email=email,
                phone=user.phone
            )
            order.save()
            # Création du récapitulatif des achats
            recapitulation = render_to_string('MyApp/backend/recapitulation.html', {"cart_items": cart_items})
            # Envoi du mail avec récapitulatif des achats
            subject = 'Statut de la commande'
            message = 'Votre commande a été effectuée et est en cours de validation.\n\n' + recapitulation
            from_email = 'youssefcasawe2@gmail.com'           
            to_email = order.email
            send_mail(subject, message, from_email, [to_email], html_message=message)
            try:
                cart_items.delete()  # Supprimer les cart_items associés au panier
            except ProtectedError:
                # Gérer l'erreur si les cart_items sont protégés
                pass
    show = Product.objects.get(id=1)  # Remplacez 1 par votre logique de récupération du produit à afficher
    return render(
        request,
        'MyApp/frontend/checkout.html',
        {"cart_items": cart_items, "total": total, "show": show, 'allProducts': allProducts}
    )

def cart(request):
    cart_items = CartItem.objects.all()[:4]
    total = 0  # Variable pour stocker le total de la commande
    for item in cart_items:
        item.total = item.product.price * item.quantity
        total += item.total  # Accumuler le sous-total à chaque itération
    allProducts = Product.objects.all()
    return render(request, 'MyApp/frontend/cart.html', {'allProducts': allProducts, "cart_items": cart_items, "total": total})

def cart_item_delete(request, item_id):
    if request.method == 'POST':
        cart_item = CartItem.objects.get(pk=item_id)
        cart_item.delete()
        return redirect('cart')  # Rediriger vers la page du panier après la suppression
    else:
        return redirect('cart')  # Rediriger vers la page du panier en cas de requête GET

def backoffice(request):
    users = User.objects.all()
    return render(request, 'MyApp/backend/backoffice.html', {'users': users})

def allPost(request):
    users = User.objects.all()
    articles = Article.objects.all()
    return render(request, 'MyApp/backend/allPost.html', {'articles': articles, 'users': users})

def allProduct(request):
    users = User.objects.all()
    products = Product.objects.all()
    return render(request, 'MyApp/backend/allProduct.html', {'products': products, 'users': users})

def allCategorie(request):
    articleCategory = CategoryArticle.objects.all
    productsCategory = Category.objects.all()
    return render(request, 'MyApp/backend/allCategories.html', {'productsCategory': productsCategory, 'articleCategory': articleCategory})

def allTag(request):
    tags = Tag.objects.all()
    return render(request, 'MyApp/backend/allTags.html', {'tags': tags})

def mailbox(request):
    contact_mails = Contact_mail.objects.all()
    return render(request, 'MyApp/backend/mailbox.html', {'contact_mails': contact_mails})

def validate_article(request, article_id):
    article = Article.objects.get(id=article_id)
    article.validate = True
    article.save()
    return redirect('allPost')




# BLOG VIEWS__________________________________________________________________________________
def readArticle(request, id):
    allProducts = Product.objects.all()
    notes = Note2.objects.filter(article_id=id)
    show = Article.objects.get(id=id)
    category = CategoryArticle.objects.all()
    tags = Tag.objects.all()
    show.view += 1  # Incrémentation du champ 'view' de l'article
    show.save()  # Enregistrement des modifications
    return render(request, 'MyApp/frontend/single-blog-1.html', {"show": show, "notes": notes, 'allProducts': allProducts, 'category': category, 'tags':tags})

def comment_create2(request, id):
    if request.method == 'POST':
        article = Article.objects.get(id=id)
        titre = request.POST.get('review-title')
        text = request.POST.get('texte')
        if request.user.is_authenticated:
            current_note = Note2.objects.create(
                author=request.user,
                article=article,
                titre=titre,
                text=text
            )
        else:
            name = request.POST.get('name')
            email = request.POST.get('email')
            
            anonymous_user = AnonymousUser2.objects.create(
                name=name,
                email=email
            )
            current_note = Note2.objects.create(
                anonymous_author=anonymous_user,
                article=article,
                titre=titre,
                text=text
            )
        # Redirection vers la page de détails de l'article
        return redirect('detail_article', id=article.id)
    return render(request, 'MyApp/frontend/single-blog-1.html')

def updateArticle(request,id):
    edit = Article.objects.get(id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('allPost')
    else:
        form = ArticleForm(instance=edit)
    return render(request, 'MyApp/backend/update.html', {'form': form})

def destroy_Article(request, id):
    destroy = Article(id)
    destroy.delete()
    return redirect('allPost')

def createArticle(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            # Définir article.validate en fonction de l'utilisateur créateur
            if request.user.role.id == 1 or request.user.role.id == 3:
                article.validate = True
                article.save()
            
            return redirect('allPost')
    else:
        form = ArticleForm()
    return render(request, 'MyApp/backend/update.html', {"form": form})

def createBlogCategorie(request):
    if request.method == 'POST':
        form = ArticleCategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allCategorie')
    else:
        form = ArticleCategorieForm()
    return render(request, 'MyApp/backend/update.html', {"form": form})

def destroyBlogCategorie(request, id):
    destroy = CategoryArticle(id)
    destroy.delete()
    return redirect('allCategorie')

def createTag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allTag')
    else:
        form = TagForm()
    return render(request, 'MyApp/backend/update.html', {"form": form})

def destroyTag(request, id):
    destroy = Tag(id)
    destroy.delete()
    return redirect('allTag')



# VIEWS CONNEXION___________________________________________________________
def signup(request):
    allProducts = Product.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        newsletter = request.POST.get('newsletter', False) == 'True'
        img_url = request.POST['img_url']
        user = User(username=username, password=make_password(password), email=email, img_url=img_url, newsletter=newsletter)
        user.save()
        # Info du mail 
        subject = 'Bienvenue sur notre site'
        message = 'Merci de vous être inscrit à notre site.'
        from_email = 'youssefcasawe2@gmail.com'          
        to_email = user.email
        # Envoi du mail
        send_mail(subject, message, from_email, [to_email])
        
        if newsletter == True:
            subject = 'Our Newsletter !'
            message = 'Merci de vous être inscrit à notre Newsletter.'
            from_email = 'youssefcasawe2@gmail.com'           
            to_email = user.email
            send_mail(subject, message, from_email, [to_email])
            
        login(request, user)
        return redirect('home')
    return render(request, 'MyApp/frontend/signup.html', {'allProducts': allProducts})

def connexion(request):
    allProducts = Product.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'MyApp/frontend/login.html', {'allProducts': allProducts})

def deconnexion(request):
    logout(request)
    return redirect('home')

def updateUserRole(request,id):
    allProducts = Product.objects.all()
    edit = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserFormRole(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('backoffice')
    else:
        form = UserFormRole(instance=edit)
    return render(request, 'MyApp/backend/update.html', {'form': form, 'allProducts': allProducts})

def updateUserAll(request,id):
    allProducts = Product.objects.all()
    edit = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserFormAll(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('backoffice')
    else:
        form = UserFormAll(instance=edit)
    return render(request, 'MyApp/backend/update.html', {'form': form, 'allProducts': allProducts})

def destroy_User(request, id):
    destroy = User(id)
    destroy.delete()
    return redirect('backoffice')

def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST['email']
        newsletter = Newsletter(email=email)
        newsletter.save()
        # Info du mail 
        subject = 'Our Newsletter !'
        message = 'Merci de vous être inscrit à notre Newsletter.'
        from_email = 'youssefcasawe2@gmail.com'           
        to_email = email
        # Envoi du mail
        send_mail(subject, message, from_email, [to_email])
        previous_page = request.META.get('HTTP_REFERER')
        if previous_page:
            return redirect(previous_page)
        else:
            return HttpResponseBadRequest("Unable to determine previous page.") 




# VIEWS CONTACT___________________________________________________________
def updateContact(request):
    edit = Contact.objects.get(id=1)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm(instance=edit)
    return render(request, 'MyApp/backend/update.html', {'form': form})

def contact_mail(request):
    cart_items = CartItem.objects.all()[:4]
    allProducts = Product.objects.all()
    contacts = Contact.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['EMAIL']
        message = request.POST['message']
        contact = Contact_mail(name=name, email=email, message=message)
        contact.save()
        # Info du mail 
        subject = 'Prise de contact'
        message = "Quelqu'un a essayée de vous contacter"
        from_email = 'youssefcasawe2@gmail.com'       
        # to_email = User.objects.filter(role=1).first() 
        to_email = 'youssefcasawe2@gmail.com' 
        # Envoi du mail
        send_mail(subject, message, from_email, [to_email])
        return redirect('home')
    return render(request, 'MyApp/frontend/contact.html', {'contacts': contacts, 'allProducts': allProducts, "cart_items": cart_items})

def destroyContact_mail(request, id):
    destroy = Contact_mail(id)
    destroy.delete()
    return redirect('mailbox')

def mark_as_read(request, mail_id):
    mail = get_object_or_404(Contact_mail, id=mail_id)
    mail.toggle_read()
    return redirect('mailbox')

def reply(request, id):
    contact_msg = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.to = contact_msg
            reply.save()
            send_mail('Reply to your message', reply.content, 'youssefcasawe2@gmail.com', [contact_msg.email])
            return redirect('mailbox')
    else:
        form = ReplyForm()
    return render(request, "MyApp/backend/reply.html", { "form": form, "errors": form.errors })




# VIEWS PRODUCT______________________________________________________________________
def readProduct(request, id):
    show = Product.objects.get(id=id)
    notes = Note.objects.filter(product=id)
    # Obtenir 5 produits aléatoires
    all_products = Product.objects.all()
    random_products = random.sample(list(all_products), 5)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if not request.user.is_authenticated:
            # Rediriger vers la page de connexion en conservant l'URL de redirection
            login_url = reverse('login')
            return redirect(f'{login_url}?next={request.path}')
        cart, created = Cart.objects.get_or_create(user=request.user)
        # Récupérer la valeur de la taille depuis la requête POST
        size = request.POST.get('size')
        # Vérifier si la taille est définie et attribuer une valeur par défaut si elle est None
        if size is None:
            size = 'S'  # Ou une autre valeur par défaut
        if 'remove_item' in request.POST:
            remove_item_id = int(request.POST['remove_item'])
            remove_item = CartItem.objects.get(id=remove_item_id)
            # Restaurer le stock du produit correspondant
            remove_item.restore_stock()
            # Supprimer l'article du panier
            remove_item.delete()
        else:
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=show, size=size)
            # Vérifier si la quantité ajoutée dépasse le stock disponible
            stock_available = show.stock
            if quantity > stock_available:
                quantity = stock_available  # Réduire la quantité au stock disponible
            # Si le CartItem existe déjà, mettez à jour la quantité plutôt que de créer un nouveau CartItem
            if not created:
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity
            cart_item.save()
            # Mettre à jour le stock du produit
            show.stock -= quantity
            show.save()
        # Rediriger vers la page du produit après l'ajout ou la suppression de l'article
        return redirect('detail_Product', id=id)
    cart_items = []
    total = 0
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = cart.cartitem_set.all()
        total = sum(item.quantity * item.product.price for item in cart_items)
    return render(
        request,
        'MyApp/frontend/products-type-1.html',
        {"show": show, "notes": notes, "cart_items": cart_items, "total": total, "random_products": random_products}
    )

def updateProduct(request,id):
    edit = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('allProduct')
    else:
        form = ProductForm(instance=edit)
    return render(request, 'MyApp/backend/update.html', {'form': form})

def updateStockProduct(request,id):
    edit = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductStockForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('allProduct')
    else:
        form = ProductStockForm(instance=edit)
    return render(request, 'MyApp/backend/update.html', {'form': form})

def destroy_Product(request, id):
    destroy = Product(id)
    destroy.delete()
    return redirect('allProduct')

def createProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('back_product')
    else:
        form = ProductForm()
    return render(request, 'MyApp/backend/update.html', {"form": form})

def comment_create(request, id):
    if request.method == 'POST':
        product = Product.objects.get(id=id)
        titre = request.POST.get('review-title')
        text = request.POST.get('texte')
        if request.user.is_authenticated:
            current_note = Note.objects.create(
                author=request.user,
                product=product,
                titre=titre,
                text=text
            )
        else:
            name = request.POST.get('name')
            email = request.POST.get('email')
            anonymous_user = AnonymousUser.objects.create(
                name=name,
                email=email
            )
            current_note = Note.objects.create(
                anonymous_author=anonymous_user,
                product=product,
                titre=titre,
                text=text
            )
        return redirect('detail_Product', id=id)
    return render(request, 'MyApp/frontend/products-type-1.html')

def createProductCategorie(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allCategorie')
    else:
        form = CategoryForm()
    return render(request, 'MyApp/backend/update.html', {"form": form})

def destroyProductCategorie(request, id):
    destroy = Category(id)
    destroy.delete()
    return redirect('allCategorie')

def update_wish(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        wish = request.POST.get('wish')
        # Effectuez les modifications nécessaires dans votre base de données Django
        # par exemple, en utilisant le modèle Product et en mettant à jour l'attribut 'wish' du produit correspondant
        product = Product.objects.get(id=product_id)
        product.wish = wish
        product.save()
    return redirect('home')  # Redirigez l'utilisateur vers la vue souhaitée après la mise à jour

def order(request):
    orders = Order.objects.all()
    return render(request, 'MyApp/backend/order.html', {'orders': orders})

class ConfirmOrderView(View):
    def post(self, request, order_id):
        order = Order.objects.get(id=order_id)
        order.validate = True
        order.save()
        # Info du mail 
        subject = 'Statut de la commande'
        message = 'Votre commande a bien été validé'
        from_email = 'youssefcasawe2@gmail.com'           
        to_email = order.email
        # Envoi du mail
        send_mail(subject, message, from_email, [to_email])
        return redirect('order')


