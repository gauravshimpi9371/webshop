from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order  # Import the Order model
from .forms import OrderForm  # Import the Order form

# Home page view to display products
def home_view(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'home/index.html', {'products': products})

# Contact page view
def contact_view(request):
    return render(request, 'home/contact.html')

# Order product view - handles ordering logic
def order_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Get the specific product or return 404 if not found

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)  # Create an order instance but don't save yet
            order.product = product  # Assign the product to the order
            order.save()  # Save the order to the database
            return render(request, 'home/order_success.html', {'name': form.cleaned_data['name']})  # Pass the name to the success page
    else:
        form = OrderForm()

    return render(request, 'home/order_form.html', {'form': form, 'product': product})

# Order success page view
def order_success(request):
    return render(request, 'home/order_success.html')
