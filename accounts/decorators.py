from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_funct):
    def wrapper_funct(request, *args, **kwargs):
            
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_funct(request, *args, **kwargs)
    
    return wrapper_funct

def allowed_users(allowed_roles=[]):
    def decorator(view_funct):
        def wrapper_funct(request, *args, **kwargs):
            
            print('working: ', allowed_roles)
            group = None 
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
           
            if group in allowed_roles:
                return view_funct(request, *args, **kwargs)
            
            else:
                return HttpResponse('You are not authorised to view this page')           
        return wrapper_funct
    return decorator

def admin_only(view_funct):
    def wrapper_funct(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'customer':
            return redirect('user-page')
        
        if group == 'admin':
            return view_funct(request, *args, **kwargs)
        
    return wrapper_funct


