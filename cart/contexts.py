from django.shortcuts import get_object_or_404
from courses.models import Course


def cart_contents(request):
# handles the shopping cart contents
# based on logic as shown in Boutique Ado walkthrough project
    cart_items = []
    total = 0
    counter = 0
    cart = request.session.get('cart', {})

    for item_id, qty in cart.items():
        course = get_object_or_404(Course, pk=item_id)
        total += qty * course.price
        counter += qty
        cart_items.append({
            'item_id': item_id,
            'qty': qty,
            'course': course,
        })


    context = {
        'cart_items' : cart_items,
        'total': total,
        'counter' : counter,
    }

    return context