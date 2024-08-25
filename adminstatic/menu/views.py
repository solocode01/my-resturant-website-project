from django.http import JsonResponse
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    menu_new = Menu.objects.all().order_by("-date_updated")[:3]
    popular_menu = Menu.objects.filter(popular=True)
    return render(request, 'menu/index.html', {'menu_new': menu_new, 'home': True,
                                               'popular_menu': popular_menu})

def about(request):
    return render(request, 'menu/about.html', {'about': True,})

def menu(request):
    menu = Menu.objects.all()
    return render(request, 'menu/menu.html', {'food_menu': True, 'menu': menu})

def menu_details(request, slug):
    try:
        menu = Menu.objects.get(slug=slug)
    except Exception as e:
        messages.warning(request, e)
        return redirect("menu")
    return render(request, 'menu/menu_details.html', {'menu': menu})

from django.views.decorators.http import require_POST
from django.core.serializers import serialize
from django.contrib.auth.decorators import login_required

@require_POST
def update_cart(request):
    id = request.POST.get('id')
    print(id)
    menu = Menu.objects.get(id=id)
    print(menu)
    cart = Cart.objects.get(is_paid=False, checker=True)
    cart_items = CartItem.objects.get(cart=cart, menu=menu)
    cart_items.quantity += 1
    cart_items.save()
    return JsonResponse({"msg": f"{menu.name} updated successfully"})

@require_POST
def reduce_cart(request):
    id = request.POST.get('id')
    print(id)
    menu = Menu.objects.get(id=id)
    print(menu)
    cart = Cart.objects.get(is_paid=False, checker=True)
    cart_items = CartItem.objects.get(cart=cart, menu=menu)
    cart_items.quantity -= 1
    cart_items.save()
    if cart_items.quantity < 1:
        cart_items.delete()
        return JsonResponse({"msg": f"{menu.name} removed successfully"})
    return JsonResponse({"msg": f"{menu.name} quantity reduced successfully"})
    

@require_POST
def add_to_cart(request):
    id = request.POST.get('id')
    print(id)
    menu = Menu.objects.get(id=id)
    print(menu)
    cart, _ = Cart.objects.get_or_create(is_paid=False, checker=True)
    cart_items, created = CartItem.objects.get_or_create(cart=cart, menu=menu)
    
    if not created:
        print("i am already available")
        return JsonResponse({"msg": f'{menu.name} already in cart'})
    else:
        print("i am just added now")
        # messages.info(request, f"{menu.name} added to cart")
        cart = CartItem.objects.count()
        print(cart)
        return JsonResponse({"msg": f"{menu.name} added to cart", "total": cart})
    
def remove_cart(request, id):
	try:
		cart_item = CartItem.objects.get(id=id)
		cart_item.delete()
	except Exception as e:
		print(e)
	return redirect(request.META.get('HTTP_REFERER'))

def view_cart(request):
	cart = CartItem.objects.filter(cart__is_paid=False, cart__checker=True)
	return render(request, 'menu/cart.html', {'cart': cart})

@login_required(login_url="login")
def checkout(request):
    cart = Cart.objects.filter(is_paid=False, checker=True).first()
    # print(cart.first().cart)
    if cart:
        customer = Customer.objects.filter(user=request.user).first()
        
        if customer:
            form = CheckoutForm(instance=customer)
            
            if request.method == "POST":
                # customer = Customer.objects.get()
                form = CheckoutForm(request.POST, instance=customer)
                
                if form.is_valid():
                    form.save()
                    
                    customer = Customer.objects.get(user=request.user)
                    return render(request, "menu/payment.html", {'customer': customer, 'cart': cart, "pub_key": settings.PAYSTACK_PUBLIC_KEY})
        else:
            form = CheckoutForm()
            
            if request.method == "POST":
                # customer = Customer.objects.get()
                form = CheckoutForm(request.POST)
                
                if form.is_valid():
                    user = form.save(commit=False)
                    print(user)
                    user.user = request.user
                    user.save()
                    
                    customer = Customer.objects.get(user=request.user)
                    return render(request, "menu/payment.html", {'customer': customer, 'cart': cart, "pub_key": settings.PAYSTACK_PUBLIC_KEY})
            # address = request.POST['address']
            # street = request.POST['street']
            # state = request.POST['state']
            # city = request.POST['city']
            # pincode = request.POST['pincode']
            # landmark = request.POST['landmark']
            
            # customer = Customer.objects.create(address=address, city=city, state=state, street=street, pin_code=pincode, landmark=landmark)
            # print(customer)
            
        return render(request, 'menu/checkout.html', {'cart': cart, 'form': form })
    else:
        messages.info(request, "please add an item to your cart before you can checkout")
        return redirect("menu")

def veriy_payment(request, ref):
    cart = Cart.objects.get(ref=ref)
    status = cart.verify_payment()
    print(status)
    
    if status:
        print(status)
        cart.is_paid = True
        cart.checker = False
        cart.save()
        return redirect('success')
    else:
        return redirect('home')

def success(request):
    user = request.user
    context = {'user': user}
    return render (request, 'menu/success.html', context)


def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = RegisterForm()
        
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.info(request, f"Welcome {user.username} Welcome to Solomon's Cuisine")
                return redirect("home")
            messages.info(request, "Username or Password incorrect")
        return render(request, 'auth/signup.html', {'form': form})
    
def login_page(request):
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        
        try:
            myuser = User.objects.filter(username=username).exists()
        except myuser.DoesNotExist:
            messages.info(request, "User does not exist")
            return redirect('login')
        
        myuser = authenticate(request, username=username, password=password)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, f"Hello {username}, Welcome to Solomon's Cuisine")
            return redirect('home')
        else:
            if not User.objects.filter(username=username, password=password).exists():
                messages.warning(request, "incorrect password")
            else:
                messages.info(request, "account doesn\'t exists")
            return redirect('login')
    return render(request, 'auth/login.html')

def logout_page(request):
    messages.info(request, f"Hello {request.user}, you have logged out")
    logout(request)
    return redirect('home')