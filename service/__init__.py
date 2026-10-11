from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

app = Flask(__name__)

# Talisman Security Headers
talisman = Talisman(
    app,
    content_security_policy={
        'default-src': "'self'",
        'object-src': "'none'"
    },
    force_https=False
)

# CORS Policy
CORS(app)
