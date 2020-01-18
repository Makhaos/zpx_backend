from app.models import Review, ReviewSchema
from sqlalchemy import desc


def reviews_list():
    reviews = Review.query.order_by(desc(Review.date_posted)).limit(1)
    reviews_schema = ReviewSchema(many=True)
    return reviews_schema.dump(reviews)
