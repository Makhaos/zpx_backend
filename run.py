import config

app = config.connexion_app
app.add_api('swagger.yml', strict_validation=True)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
