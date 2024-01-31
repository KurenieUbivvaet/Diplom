import datetime

from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

from django.core.mail import send_mail


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()

            # Получите адрес электронной почты из формы
            email = form.cleaned_data['email']

            # Определите переменные для отправителя, получателя, темы и текста письма
            subject = f'Заказ № {order.id}'

            product_list = ''
            num = 0
            for item in cart:
                num += 1
                product_list += f'Товар {num}: {item["product"]}\n Цена: {item["price"]} руб., Количество: {item["quantity"]} шт.\n'
            product_list += f"Сумма: {cart.get_total_price()} руб."
            message = f'Здравствуйте, {order.name}\n' \
                f'Ваш заказ № {order.id}\n' \
                f'Список товаров:\n{product_list}'
            from_email = 'smdmisha@yandex.ru'
            to_email = email

            # Отправка письма
            send_mail(subject, message, from_email, [to_email])

            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})