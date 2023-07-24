from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

class Stop(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if not request.user.is_authenticated:
            if request.path.startswith('/backoffice/'):
                return redirect('home')
        if request.path == '/allProduct/':
            user = request.user
            if user.is_authenticated:
                if user.role.id == 1 or user.role.id == 2 or user.role.id == 3:
                    return None
                else: 
                    return redirect('backoffice')
            else:
                return redirect('backoffice')
        if request.path in ['/contact/edit']:
            user = request.user
            if user.is_authenticated:
                if user.role.id == 1 or user.role.id == 3:
                    return None
                else: 
                    return redirect('backoffice')
            else:
                return redirect('backoffice')
        if request.path in ['/mailbox/','/order/', '/allTag/', '/allCategorie/']:
            user = request.user
            if user.is_authenticated:
                if user.role.id == 1:
                    return None
                else: 
                    return redirect('backoffice')
            else:
                return redirect('backoffice')
            




