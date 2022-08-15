from django.shortcuts import render, redirect

from .forms import OrderForm
from .models import *
from django.db.models import Q
    
    
def product_list(request):
    category=request.GET.get('category')
    brand=request.GET.get('brand')
    categories=Category.objects.all()
    slides=Slide.objects.all()
    brands=Brand.objects.all()
    products=Product.objects.all()
    products=products.filter(category=category) if category else products
    products=products.filter(brand=brand) if brand else products

    product_id=request.GET.get('product')

    if product_id:
        product=Product.objects.get(pk=product_id)
        cart_item=CartItem.objects.filter(product=product)
        if not cart_item:
            cart_item=CartItem.objects.create(customer=request.user, product=product, quantity=1)
            cart_item.save()
            return redirect('product_list')
        for item in cart_item:
            item.quantity += 1
            item.save()

    return render(request, 'product_list.html', {'categories':categories, 'brands':brands, 'products':products, 'slides':slides})






def cart(request):
    cart_items=CartItem.objects.filter(customer=request.user)
    total_price=sum([item.total_price() for item in cart_items])
    total_quantity=sum([item.quantity for item in cart_items])
    return render(request, 'cart.html', {'cart_items':cart_items, 'total_price':total_price, 'total_quantity':total_quantity})





def delete_cart_item(request, pk):
    cart_item=CartItem.objects.get(pk=pk).delete()
    return redirect('cart')




def edit_cart_item(request, pk):
    cart_item=CartItem.objects.get(pk=pk)
    action=request.GET.get('action')

    if action == 'take' and cart_item.quantity > 0:
        if cart_item.quantity == 1:
            cart_item.delete()
            return redirect('cart')
        cart_item.quantity -= 1
        cart_item.save()
        return redirect('cart')
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')





def product_detail(request, pk):
    product=Product.objects.get(pk=pk)
    return render(request, 'product_detail.html', {'product':product})




def create_order(request):
    cart_items=CartItem.objects.filter(customer=request.user)
    total_price=sum([item.total_price() for item in cart_items])
    amout=sum([item.quantity for item in cart_items])
    form = OrderForm()

    if request.method=='POST' and form.is_valid():
        order=Order.objects.create(
            address=request.POST.get('address'),
            phone=request.POST.get('phone'),
            total_price=total_price,
            customer=request.user
        )
        for cart_item in cart_items:
            OrderProduct.objects.create(
                order=order,
                product=cart_item.product,
                amout=cart_item.quantity,
                total=cart_item.total_price(),
            )
        cart_items.delete()
        return redirect('cart')

    return render(request, 'order_creation_page.html', {'cart_items':cart_items, 'total_price':total_price, 'amout':amout, 'form':form})