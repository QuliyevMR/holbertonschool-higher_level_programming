#!/usr/bin/python3
"""
Bu modul Flask framework-ü istifadə edərək sadə bir API qurur.
"""
from flask import Flask, jsonify, request

# Flask tətbiqini (app) yaradırıq
app = Flask(__name__)

# İstifadəçi məlumatlarını yaddaşda saxlamaq üçün boş lüğət (dictionary)
users = {}


@app.route("/")
def home():
    """
    Ana səhifə (root) endpoint-i.
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """
    Yaddaşda olan bütün istifadəçi adlarının (username) siyahısını
    JSON formatında qaytarır.
    """
    # Lüğətin sadəcə açarlarını (keys) alıb siyahıya çeviririk
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """
    API-nin vəziyyətini yoxlamaq üçün endpoint.
    """
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """
    Dinamik route: Verilən username-ə uyğun istifadəçi məlumatlarını qaytarır.
    İstifadəçi tapılmazsa, 404 xətası qaytarır.
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    POST sorğusu ilə yeni istifadəçi əlavə edir.
    Gələn JSON məlumatını yoxlayır və xətaları idarə edir.
    """
    # Gələn JSON datasını oxuyuruq (xəta olarsa, serverin çökməməsi üçün silent=True)
    parsed_data = request.get_json(silent=True)

    # 1. JSON valid (düzgün) deyilsə
    if parsed_data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = parsed_data.get("username")

    # 2. Username parametri göndərilməyibsə
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # 3. Bu username artıq bazada (luğətdə) mövcuddursa
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # 4. Hər şey qaydasındadırsa, istifadəçini lüğətə əlavə edirik
    users[username] = parsed_data

    # Uğurlu əməliyyat (201 Created) cavabını qaytarırıq
    return jsonify({
        "message": "User added",
        "user": parsed_data
    }), 201


if __name__ == "__main__":
    # Serveri işə salırıq
    app.run()
