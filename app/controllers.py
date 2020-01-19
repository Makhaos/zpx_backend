import os
import flask
from app.models import Review, ReviewSchema, Event, EventSchema
from sqlalchemy import desc, asc


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


def event_reviews(event_id):
    event_query = Event.query.filter_by(id=event_id).one()
    event_schema = EventSchema()
    event_date = event_schema.dump(event_query)['time_stamp']
    next_event = Event.query.filter(Event.time_stamp >= event_date).order_by(asc(Event.time_stamp)).first()
    next_event_date = event_schema.dump(next_event)['time_stamp']
    return reviews_between_dates(event_date, next_event_date)


def event_vote_amount(event_id):
    pos = 0
    reviews = event_reviews(event_id)
    for review in reviews:
        if review['recommended'] == 1:
            pos = pos + 1
    report_amount = {'Amount of positive votes': pos, 'Amount of negative votes': len(reviews)-pos}
    return flask.jsonify(report_amount)


