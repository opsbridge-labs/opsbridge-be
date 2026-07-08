from flask import Blueprint, jsonify, request
from app.services.auth_service import AuthService

bp = Blueprint("auth_controller", __name__, url_prefix="/api/auth")

@bp.post("/login")
def login():
    payload = request.get_json(silent=True) or {}
    return jsonify(AuthService().login(payload.get("email", "demo@example.com")))
