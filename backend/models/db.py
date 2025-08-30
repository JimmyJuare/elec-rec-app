import os
from flask_sqlalchemy import SQLAlchemy

environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")
# Initialize SQLAlchemy
db = SQLAlchemy()

# Optional: helper function for prefixing foreign keys (if needed)
def add_prefix_for_prod(attr):
    if environment == "production":
        return f"{SCHEMA}.{attr}"
    else:
        return attr
