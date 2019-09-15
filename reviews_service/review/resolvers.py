from .models import Review


def resolve_create_review(_, info, input):
    review = Review(content=input.get(
        "content")
    )
    review.save()
    return review


def resolve_get_reviews(*_):
    return [review for review in Review.objects.all()]
