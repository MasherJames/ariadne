from .models import Product


def resolve_create_product(_, info, input):
    product = Product(name=input.get(
        "name"), price=input.get("price"),
        weight=input.get("weight"))
    product.save()
    return product


def resolve_get_products(*_):
    return [product for product in Product.objects.all()]
