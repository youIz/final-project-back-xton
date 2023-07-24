import django
django.setup()

from MyApp.seed import runConnexion
from MyApp.seed import runContact
from MyApp.seed import runProduct
from MyApp.seed import runBlog

if __name__ == '__main__':
    runConnexion()
    runContact()
    runProduct()
    runBlog()

