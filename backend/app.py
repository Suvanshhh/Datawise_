from flask import Flask
from flasgger import Swagger
from routes.datasets import datasets_bp
from routes.quality_logs import quality_logs_bp
from dotenv import load_dotenv
from flask_cors import CORS

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Enable CORS for all routes (important for React/JS frontend)
CORS(app)

# Enable Swagger UI for API documentation
swagger = Swagger(app)

# Register blueprints for modular route handling
app.register_blueprint(datasets_bp)
app.register_blueprint(quality_logs_bp)

if __name__ == "__main__":
    app.run()
