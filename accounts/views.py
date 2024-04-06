from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
import requests
from customkit.models import CustomOrder
from .forms import RegistrationForm, UserForm
from .models import Account
from carts.models import Cart, CartItem
from orders.models import Order, OrderProduct
from carts.views import _cart_id


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # USER CREATION
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            phone_number = form.cleaned_data["phone_number"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            username = email.split("@")[0]
            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password,
            )
            user.phone_number = phone_number
            user.save()

            # USER ACTIVATION
            current_site = get_current_site(request)
            mail_subject = "Please activate your account"
            message = render_to_string(
                "accounts/account_verification_email.html",
                {
                    "user": user,
                    "domain": current_site,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": default_token_generator.make_token(user),
                },
            )
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            # messages.success(
            #     request, "Verification email sent to your registered email"
            # )
            return redirect("/accounts/login/?command=verification&email=" + email)
    else:
        form = RegistrationForm()
    context = {"form": form}
    return render(request, "accounts/register.html", context)


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            try:
                cart = Cart.objects.get(cart_id=_cart_id(request))
                is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()
                if is_cart_item_exists:
                    cart_item = CartItem.objects.filter(cart=cart)

                    # Getting the product variations by cart id
                    product_variation = []
                    for item in cart_item:
                        variation = item.variations.all()
                        product_variation.append(list(variation))

                    # Get the cart items from the user to access his product variations
                    cart_item = CartItem.objects.filter(user=user)
                    ex_var_list = []
                    id = []
                    for item in cart_item:
                        existing_variation = item.variations.all()
                        ex_var_list.append(list(existing_variation))
                        id.append(item.id)
                    for pr in product_variation:
                        if pr in ex_var_list:
                            index = ex_var_list.index(pr)
                            item_id = id[index]
                            item = CartItem.objects.get(id=item_id)
                            item.quantity += 1
                            item.user = user
                            item.save()
                        else:
                            cart_item = CartItem.objects.filter(cart=cart)
                            for item in cart_item:
                                item.user = user
                                item.save()
            except:
                pass
            auth.login(request, user)
            messages.success(request, "You are now logged in!")
            url = request.META.get("HTTP_REFERER")
            try:
                query = requests.utils.urlparse(url).query
                # query = next=/cart/checkout/
                params = dict(x.split("=") for x in query.split("&"))
                # params = {'next': '/cart/checkout/'}
                if "next" in params:
                    nextpage = params["next"]
                    return redirect(nextpage)
            except:
                return redirect("dashboard")
            # return redirect('dashboard')
        else:
            messages.error(request, "Invalid login credentials")
            return redirect("login")
    return render(request, "accounts/login.html")


@login_required(login_url="login")
def logout(request):
    auth.logout(request)
    messages.success(request, "You are logged out.")
    return redirect("login")


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Congratulations your account is activate")
        return redirect("login")
    else:
        messages.error(request, "Invalid activation link")
        return redirect("register")


@login_required(login_url="login")
def dashboard(request):
    orders = Order.objects.order_by("-created_at").filter(
        user_id=request.user.id, is_ordered=True
    )
    orders_count = orders.count()

    context = {"orders_count": orders_count}
    return render(request, "accounts/dashboard.html", context)


def forgotpassword(request):
    if request.method == "POST":
        email = request.POST["email"]
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(
                email__exact=email
            )  # da get() e procura email com case sensitive
            current_site = get_current_site(request)
            mail_subject = "Reset your password"
            message = render_to_string(
                "accounts/reset_password_email.html",
                {
                    "user": user,
                    "domain": current_site,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": default_token_generator.make_token(user),
                },
            )
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            messages.success(
                request, "Recovery password email sent to your email address"
            )
            return redirect("login")
        else:
            messages.error(request, "Account does not exist")
            return redirect("forgotpassword")
    return render(request, "accounts/forgotpassword.html")


def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        request.session["uid"] = uid
        messages.success(request, "Please reset your password")
        return redirect("resetpassword")
    else:
        messages.error(request, "This link has been expired")
        return redirect("login")


def resetpassword(request):
    if request.method == "POST":
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        if password == confirm_password:
            uid = request.session.get("uid")
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, "Password reset successful")
            return redirect("login")
        else:
            messages.error(request, "Password do not match")
            return redirect("resetpassword")
    else:
        return render(request, "accounts/resetpassword.html")


@login_required(login_url="login")
def my_orders(request):
    orders = Order.objects.filter(user=request.user, is_ordered=True).order_by(
        "-created_at"
    )
    context = {
        "orders": orders,
    }
    return render(request, "accounts/my_orders.html", context)



@login_required(login_url="login")
def my_custom_orders(request):
    orders = CustomOrder.objects.filter(user=request.user, is_ordered=False).order_by(
        "-created_at"
    )
    context = {
        "orders": orders,
    }
    return render(request, "accounts/my_custom_orders.html", context)


@login_required(login_url="login")
def edit_profile(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, request.FILES, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect("edit_profile")
    else:
        user_form = UserForm(instance=request.user)

    context = {
        "user_form": user_form,
    }
    return render(request, "accounts/edit_profile.html", context)


@login_required(login_url="login")
def change_password(request):
    if request.method == "POST":
        current_password = request.POST["current_password"]
        new_password = request.POST["new_password"]
        confirm_password = request.POST["confirm_password"]
        user = Account.objects.get(username__exact=request.user.username)
        if new_password == confirm_password:
            success = user.check_password(current_password)
            if success:
                user.set_password(new_password)
                user.save()
                # auth.Logout(request)
                messages.success(request, "Password Updated Successfully.")
                return redirect("change_password")
            else:
                messages.error(request, "Please enter valid current password")
                return redirect("change_password")
        else:
            messages.error(request, "Password does not match!")
            return redirect("change_password")
    return render(request, "accounts/change_password.html")


@login_required(login_url="login")
def order_detail(request, order_id):
    order_details = OrderProduct.objects.filter(order__order_number=order_id)
    order = Order.objects.get(order_number=order_id)
    subtotal = 0
    for i in order_details:
        subtotal += i.product_price * i.quantity
    context = {
        "order_detail": order_details,
        "order": order,
        "subtotal": subtotal,
    }
    return render(request, "accounts/order_detail.html", context)


# @login_required(login_url="login")
# def view_all_orders_to_admin(request):
#     user = request.user
#     orders = Order.objects.all().order_by("-id")
#     context = {
#         "orders": orders,
#     }
#     if user.is_admin:
#         return render(request, "accounts/view_all_orders_to_admin.html", context)
#     else:
#         return redirect("dashboard")

from datetime import timedelta
from django.utils import timezone
from django.db.models import Sum

# ... other imports ...

@login_required(login_url="login")
def view_all_orders_to_admin(request):
    user = request.user
    orders = Order.objects.all().order_by("-id")

    # Retrieve orders for the last 10 days
    ten_days_ago = timezone.now() - timedelta(days=10)
    orders_data = Order.objects.filter(created_at__gte=ten_days_ago).values('created_at__date').annotate(total_amount=Sum('order_total')).order_by('created_at__date')

    # Process order data to create xValues and yValues
    x_values = [item['created_at__date'].strftime('%Y-%m-%d') for item in orders_data]
    y_values = [item['total_amount'] for item in orders_data]

    # Pass orders data to the template context
    context = {
        "orders_data": orders_data,
        "order_x_values": x_values,
        "order_y_values": y_values,
        "orders": orders,
    }

    if user.is_admin:
        return render(request, "accounts/view_all_orders_to_admin.html", context)
    else:
        return redirect("dashboard")


@login_required(login_url="login")
def view_all_users_to_admin(request):
    user = request.user
    accounts = Account.objects.all().order_by('-id')


    context = {
        "accounts": accounts
    }

    if user.is_admin:
        return render(request, "accounts/view_all_customers_to_admin.html", context)
    else:
        return redirect('dashboard')


@login_required(login_url="login")
def view_all_custom_orders_to_admin(request):
    user = request.user
    orders = CustomOrder.objects.all().order_by('-id')


    context = {
        "orders": orders
    }

    if user.is_admin:
        return render(request, "accounts/view_all_custom_orders_to_admin.html", context)
    else:
        return redirect('dashboard')


# views.py
import pandas as pd
from django.utils import timezone

def download_excel(request):
    # Retrieve data from the Account model
    account_data = Account.objects.values(
        'first_name', 'last_name', 'username', 'email', 'phone_number',
    )

    # Create a DataFrame using pandas
    df = pd.DataFrame(account_data)

    # Convert datetime columns to timezone-unaware datetimes
    # df['date_joined'] = df['date_joined'].apply(lambda x: timezone.make_naive(x) if x else None)
    # df['last_login'] = df['last_login'].apply(lambda x: timezone.make_naive(x) if x else None)

    # Create an Excel writer object
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="account_data.xlsx"'

    # Write the DataFrame to the Excel sheet
    df.to_excel(response, index=False, engine='openpyxl')

    return response

# def download_excel(request):
#     # Retrieve data from the Account model
#     account_data = Account.objects.values(
#         'first_name', 'last_name', 'username', 'email', 'phone_number')

#     # Create a DataFrame using pandas
#     df = pd.DataFrame(account_data)

#     # Create an Excel writer object
#     response = HttpResponse(content_type='application/ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="account_data.xlsx"'

#     # Write the DataFrame to the Excel sheet
#     df.to_excel(response, index=False, engine='openpyxl')

#     return response

from django.db.models import Q
def account_search(request):
    query = request.GET.get('q')

    if query:
        results = Account.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(username__icontains=query) |
            Q(email__icontains=query) |
            Q(phone_number__icontains=query)
            # Add other fields as needed
        )
    else:
        results = Account.objects.all()

    context = {'results': results, 'query': query}
    return render(request, 'accounts/account_search.html', context)


def order_search(request):
    query = request.GET.get('q')
    if query:
        results = Order.objects.filter(
            Q(order_number__icontains=query)

        )
    else:
        results = Order.objects.all()
    
    context = {'results': results, 'query': query}
    return render(request, 'accounts/order_search.html', context)


def custom_order_search(request):
    query = request.GET.get('q')
    if query:
        results = CustomOrder.objects.filter(
            Q(order_number__icontains=query)

        )
    else:
        results = Order.objects.all()
    
    context = {'results': results, 'query': query}
    return render(request, 'accounts/custom_order_search.html', context)