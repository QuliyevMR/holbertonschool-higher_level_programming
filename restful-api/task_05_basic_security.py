#!/usr/bin/python3
"""
Bu modul Flask ilə API təhlükəsizliyini təmin etmək üçün
Basic Auth və JWT (JSON Web Tokens) mexanizmlərini tətbiq edir.
"""
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, get_jwt_identity, jwt_required
)

app = Flask(__name__)

# JWT üçün gizli açar (Real layihələrdə bu gizli saxlanılır)
app.config['JWT_SECRET_KEY'] = 'gizli_ve_tehlukesiz_acar_123'

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# İstifadəçilər və onların şifrələnmiş (hashed) parolları
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# ==========================================
# 1. BASIC AUTHENTICATION (Əsas Doğrulama)
# ==========================================

@auth.verify_password
def verify_password(username, password):
    """Basic Auth üçün istifadəçi adı və şifrəni yoxlayır."""
    user = users.get(username)
    # Əgər istifadəçi varsa və göndərilən şifrə hash ilə uyğun gəlirsə
    if user and check_password_hash(user['password'], password):
        return username
    return None

@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Yalnız Basic Auth ilə girişi olanlar üçün."""
    return "Basic Auth: Access Granted"


# ==========================================
# 2. JWT AUTHENTICATION (Token ilə Doğrulama)
# ==========================================

@app.route("/login", methods=["POST"])
def login():
    """
    İstifadəçi adı və şifrəni yoxlayır, uğurlu olarsa JWT Token qaytarır.
    """
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    user = users.get(username)
    
    # Şifrə düzgündürsə, token yaradırıq
    if user and check_password_hash(user['password'], password):
        # Token-in içinə istifadəçi adını və rolunu (payload) yerləşdiririk
        access_token = create_access_token(identity={
            "username": username,
            "role": user["role"]
        })
        return jsonify(access_token=access_token), 200

    # Məlumatlar səhvdirsə
    return jsonify({"error": "Invalid username or password"}), 401


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """Yalnız düzgün JWT Token-ə sahib olanlar bura daxil ola bilər."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Yalnız admin roluna sahib olanlar bura daxil ola bilər."""
    # get_jwt_identity() bizə token yaradarkən içinə qoyduğumuz obyekti qaytarır
    current_user = get_jwt_identity()
    
    if current_user.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
        
    return "Admin Access: Granted"


# ==========================================
# 3. JWT XƏTA İDARƏETMƏSİ (Custom Error Handlers)
# ==========================================
# Şərtdə tələb olunduğu kimi, bütün avtorizasiya xətaları 401 qaytarmalıdır.

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
