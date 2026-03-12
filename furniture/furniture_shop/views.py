from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import razorpay
from datetime import  timedelta, timezone

from django.shortcuts import  get_object_or_404
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

# Create your views here.
def user_home(re):
    return render(re,'user_home.html')

def admin_home(re):
    return render(re,'admin_home.html')
def login(re):
    if re.method == 'POST':
        c = re.POST['username']
        d = int(re.POST['password'])
        try:
            data = reg.objects.get(Username=c)
            if data.Password == d:
                re.session['user'] = c
                return redirect(user_home)
            else:
                # return HttpResponse('incorrect password')
                messages.error(re, 'INVALID CREDENTIAL!!!')
        except:
            if c == 'admin' and d == 1234:
                re.session['admin'] = d
                return redirect(admin_home)
            messages.error(re,'INVALID CREDENTIAL!!!')
    return render(re, 'login.html')


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = reg.objects.get(Email=email)
        except:
            messages.info(request,"Email id not registered")
            return redirect(forgot_password)
        # Generate and save a unique token
        token = get_random_string(length=4)
        PasswordReset.objects.create(user=user, token=token)

        # Send email with reset link
        reset_link = f'http://127.0.0.1:8000/reset/{token}'
        try:
            send_mail('Reset Your Password', f'Click the link to reset your password: {reset_link}','settings.EMAIL_HOST_USER', [email],fail_silently=False)
            # return render(request, 'emailsent.html')
        except:
            messages.info(request,"Network connection failed")
            return redirect(forgot_password)

    return render(request, 'frgt.html')

def reset_password(request, token):
    # Verify token and reset the password
    print(token)
    password_reset = PasswordReset.objects.get(token=token)
    # usr = User.objects.get(id=password_reset.user_id)
    if request.method == 'POST':
        new_password = request.POST.get('newpassword')
        repeat_password = request.POST.get('cpassword')
        if repeat_password == new_password:
            password_reset.user.Password=new_password
            password_reset.user.save()
            # password_reset.delete()
            return redirect(login)
    return render(request, 'rest-pass.html',{'token':token})




def view_user(re):
    data = reg.objects.all()
    return render(re, 'view_user.html', {'data': data})

# ✅ Admin page for pending approvals
def prod_approval(re):
    # data = Product.objects.filter()
    return render(re, 'prod_approval.html')

# ✅ User's shop page — shows only approved products



def create_user(re):
    if re.method=='POST':
        a=re.POST['name']
        b=re.POST['email']
        c=re.POST['username']
        d=int(re.POST['password'])
        e=int(re.POST['mobile'])

        if reg.objects.filter(Username=c).exists():
            # return HttpResponse(f"{c} Already exists")
            messages.error(re,f"{c} Already exists")
            return redirect(create_user)
        else:
            data=reg.objects.create(Name=a,Email=b,Username=c,Password=d,Phone=e)
            data.save()
            return redirect(login)
    return render(re,'login.html')


def logout(re):
    if 'user' in re.session or 'admin' in re.session:
        re.session.flush()
        return redirect(home)
    return redirect(home)


# def shop(request):
#     products = Product.objects.filter(status="approved")
#     return render(request, "shop.html", {"products": products})

def shop(request):
    category = request.GET.get("category")

    products = Product.objects.filter(status="approved")

    if category:
        products = products.filter(category=category)

    return render(request, "shop.html", {
        "products": products,
        "categories": Product.CATEGORY_CHOICES,
    })








def add_to_cart(re,product_id):
    if 'user' in re.session:
        user = reg.objects.get(Username=re.session['user'])
        prod = Product.objects.get(pk=product_id)

        # Add product to cart
        try:
            item = CartItem.objects.get(product=prod, user=user)
            item.quantity += 1
            item.total_price = item.quantity * prod.price
            item.save()
        except CartItem.DoesNotExist:
            CartItem.objects.create(
                product=prod,
                user=user,
                quantity=1,
                total_price=prod.price
            )


        return redirect(cart_view)   # Redirect to cart after adding
    return redirect('login')

def cart_view(re):
    user=reg.objects.get(Username=re.session['user'])
    data=CartItem.objects.filter(user=user)
    s=0
    for i in data:
        i.total_price=i.product.price*i.quantity
        s+=i.total_price
    return render(re,'cart.html',{'cart':data,'total':s})

def increase_quantity(request, item_id):
    user = reg.objects.get(Username=request.session['user'])
    item = CartItem.objects.get(pk=item_id, user=user)
    item.quantity += 1
    item.total_price = item.quantity * item.product.price
    item.save()
    return redirect(cart_view)

def decrease_quantity(request, item_id):
    user = reg.objects.get(Username=request.session['user'])
    item = CartItem.objects.get(pk=item_id, user=user)
    if item.quantity > 1:
        item.quantity -= 1
        item.total_price = item.quantity * item.product.price
        item.save()
    return redirect(cart_view)

def remove_item(request, item_id):
    user = reg.objects.get(Username=request.session['user'])
    item = CartItem.objects.get(pk=item_id, user=user)
    item.delete()
    return redirect(cart_view)


def product_status(request):
    user = reg.objects.get(Username=request.session['user'])
    pending = Product.objects.filter(user=user,status='pending')
    approved = Product.objects.filter(user=user,status='approved')
    rejected = Product.objects.filter(user=user,status='rejected')

    return render(request, 'product_status.html', {
        'pending': pending,
        'approved': approved,
        'rejected': rejected,
    })




def about(re):
    return render(re,'about.html')

def contact(re):
    return render(re,'contact.html')
def blog(re):
    return render(re,'blog.html')
def home(re):
    return render(re,'home.html')
def home_about(re):
    return render(re,'home_about.html')
def home_contact(re):
    return render(re,'home_contact.html')


def checkout(request):

    # Fetch logged-in user from session
    user = reg.objects.get(Username=request.session['user'])

    # Fetch cart items
    cart_items = CartItem.objects.filter(user=user)

    # Calculate total amount
    total = sum(item.total_price for item in cart_items)

    # Send reg object to template
    return render(request, 'checkout.html', {
        'cart': cart_items,
        'total': total,
        'reg': user     # <-- IMPORTANT
    })


def place_order(request):
    if 'user' not in request.session:
        return redirect('login')

    username = request.session['user']
    user = reg.objects.get(Username=username)
    items = CartItem.objects.filter(user=user)

    if not items:
        return HttpResponse("Cart is empty")

    total = sum(item.total_price for item in items)
    total_paise = int(total * 100)  # Razorpay accepts in paise

    if request.method == 'POST':
        address = request.POST['address']

        # Razorpay client

        client = razorpay.Client(
            auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))
        # Create Razorpay Order
        payment = client.order.create({
            'amount': total_paise,
            'currency': 'INR',
            'payment_capture': '1'
        })

        # Store in session for verification after payment
        request.session['order_data'] = {
            'user': username,
            'address': address,
            'total': total,
            'razorpay_order_id': payment['id']
        }

        return render(request, 'payment.html', {
            'payment': payment,
            'user': user,
            'items': items,
            'total': total,

        })

    return redirect('checkout')


def payment_success(request):
    if 'order_data' not in request.session:
        return HttpResponse("Invalid session")
    data = request.session['order_data']
    user = reg.objects.get(Username=data['user'])
    items = CartItem.objects.filter(user=user)

    # Create Order
    order = Order.objects.create(
        user=user,
        address=data['address'],
        total_amount=data['total']
    )

    for item in items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

    items.delete()
    del request.session['order_data']

    return render(request, 'order_success.html', {'order': order})



def add_product(request):
    if request.method == "POST":
        user = reg.objects.get(Username=request.session['user'])

        Product.objects.create(
            user=user,
            category=request.POST.get("category"),
            productName=request.POST.get("productName"),
            brand=request.POST.get("brand"),
            price=request.POST.get("price"),
            image=request.FILES.get("image"),
            storage_type=request.POST.get("storage_type"),
            capacity=request.POST.get("capacity"),
            cable_type=request.POST.get("cable_type"),
            length=request.POST.get("length"),
            cores=request.POST.get("cores"),
            clock_speed=request.POST.get("clock_speed"),
            memory_size=request.POST.get("memory_size"),
            speed=request.POST.get("speed"),
            vram=request.POST.get("vram"),
            chipset=request.POST.get("chipset"),
        )

        return redirect('shop')  # use name of URL pattern

    return render(request, "add_product.html")


def prod_approval(request):
    data = Product.objects.filter(status='pending')   # Only show PENDING items
    return render(request, 'prod_approval.html', {'data': data})

def approve_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.status = "approved"
    product.save()
    return redirect('prod_approval')

def reject_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.status = "rejected"
    product.save()
    return redirect('prod_approval')


def reorder(request):
    category = request.GET.get("category")

    products = Product.objects.filter(status="approved")

    if category:
        products = products.filter(category=category)

    return render(request, 'reorder.html', {
        "products": products,
        "categories": Product.CATEGORY_CHOICES})

def remove_product(re,id):
    product = get_object_or_404(Product,id=id)
    product.delete()
    return redirect(reorder)


def order_details(request):
    username = request.session['user']
    user = reg.objects.get(Username=username)

    orders = Order.objects.filter(user=user).order_by('-date')
    q = request.GET.get('q', '')
    status = request.GET.get('status', '')
    date_filter = request.GET.get('date_filter', '')

    if q:
        orders = orders.filter(id__icontains=q)

    if status:
        orders = orders.filter(status__iexact=status)

    if date_filter == '30':
        thirty_days_ago = timezone.now() - timedelta(days=30)
        orders = orders.filter(date__gte=thirty_days_ago)

    return render(request, 'order_details.html', {'orders':orders})


def view_orders(request):
    orders = Order.objects.all().order_by('-date')  # Latest first
    context = {'orders': orders}
    return render(request, 'view_order.html', context)


# Show selected order details
def admin_view_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    context = {'order': order}
    return render(request, 'admin_view_order.html', context)

# Update order status
def update_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == "POST":
        status = request.POST.get('status')
        order.status = status
        order.save()
        return redirect('admin_view_order', order_id=order.id)

def profile(request):
    user = reg.objects.get(Username=request.session['user'])

    if request.method == "POST":
        user.Name = request.POST.get("Name")
        user.Email = request.POST.get("Email")
        user.Phone = request.POST.get("Phone")
        user.Address = request.POST.get("Address")
        user.Place = request.POST.get("Place")
        user.District = request.POST.get("District")
        user.State = request.POST.get("State")
        user.save()

        return redirect("profile")

    return render(request, "profile.html", {"user": user})
