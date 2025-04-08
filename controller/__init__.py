from flask import Blueprint

# Create a Blueprint named 'api'
api_bp = Blueprint('api', __name__)

from . import account
from . import webhook