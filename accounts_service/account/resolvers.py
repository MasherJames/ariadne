from .models import User


def resolve_create_user(_, info, input):
    user = User(firstname=input.get(
        "firstname"), lastname=input.get("lastname"))
    user.save()
    return user


def resolve_get_users(*_):
    return [user for user in User.objects.all()]
