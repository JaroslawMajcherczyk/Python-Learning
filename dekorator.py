

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("** Dodałeś posypke ✨✨✨ **")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("** Dodałeś czekolade 🍫🍫🍫 **")
        func(*args, **kwargs)
    return wrapper


@add_fudge
@add_sprinkles
def get_ice_cream(flaver):
    print(f"Tu są twoje {flaver} lody 🍦🍧🍨🧁")

get_ice_cream("Czekoladowe")