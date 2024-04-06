import datetime
import json

from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from carts.models import CartItem
from .forms import OrderForm
from .models import Order, OrderProduct,Payment
from store.models import Product

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import stripe

# def payments(request):
#     # body = json.loads(request.body)
#     try:
#         body = json.loads(request.body)
#     except json.JSONDecodeError as e:
#     # Handle the JSONDecodeError, log the error, and return an appropriate response
#         print(request.body)
#         return JsonResponse({"error": "Invalid JSON data"}, status=400)

#     order = Order.objects.get(
#         user=request.user, is_ordered=False, order_number=body["orderID"]
#     )
#     # armazena os detalhes da transação na tabela Payments
#     payment = Payment(
#         user=request.user,
#         payment_id=body["transID"],
#         payment_method=body["payment_method"],
#         amount_paid=order.order_total,
#         status=body["status"],
#     )
#     payment.save()
#     order.payment = payment
#     order.is_ordered = True
#     order.save()

#     # insere cart itens na tabela OrderProduct
#     cart_items = CartItem.objects.filter(user=request.user)
#     for item in cart_items:
#         orderproduct = OrderProduct()
#         orderproduct.order_id = order.id
#         orderproduct.payment = payment
#         orderproduct.user_id = request.user.id
#         orderproduct.product_id = item.product_id
#         orderproduct.quantity = item.quantity
#         orderproduct.product_price = item.product.price
#         orderproduct.ordered = True
#         orderproduct.save()

#         # pega as variações de cada produto em CartItem
#         cart_item = CartItem.objects.get(id=item.id)
#         product_variation = cart_item.variations.all()
#         orderproduct = OrderProduct.objects.get(id=orderproduct.id)
#         orderproduct.variations.set(product_variation)
#         orderproduct.save()

#         # reduz a quantidade dos produtos vendidos
#         product = Product.objects.get(id=item.product_id)
#         product.stock -= item.quantity
#         product.save()

#     # reseta o carrinho
#     CartItem.objects.filter(user=request.user).delete()

#     # envia recibo da ordem para o cliente para o email registrado no cadastro de usuario
#     mail_subject = "Thank you with your Order!"
#     message = render_to_string(
#         "orders/order_received_email.html",
#         {
#             "user": request.user,
#             "order": order,
#         },
#     )
#     to_email = request.user.email
#     send_email = EmailMessage(mail_subject, message, to=[to_email])
#     send_email.send()

#     # envia order_number e transaction_id para sendData usando jsonResponse
#     data = {"order_number": order.order_number, "transID": payment.payment_id}
#     return place_order(request, payment=payment, data=data)




from django.core.mail import mail_admins

def place_order(request, total=0, quantity=0):
    current_user = request.user
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect("store")
    grand_total = 0
    tax = 0
    for cart_item in cart_items:
        total += cart_item.product.price * cart_item.quantity
        quantity += cart_item.quantity
    tax = (2 * total) / 100  # aplicar regra de imposto correta aki
    grand_total = total + tax
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            # armazena todos os dados da ordem de pagamento em Order
            data = Order()
            data.user = current_user
            data.first_name = form.cleaned_data["first_name"]
            data.last_name = form.cleaned_data["last_name"]
            data.phone = form.cleaned_data["phone"]
            data.email = form.cleaned_data["email"]
            data.address_line_1 = form.cleaned_data["address_line_1"]
            data.address_line_2 = form.cleaned_data["address_line_2"]
            data.country = form.cleaned_data["country"]
            data.state = form.cleaned_data["state"]
            data.city = form.cleaned_data["city"]
            data.order_note = form.cleaned_data["order_note"]
            data.order_total = grand_total
            data.tax = tax
            data.ip = request.META.get("REMOTE_ADDR")
            data.save()

            # order_number generator
            yr = int(datetime.date.today().strftime("%y"))
            dt = int(datetime.date.today().strftime("%d"))
            mt = int(datetime.date.today().strftime("%m"))
            d = datetime.date(yr, mt, dt)
            current_date = d.strftime("%Y-%m-%d")  # 20210615
            order_number = current_date + str(data.id)  # 20210615+id
            data.order_number = order_number
            data.save()

            order = Order.objects.get(user=current_user, order_number=order_number)

            for item in cart_items:
                orderproduct = OrderProduct()
                orderproduct.order_id = order.id
                # orderproduct.payment = payment
                orderproduct.user_id = request.user.id
                orderproduct.product_id = item.product_id
                orderproduct.quantity = item.quantity
                orderproduct.product_price = item.product.price
                orderproduct.ordered = True
                orderproduct.save()

                # pega as variações de cada produto em CartItem
                cart_item = CartItem.objects.get(id=item.id)
                product_variation = cart_item.variations.all()
                orderproduct = OrderProduct.objects.get(id=orderproduct.id)
                orderproduct.variations.set(product_variation)
                orderproduct.save()
                order.is_ordered = True
                order.save()
                # reduz a quantidade dos produtos vendidos
                product = Product.objects.get(id=item.product_id)
                product.stock -= item.quantity
                product.save()

            # reseta o carrinho
            CartItem.objects.filter(user=request.user).delete()
            ordered_products = OrderProduct.objects.filter(order_id=order.id)
            # envia recibo da ordem para o cliente para o email registrado no cadastro de usuario
            mail_subject = "Thank you with your Order!"
            message = render_to_string(
                "orders/order_received_email.html",
                {
                    "user": request.user,
                    "order": order,
                },
            )

            to_email = request.user.email
            send_email = EmailMultiAlternatives(mail_subject, message, to=[to_email])
            send_email.attach_alternative(message, "text/html")
            send_email.send()
            


            admin_subject = 'New Order Placed'
            admin_message = render_to_string('emails/new_order_notification_two.html', {'order': order})
            admin_email = 'waseemint.pk@gmail.com'
            send_mail(admin_subject, strip_tags(admin_message), None, [admin_email], html_message=admin_message)


            # enviar email para o admin
            # admin_subject = f"New Order Placed: {order_number}"
            # admin_message = f"New Order Placed:\n\nOrder Number: {order_number}\n\nOrder Details:\n\n"
            # for item in ordered_products:
            #     admin_message += f"Product: {item.product.product_name}\nQuantity: {item.quantity}\n\n"
            # admin_message += f"Total Price: {grand_total}\n\n"
            # admin_message += "Customer Information:\n"
            # admin_message += f"Name: {order.first_name} {order.last_name}\n"
            # admin_message += f"Email: {order.email}\n"
            # admin_message += f"Phone: {order.phone}\n"
            # admin_message += f"Address: {order.address_line_1}, {order.address_line_2}, {order.city}, {order.state}, {order.country}\n\n"
            # admin_message += "Order Note: \n"
            # admin_message += f"{order.order_note}\n\n"
            # admin_message += "Thank you.\n"
            
            # mail_admins(admin_subject, admin_message)
            

            context = {
                "order": order,
                "cart_items": cart_items,
                "total": total,
                "tax": tax,
                "grand_total": grand_total,
                "ordered_products": ordered_products,
            }

            return render(request, "orders/order_complete.html", context)
    else:
        return redirect("checkout")







# def place_order(request, total=0, quantity=0):
#     current_user = request.user
#     cart_items = CartItem.objects.filter(user=current_user)
#     cart_count = cart_items.count()
#     if cart_count <= 0:
#         return redirect("store")
#     grand_total = 0
#     tax = 0
#     for cart_item in cart_items:
#         total += cart_item.product.price * cart_item.quantity
#         quantity += cart_item.quantity
#     tax = (2 * total) / 100  # aplicar regra de imposto correta aki
#     grand_total = total + tax
#     if request.method == "POST":
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             # armazena todos os dados da ordem de pagamento em Order
#             data = Order()
#             data.user = current_user
#             data.first_name = form.cleaned_data["first_name"]
#             data.last_name = form.cleaned_data["last_name"]
#             data.phone = form.cleaned_data["phone"]
#             data.email = form.cleaned_data["email"]
#             data.address_line_1 = form.cleaned_data["address_line_1"]
#             data.address_line_2 = form.cleaned_data["address_line_2"]
#             data.country = form.cleaned_data["country"]
#             data.state = form.cleaned_data["state"]
#             data.city = form.cleaned_data["city"]
#             data.order_note = form.cleaned_data["order_note"]
#             data.order_total = grand_total
#             data.tax = tax
#             data.ip = request.META.get("REMOTE_ADDR")
#             data.save()

#             # order_number generator
#             yr = int(datetime.date.today().strftime("%y"))
#             dt = int(datetime.date.today().strftime("%d"))
#             mt = int(datetime.date.today().strftime("%m"))
#             d = datetime.date(yr, mt, dt)
#             current_date = d.strftime("%Y-%m-%d")  # 20210615
#             order_number = current_date + str(data.id)  # 20210615+id
#             data.order_number = order_number
#             data.save()

#             order = Order.objects.get(user=current_user, order_number=order_number)

#             for item in cart_items:
#                 orderproduct = OrderProduct()
#                 orderproduct.order_id = order.id
#                 # orderproduct.payment = payment
#                 orderproduct.user_id = request.user.id
#                 orderproduct.product_id = item.product_id
#                 orderproduct.quantity = item.quantity
#                 orderproduct.product_price = item.product.price
#                 orderproduct.ordered = True
#                 orderproduct.save()

#                 # pega as variações de cada produto em CartItem
#                 cart_item = CartItem.objects.get(id=item.id)
#                 product_variation = cart_item.variations.all()
#                 orderproduct = OrderProduct.objects.get(id=orderproduct.id)
#                 orderproduct.variations.set(product_variation)
#                 orderproduct.save()
#                 order.is_ordered = True
#                 order.save()
#                 # reduz a quantidade dos produtos vendidos
#                 product = Product.objects.get(id=item.product_id)
#                 product.stock -= item.quantity
#                 product.save()

#             # reseta o carrinho
#             CartItem.objects.filter(user=request.user).delete()
#             ordered_products = OrderProduct.objects.filter(order_id=order.id)
#             # envia recibo da ordem para o cliente para o email registrado no cadastro de usuario
#             mail_subject = "Thank you with your Order!"
#             message = render_to_string(
#                 "orders/order_received_email.html",
#                 {
#                     "user": request.user,
#                     "order": order,
#                 },
#             )

#             to_email = request.user.email
#             send_email = EmailMultiAlternatives(mail_subject, message, to=[to_email])
#             send_email.attach_alternative(message, "text/html")
#             send_email.send()
#             context = {
#                 "order": order,
#                 "cart_items": cart_items,
#                 "total": total,
#                 "tax": tax,
#                 "grand_total": grand_total,
#                 "ordered_products": ordered_products,
#             }

#             return render(request, "orders/order_complete.html", context)
#     else:
#         return redirect("checkout")


# def order_complete(request):
#     order_number = request.GET.get("order_number")
#     transID = request.GET.get("payment_id")
#     try:
#         order = Order.objects.get(order_number=order_number, is_ordered=True)
#         ordered_products = OrderProduct.objects.filter(order_id=order.id)
#         subtotal = 0
#         tax = 0
#         grand_total = 0
#         for i in ordered_products:
#             subtotal += i.product_price * i.quantity
#             tax += (2*subtotal)/100
#             grand_total += subtotal + tax
#         payment = Payment.objects.get(payment_id=transID)
#         context = {
#             "order": order,
#             "ordered_products": ordered_products,
#             "order_number": order.order_number,
#             "transID": payment.payment_id,
#             "payment": payment,
#             "subtotal": subtotal,
#             'tax': tax,
#             'grand_total': grand_total,
#         }
#         return render(request, "orders/order_complete.html", context)
#     except (Payment.DoesNotExist, Order.DoesNotExist):
#         return redirect("home")
