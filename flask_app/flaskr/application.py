from flask_cors import CORS
from flaskr import create_app


application = create_app('production')
cors = CORS(application)
