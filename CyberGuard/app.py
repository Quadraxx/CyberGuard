from flask import Flask, render_template, request, jsonify
import re
import math
import random
import datetime
import base64

app = Flask(__name__)

# ==========================================
# 💾 VERİTABANI VE SENARYOLAR (DATABASE)
# ==========================================

# 1. OLTALAMA (PHISHING) SENARYOLARI
# (Not: Satır sayısı farkı genelde bu listelerin yazım şeklinden kaynaklanır)
PHISHING_SCENARIOS = [
    {"id": 1, "sender": "Netflix Support <destek@netflix-tr-update.com>", "subject": "Ödeme Reddedildi!", "body": "Hesabınız kapanacak, hemen güncelleyin.", "link": "http://netflix-guvenli.com", "is_phishing": True, "reason": "❌ TUZAK! Link 'http' ile başlıyor ve alan adı sahte."},
    {"id": 2, "sender": "Google <no-reply@accounts.google.com>", "subject": "Güvenlik Uyarısı", "body": "Hesabınıza yeni bir cihazdan giriş yapıldı.", "link": "https://myaccount.google.com", "is_phishing": False, "reason": "✅ GÜVENLİ. Google'ın resmi adresinden gelmiş."},
    {"id": 3, "sender": "IK Departmanı <ik@sirketim.net>", "subject": "Maaş Bordrosu", "body": "Ekteki 'bordro.exe' dosyasını indirin.", "link": "bordro.exe", "is_phishing": True, "reason": "❌ TUZAK! E-posta ile asla '.exe' dosyası indirmeyin."},
    {"id": 4, "sender": "Instagram <security@instagram.com>", "subject": "Giriş Kodu", "body": "Instagram giriş kodunuz: 123 456", "link": "https://instagram.com", "is_phishing": False, "reason": "✅ GÜVENLİ. Resmi Instagram adresinden gelmiş."}
]

# 2. SIZINTI VERİTABANI (SİMÜLASYON)
LEAK_DATABASE = {
    "test@gmail.com": {"source": "Facebook 2019 Sızıntısı", "data": "Şifre, Telefon No", "risk": "YÜKSEK"},
    "admin@sirket.com": {"source": "LinkedIn 2021 Sızıntısı", "data": "E-posta, İş Unvanı", "risk": "ORTA"},
    "huseyin@denizli.com": {"source": "YemekSepeti Benzeri DB", "data": "Adres, Telefon", "risk": "YÜKSEK"},
    "torul@gumushane.edu.tr": {"source": "Kampüs Veri İhlali", "data": "Öğrenci No, Notlar", "risk": "DÜŞÜK"}
}

# ==========================================
# 🌐 SAYFA YÖNLENDİRMELERİ (ROUTING)
# ==========================================

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tool-1-password')
def tool_password():
    return render_template('password.html')

@app.route('/tool-2-phishing')
def tool_phishing():
    return render_template('phishing.html')

@app.route('/tool-3-leak')
def tool_leak():
    return render_template('leak_check.html')

@app.route('/tool-4-crypto')
def tool_crypto():
    return render_template('crypto.html')

@app.route('/tool-5-sqli')
def tool_sqli():
    return render_template('sqli.html')

@app.route('/tool-6-xss')
def tool_xss():
    return render_template('xss.html')

# --- 7. ARAÇ: DİJİTAL PARMAK İZİ ---
@app.route('/tool-7-fingerprint')
def tool_fingerprint():
    # Tarayıcı ve IP bilgisini al
    ua_string = request.user_agent.string
    ip_address = request.remote_addr
    
    # 1. İşletim Sistemi Tespiti (Manuel Kontrol)
    os_name = "Bilinmiyor"
    if "Windows" in ua_string: os_name = "Windows"
    elif "Macintosh" in ua_string: os_name = "MacOS"
    elif "Linux" in ua_string: os_name = "Linux"
    elif "Android" in ua_string: os_name = "Android"
    elif "iPhone" in ua_string or "iPad" in ua_string: os_name = "iOS"

    # 2. Tarayıcı Tespiti (Manuel Kontrol)
    browser_name = "Bilinmiyor"
    if "Edg" in ua_string: browser_name = "Microsoft Edge"
    elif "Chrome" in ua_string: browser_name = "Google Chrome"
    elif "Firefox" in ua_string: browser_name = "Mozilla Firefox"
    elif "Safari" in ua_string: browser_name = "Safari"
    elif "Opera" in ua_string or "OPR" in ua_string: browser_name = "Opera"

    # 3. Dil Temizleme
    language = "Bilinmiyor"
    if request.accept_languages:
        language = request.accept_languages[0]

    info = {
        "ip": ip_address,
        "os": os_name,
        "browser": browser_name,
        "version": request.user_agent.version if request.user_agent.version else "Güncel",
        "language": language,
        "raw_agent": ua_string
    }
    
    return render_template('fingerprint.html', info=info)

# ==========================================
# ⚙️ API ENDPOINTLERİ (BACKEND MANTIĞI)
# ==========================================

# --- 1. ŞİFRE ANALİZİ ---
@app.route('/api/analyze-password', methods=['POST'])
def analyze_password():
    data = request.get_json()
    password = data.get('password', '')
    score = 0
    feedback = []
    
    if len(password) >= 8: score += 20
    else: feedback.append("⚠️ Şifre çok kısa (Min 8 karakter).")
    if re.search(r"[A-Z]", password): score += 20
    else: feedback.append("⚠️ Büyük harf eksik.")
    if re.search(r"[a-z]", password): score += 20
    else: feedback.append("⚠️ Küçük harf eksik.")
    if re.search(r"[0-9]", password): score += 20
    else: feedback.append("⚠️ Rakam eksik.")
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): score += 20
    else: feedback.append("⚠️ Özel karakter eksik.")
    
    return jsonify({'score': score, 'feedback': feedback})

# --- 2. PHISHING OYUNU ---
@app.route('/api/get-phishing-question')
def get_phishing_question():
    return jsonify(random.choice(PHISHING_SCENARIOS))

@app.route('/api/check-phishing-answer', methods=['POST'])
def check_phishing_answer():
    data = request.get_json()
    scenario = next((item for item in PHISHING_SCENARIOS if item["id"] == data.get('id')), None)
    if not scenario: return jsonify({"error": "Hata"}), 404
    is_correct = (scenario["is_phishing"] == data.get('guess'))
    return jsonify({"correct": is_correct, "reason": scenario["reason"]})

# --- 3. SIZINTI KONTROLÜ ---
@app.route('/api/check-leak', methods=['POST'])
def check_leak():
    email = request.get_json().get('email', '').lower()
    if email in LEAK_DATABASE:
        return jsonify({"leaked": True, "info": LEAK_DATABASE[email]})
    else:
        return jsonify({"leaked": False})

# --- 4. KRİPTO LAB ---
@app.route('/api/crypto', methods=['POST'])
def crypto_action():
    data = request.get_json()
    text = data.get('text', '')
    action = data.get('action') 
    method = data.get('method')
    
    result = ""
    if method == 'base64':
        if action == 'encrypt':
            try: result = base64.b64encode(text.encode('utf-8')).decode('utf-8')
            except Exception as e: result = f"Hata: {str(e)}"
        else:
            try: result = base64.b64decode(text.encode('utf-8')).decode('utf-8')
            except: result = "HATA: Geçersiz Base64 formatı!"
    elif method == 'rot13':
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        trans = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
        result = text.translate(str.maketrans(chars, trans))

    return jsonify({'result': result})

# --- 5. SQL INJECTION SİMÜLASYONU ---
@app.route('/api/sqli-login', methods=['POST'])
def sqli_login():
    data = request.get_json()
    username = data.get('username', '')
    password = data.get('password', '')
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    success = False
    message = "Giriş Başarısız: Yanlış bilgiler."
    if username == "admin" and password == "secret123":
        success = True
        message = "Giriş Başarılı: Hoş geldin Admin."
    elif "' OR 1=1" in username or "' OR '1'='1" in username:
        success = True
        message = "⚠️ HACK BAŞARILI! SQL Enjeksiyonu ile sistemi kandırdın."
    return jsonify({"success": success, "message": message, "executed_query": query})

# --- 6. XSS SİMÜLASYONU ---
@app.route('/api/xss-comment', methods=['POST'])
def xss_comment():
    data = request.get_json()
    comment = data.get('comment', '')
    return jsonify({"original_comment": comment, "message": "Yorum eklendi!"})

# ==========================================
# 🚀 BAŞLAT
# ==========================================
if __name__ == '__main__':
    app.run(debug=True)