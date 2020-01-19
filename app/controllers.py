import os
import flask
from app.models import Review, ReviewSchema
from sqlalchemy import desc


def sample():
    templates_path = os.path.join('app', 'templates')
    return flask.send_from_directory(templates_path, 'sample.html')


def reviews_list(limit, offset):
    reviews = Review.query.order_by(desc(Review.date_updated), desc(Review.date_posted)).paginate(per_page=limit,
                                                                                                  page=offset,
                                                                                                  error_out=True)
    reviews_schema = ReviewSchema(many=True)
    return reviews_schema.dump(reviews.items)


def reviews_between_dates(start_date, end_date):
    reviews = Review.query.filter(Review.date_updated.between(start_date, end_date),
                                  Review.date_posted.between(start_date, end_date)).order_by(desc(Review.date_updated),
                                                                                             desc(Review.date_posted))
    reviews_schema = ReviewSchema(many=True)
    return reviews_schema.dump(reviews)

