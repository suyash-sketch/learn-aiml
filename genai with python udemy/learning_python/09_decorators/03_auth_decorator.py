from functools import wraps

def require_admin(funct):
    @wraps(funct)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied: Admins only")
        else:
            return funct(user_role)
    return wrapper


@require_admin
def access_tea_inventory(role):
    print("Acess granted to tea inventory")

access_tea_inventory("user")
access_tea_inventory("admin")