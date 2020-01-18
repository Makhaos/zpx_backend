from flask import render_template
import config

app = config.connexion_app
app.add_api('swagger.yml')


# models.py, functions on app? maybe use Api, config.py, run.py combine with run.py, from flask_restful import Api seems good and simple


@app.route('/')
def route():
    # print("Total number of games:", Games.query.count())
    # print(datetime(2017, 6, 5, 10, 20, 11))
    # # print("Reviews list between dates:", Reviews.query.filter(
    # #     Reviews.date_posted.between(datetime(2017, 6, 5, 10, 20, 11), datetime(2018, 6, 5, 10, 20, 11))).all())
    # return jsonify(Games.query.count())
    return render_template('sample.html')


# reviews_schema = ReviewSchema(many=True)
# review_schema = ReviewSchema()


# GET GET /users?sort_by=desc(last_modified),asc(email)

# @app.route('/reviews')
# def reviews():
#     item = request.args.get('order_by', 'date_posted')
#     oldest = Review.query.order_by(desc(item)).limit(50)
#     oldest = reviews_schema.dump(oldest)
#     return jsonify(oldest)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
