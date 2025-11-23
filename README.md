# 🛡️ CyberGuard: Siber Güvenlik Eğitim Laboratuvarı

**CyberGuard**, siber güvenlik temellerini uygulamalı ve interaktif bir şekilde öğretmek için **Python (Flask)** ile geliştirilmiş kapsamlı bir web platformudur. Amacımız, kullanıcıların hem yaygın saldırı vektörlerini (SQLi, XSS) deneyimlemesini hem de güçlü savunma mekanizmalarını öğrenmesini sağlamaktır.

## ✨ Kilit Özellikler (7 Laboratuvar Aracı)

Proje, kullanıcıların farklı siber güvenlik senaryolarını test edebileceği 7 temel aracı barındırır:

| İkon | Özellik Adı | Açıklama |
| :---: | :--- | :--- |
| 🔑 | **Şifre Analizörü** | Girilen şifrenin karmaşıklığını ve modern araçlarla tahmini kırılma süresini hesaplar. |
| 🎣 | **Phishing Avcısı** | Kullanıcının oltalama (phishing) e-postalarını doğru tespit etme yeteneğini test eden bir eğitim modülü. |
| 🚨 | **Sızıntı Kontrolü** | Bir e-posta adresinin simüle edilmiş (simulated) veri ihlalleri listesinde yer alıp almadığını sorgular. |
| 🕵️‍♂️ | **Kripto Lab** | Base64 ve ROT13 gibi temel şifreleme ve çözme tekniklerini uygulamalı olarak gösterir. |
| 💉 | **SQL Injection (SQLi) Simülasyonu** | Güvenlik açığı bulunan bir giriş panelini kullanarak temel SQL Injection saldırılarının mantığını ve etkilerini öğretir. |
| 🕷️ | **XSS (Cross-Site Scripting) Simülasyonu** | Zararlı istemci taraflı kodun bir web sayfasına nasıl enjekte edildiğini ve tarayıcıda nasıl çalıştığını gösterir. |
| 👣 | **Dijital Parmak İzi** | Kullanıcının tarayıcı, işletim sistemi ve IP adresi gibi dijital ayak izi bilgilerini analiz eder. |

## 🛠️ Kurulum ve Çalıştırma

Bu projeyi yerel makinenizde hızla kurmak ve çalıştırmak için aşağıdaki adımları izleyin.

### Önkoşullar

Projenin çalışması için temel Python ve paket yöneticisi gereklidir:

* **Python 3.8+**
* **pip** (Python paket yöneticisi)

### Adımlar

1.  **Depoyu Klonlayın:**
    Terminalinizi açın ve projeyi GitHub'dan yerel makinenize klonlayın:

    ```bash
    git clone [https://github.com/Quadraxx/CyberGuard.git](https://github.com/Quadraxx/CyberGuard.git)
    cd CyberGuard
    ```

2.  **Gerekli Kütüphaneleri Yükleyin:**
    Projenin temelini oluşturan **Flask** dahil olmak üzere gerekli tüm Python kütüphanelerini yükleyin:

    ```bash
    pip install flask
    # Gerekli tüm kütüphaneler için (eğer bir requirements.txt dosyası varsa):
    # pip install -r requirements.txt
    ```

3.  **Projeyi Başlatın:**
    Flask uygulamasını çalıştırın:

    ```bash
    python app.py
    ```

4.  **Erişim:**
    Tarayıcınızı açın ve uygulamaya erişmek için aşağıdaki adrese gidin:

    ```
    [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
    ```

## 👨‍💻 Geliştirici

Bu proje, siber güvenlik eğitimine katkıda bulunmak amacıyla geliştirilmiştir.

* **Geliştirici:** Hüseyin Akın
* **Kurum:** Torul Meslek Yüksekokulu
