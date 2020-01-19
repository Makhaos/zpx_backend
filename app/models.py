from config import db, ma


class Review(db.Model):
    __tablename__ = 'stats_steam_reviews'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.Text)
    review_text = db.Column(db.Text)
    date_updated = db.Column(db.DateTime)
    date_posted = db.Column(db.DateTime)
    recommended = db.Column(db.Integer)


class Event(db.Model):
    __tablename__ = 'stats_steam_events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    steam_appid = db.Column(db.Integer)
    time_stamp = db.Column(db.DateTime)
    type = db.Column(db.Text)


class ReviewSchema(ma.ModelSchema):
    class Meta:
        model = Review
        sqla_session = db.session


class EventSchema(ma.ModelSchema):
    class Meta:
        model = Event
        sqla_session = db.session
