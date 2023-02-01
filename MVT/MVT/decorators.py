from django.http import HttpResponse
from django.shortcuts import redirect


def logged_in_user(view_func):
    def wrapper_func(request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect("index")
        else:
            return view_func(request,*args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[""]):
    def decorator(view_func):
        def wrapper_func(request,*args, **kwargs):
            
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles or request.user.is_superuser:
                return view_func(request,*args, **kwargs)

            else:
                return HttpResponse("usted no tiene los permisos para ingresar a esta pagina")
            
        return wrapper_func
    return decorator