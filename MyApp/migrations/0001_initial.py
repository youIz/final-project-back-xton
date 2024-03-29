# Generated by Django 4.2.3 on 2023-07-22 16:16

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnonymousUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='AnonymousUser2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=1000)),
                ('description', models.TextField()),
                ('validate', models.BooleanField(default=False)),
                ('creation', models.DateField(default=django.utils.timezone.now)),
                ('update', models.DateField(auto_now=True)),
                ('view', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.CharField(max_length=20)),
                ('adresse', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('fax', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Contact_mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('read', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(default=3, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('img_url', models.CharField(max_length=500)),
                ('newsletter', models.BooleanField(default=False)),
                ('country', models.CharField(max_length=80, null=True)),
                ('company', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=150, null=True)),
                ('city', models.CharField(max_length=60, null=True)),
                ('state', models.CharField(max_length=60, null=True)),
                ('postcode', models.CharField(max_length=6, null=True)),
                ('phone', models.CharField(max_length=25, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('role', models.ForeignKey(default=4, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MyApp.role')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.contact')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.CharField(max_length=1000)),
                ('img2', models.CharField(max_length=1000)),
                ('img3', models.CharField(max_length=1000)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('name', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField()),
                ('promo', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('stock', models.IntegerField(default=0)),
                ('wish', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MyApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('country', models.CharField(max_length=80)),
                ('company', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=60)),
                ('postcode', models.CharField(max_length=6)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=25)),
                ('validate', models.BooleanField(default=False)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.cart')),
            ],
        ),
        migrations.CreateModel(
            name='Note2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('text', models.TextField(default='valeur_par_défaut', max_length=300)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('anonymous_author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MyApp.anonymoususer2')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.article')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(blank=True, max_length=50)),
                ('text', models.TextField(default='valeur_par_défaut', max_length=300)),
                ('anonymous_author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MyApp.anonymoususer')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.product')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, max_length=2, null=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.product')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(through='MyApp.CartItem', to='MyApp.product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.categoryarticle'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='MyApp.tag'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
