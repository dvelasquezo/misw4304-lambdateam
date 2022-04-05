from flask_cors import CORS
from flaskr import create_app


app = create_app('production')
cors = CORS(app)
