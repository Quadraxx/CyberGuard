# 🛡️ CyberGuard: Siber Güvenlik Eğitim Laboratuvarı

## 🌟 Proje Hakkında

**CyberGuard**, siber güvenlik temellerini uygulamalı olarak öğretmeyi amaçlayan interaktif bir web eğitim platformudur. **Python (Flask)** kullanılarak geliştirilen bu sistem, kullanıcıların güvenli kodlama bilincini artırmak amacıyla hem temel saldırı vektörlerini (SQLi, XSS) hem de temel savunma araçlarını deneyimlemesini sağlar.

## 👨‍💻 Geliştirici ve Ortam

* **Geliştirici:** Hüseyin Akın
* **Kurum:** Torul Meslek Yüksekokulu (Torul MYO)
* **Temel Teknoloji:** Python (Flask)
* **Mimari:** İnteraktif Web Uygulaması (Laboratuvar Simülasyonları)

## ✨ Kilit Özellikler ve Öğrenim Alanları (7 Araç)

CyberGuard, öğrencilerin ve yeni başlayanların en kritik siber güvenlik konularını uygulamalı olarak deneyimleyebileceği 7 ayrı laboratuvar aracı sunar.

| İkon | Özellik Adı | Amacı ve Siber Güvenlikteki Rolü | Konu Alanı |
| :---: | :--- | :--- | :--- |
| 🔑 | **Şifre Analizörü** | Kullanıcıların seçtiği şifrenin gücünü ve tahmini kırılma süresini hesaplayarak güvenli şifre bilinci oluşturur. | **Kimlik Doğrulama Güvenliği** |
| 🎣 | **Phishing Avcısı** | Oltalama (Phishing) e-postalarını tespit etme yeteneğini test eden oyun tabanlı bir modül. | **Sosyal Mühendislik / Farkındalık** |
| 🚨 | **Sızıntı Kontrolü** | Bir e-posta adresinin simüle edilmiş veri ihlallerinde yer alıp almadığını kontrol ederek veri güvenliği ciddiyetini gösterir. | **Veri İhlalleri Yönetimi** |
| 🕵️‍♂️ | **Kripto Lab** | Base64 ve ROT13 gibi temel şifreleme/çözme mekanizmalarını uygulamalı olarak gösterir. | **Temel Kriptografi** |
| 💉 | **SQL Injection (SQLi) Simülasyonu** | Güvenlik açığı bulunan bir giriş panelini kullanarak SQLi saldırılarının mantığını ve nasıl önleneceğini öğretir. | **Web Uygulama Güvenliği (Zafiyet)** |
| 🕷️ | **XSS (Cross-Site Scripting) Simülasyonu** | Zararlı istemci tarafı kodun bir web sitesine nasıl enjekte edildiğini ve tarayıcıda kullanıcıya nasıl zarar verdiğini gösterir. | **Web Uygulama Güvenliği (Zafiyet)** |
| 👣 | **Dijital Parmak İzi** | Kullanıcının IP adresi, işletim sistemi ve tarayıcı bilgileri gibi internette bıraktığı izleri analiz eder. | **Bilgi Toplama (Reconnaissance)** |



## 🛠️ Kurulum ve Çalıştırma

Bu projeyi yerel makinenizde hızla kurmak ve çalıştırmak için aşağıdaki adımları sırasıyla izleyin.

### A. Önkoşullar

Projenin çalışması için temel Python ortamı gereklidir:

* **Python 3.8+**
* **pip** (Python paket yöneticisi)
* **git** (Depoyu klonlamak için)

### B. Kurulum Adımları

1.  **Depoyu Klonlayın:**
    Terminalinizi açın ve projeyi GitHub'dan yerel makinenize indirin:

    ```bash
    git clone [https://github.com/Quadraxx/CyberGuard.git](https://github.com/Quadraxx/CyberGuard.git)
    cd CyberGuard
    ```

2.  **Gerekli Kütüphaneleri Yükleyin:**
    Projenin temelini oluşturan **Flask** framework'ünü yükleyin:

    ```bash
    pip install flask
    ```
    *(Not: Projenin başka özel bağımlılıkları varsa, genellikle bu adımda `pip install -r requirements.txt` komutu kullanılır.)*

### C. Uygulamayı Başlatma

Flask uygulamasını yerel sunucunuzda çalıştırın:

```bash
python app.py
