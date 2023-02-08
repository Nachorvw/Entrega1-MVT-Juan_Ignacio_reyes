from django.http import HttpResponse
from django.shortcuts import redirect

#? function to redirect a user if its logged in 
def logged_in_user(view_func):
    def wrapper_func(request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect("index")
        else:
            return view_func(request,*args, **kwargs) #? if the user is not logged in, we let the user view the page he requested
    return wrapper_func

#? function to add authentication based on roles
def allowed_users(allowed_roles=[""]): #? we get the group
    def decorator(view_func):
        def wrapper_func(request,*args, **kwargs):
            
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name #? we get the first and only group that the user haves

            if group in allowed_roles or request.user.is_superuser: #? if the user is in that role or is an admin, he can enter the view
                return view_func(request,*args, **kwargs)

            else:
                return HttpResponse("usted no tiene los permisos para ingresar a esta pagina") #? if not we return an "error"
            
        return wrapper_func
    return decorator