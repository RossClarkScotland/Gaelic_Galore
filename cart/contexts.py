

def cart_contents(request):
# handles the shopping cart contents
    cart_items = []
    total = 0
    counter = 0

    context = {
        'cart_items' : cart_items,
        'total': total,
        'counter' : counter,
    }

    return context