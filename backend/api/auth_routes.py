import datetime as dt
import jwt
from flask import Blueprint, jsonify, request, current_app as app
from ..models.db import db
from ..models.user import User
from ..models.license import License
from ..forms.auth_forms import RegisterForm, LoginForm, LicenseForm

auth_routes = Blueprint('auth', __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Turns WTForms validation errors into a simple list
    """
    error_messages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            error_messages.append(f"{field}: {error}")
    return error_messages


@auth_routes.route("/")
def authenticate():
    """
    Dummy route to check authentication if you want to extend to Flask-Login later
    For now, just returns a message
    """
    return {"message": "Auth API is working"}


@auth_routes.route("/register", methods=["POST"])
def register():
    """
    Registers a new user
    """
    form = RegisterForm(data=request.get_json())
    if not form.validate():
        return {"errors": validation_errors_to_error_messages(form.errors)}, 400

    if User.query.filter_by(email=form.email.data).first():
        return {"errors": ["Email already registered"]}, 409

    user = User(email=form.email.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
    return {"ok": True}


@auth_routes.route("/login", methods=["POST"])
def login():
    """
    Logs a user in and returns a JWT
    """
    form = LoginForm(data=request.get_json())
    if not form.validate():
        return {"errors": validation_errors_to_error_messages(form.errors)}, 400

    user = User.query.filter_by(email=form.email.data).first()
    if not user or not user.check_password(form.password.data):
        return {"errors": ["Invalid credentials"]}, 401

    payload = {
        "sub": user.id,
        "email": user.email,
        "exp": dt.datetime.utcnow() + dt.timedelta(days=app.config.get("TOKEN_DAYS", 7))
    }
    token = jwt.encode(payload, app.config["SECRET_KEY"], algorithm="HS256")
    return {"token": token}


@auth_routes.route("/validate-license", methods=["POST"])
def validate_license():
    """
    Validates a license key for a given email
    """
    form = LicenseForm(data=request.get_json())
    if not form.validate():
        return {"errors": validation_errors_to_error_messages(form.errors)}, 400

    lic = License.query.filter_by(
        email=form.email.data,
        license_key=form.license_key.data,
        active=True
    ).first()
    return {"valid": bool(lic)}
