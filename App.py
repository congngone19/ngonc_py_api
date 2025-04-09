from flask import Flask
from controller import api_bp  # Import Blueprint
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
jwt = JWTManager(app)
# Register the API Blueprint
app.register_blueprint(api_bp, url_prefix="/api")

if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=5000)
    app.run(debug=True)