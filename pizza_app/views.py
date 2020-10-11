from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Pizza_Model, User_Model, Order_Model
from django.contrib.auth.models import User


# Create your views here.
def admin_login_view(request):
    return render(request, 'pizza_app/admin_login.html')


def authenticate_admin(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None and user.username == 'debiprasad':
        login(request, user)
        return redirect('admin_homepage')
    if user is None:
        messages.add_message(request, messages.ERROR, 'Invalid User Name or Password')
        return redirect('admin_login_page')


def admin_homepage_view(request):
    context = {'pizzas': Pizza_Model.objects.all()}
    return render(request, 'pizza_app/admin_homepage.html', context)


def logout_admin(request):
    logout(request)
    return redirect('admin_login_page')


def add_pizza(request):
    name = request.POST['pizza']
    price = request.POST['price']
    Pizza_Model(name=name, price=price).save()
    return redirect('admin_homepage')


def delete_pizza(request, pizza_id):
    Pizza_Model.objects.filter(id=pizza_id).delete()
    return redirect('admin_homepage')


def homepage_view(request):
    return render(request, 'pizza_app/homepage.html')


def signup_user(request):
    user_name = request.POST['username']
    password = request.POST['password']
    phone_no = request.POST['phone']
    if User.objects.filter(username=user_name).exists():
        messages.add_message(request, messages.ERROR, 'User Already Exists')
        return redirect('homepage')
    User.objects.create_user(username=user_name, password=password).save()
    last_object = len(User.objects.all()) - 1
    User_Model(user_id=User.objects.all()[int(last_object)].id, phone_no=phone_no).save()
    messages.add_message(request, messages.ERROR, "Congrats!You're Successfully Registered")
    return redirect('homepage')


def user_login_view(request):
    return render(request, 'pizza_app/user_login.html')


def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('user_page')
    if user is None:
        messages.add_message(request, messages.ERROR, 'Invalid User Name or Password')
        return redirect('user_login_page')


def user_welcome_view(request):
    if not request.user.is_authenticated:
        return redirect('user_login_page')
    username = request.user.username
    context = {'username': username, 'pizzas': Pizza_Model.objects.all()}
    return render(request, 'pizza_app/welcome_user.html', context)


def user_logout(request):
    return redirect('user_login_page')


def place_order(request):
    if not request.user.is_authenticated:
        return redirect('user_login_page')
    user_name = request.user.username
    phone = User_Model.objects.filter(user_id=request.user.id)[0].phone_no
    user_address = request.POST['address']
    ordered_items = ""
    for pizza in Pizza_Model.objects.all():
        pizza_id = pizza.id
        name = pizza.name
        price = pizza.price
        quantity = request.POST.get(str(pizza_id), " ")
        if str(quantity) != "0" and str(quantity) != " ":
            ordered_items = ordered_items + name + " " + "Price: " + str(
                int(quantity) * int(price)) + " " + "Quantity: " + quantity + "    "
    Order_Model(user_name=user_name, phone_no=phone, user_address=user_address, ordered_items=ordered_items).save()
    if str(quantity) != "0" and str(quantity) != " ":
        messages.add_message(request, messages.ERROR, 'Order Placed Successfully. Thank you for using our Service :)')
        return redirect('user_page')
    messages.add_message(request, messages.ERROR, 'Please select at-least one Item :)')
    return redirect('user_page')


def user_orders(request):
    orders = Order_Model.objects.filter(user_name=request.user.username)
    context = {'orders': orders}
    return render(request, 'pizza_app/user_orders_section.html', context)


def admin_order(request):
    orders = Order_Model.objects.all()
    context = {'orders': orders}
    return render(request, 'pizza_app/admin_orders_section.html', context)


def accept_order(request, order_id):
    order = Order_Model.objects.get(id=order_id)
    order.order_status = "Accepted"
    order.save()
    return redirect(request.META['HTTP_REFERER'])


def decline_order(request, order_id):
    order = Order_Model.objects.get(id=order_id)
    order.order_status = "Declined"
    order.save()
    return redirect(request.META['HTTP_REFERER'])
