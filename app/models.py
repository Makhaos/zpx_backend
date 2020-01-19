from config import db, ma
from marshmallow import fields


# class Games(db.Model):
#     __tablename__ = 'stats_steam_games'
#     # __table_args__ = {'extend_existing': True}
#     steam_appid = db.Column(db.Integer, primary_key=True)
#
#
class Review(db.Model):
    __tablename__ = 'stats_steam_reviews'
    id = db.Column(db.Integer, primary_key=True)
    steam_appid = db.Column(db.Integer)
    user_name = db.Column(db.Text)
    review_text = db.Column(db.Text)
    date_updated = db.Column(db.DateTime)
    date_posted = db.Column(db.DateTime)


class ReviewSchema(ma.ModelSchema):
    class Meta:
        model = Review
        sqla_session = db.session
    # id = fields.Integer()
    # steam_appid = fields.Integer()
    # user_name = fields.String()
    # review_text = fields.String()
    # date_posted = fields.DateTime()
    # date_updated = fields.DateTime()
