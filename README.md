# 🔍 DNS Resolver Tool

**DNS Resolver Tool**, Python tabanlı, hafif ve hızlı bir DNS kayıt sorgulama aracıdır. Bu araç; sızma testi süreçlerinde bilgi toplama (reconnaissance) aşamasını hızlandırmak veya ağ yapılandırmalarını kontrol etmek amacıyla geliştirilmiştir.

## ✨ Öne Çıkan Özellikler

* **Çoklu Kayıt Analizi:** Tek bir sorgu ile `A`, `AAAA`, `MX`, `NS`, `TXT` ve `CNAME` kayıtlarını analiz eder.
* **Görselleştirilmiş Çıktı:** `colorama` kütüphanesi sayesinde sonuçları, uyarıları ve hataları terminal üzerinden renk kodlarıyla sunar.
* **Hata Yönetimi:** Mevcut olmayan alan adları veya boş kayıtlar için kullanıcıyı bilgilendiren gelişmiş hata yakalama mekanizmasına sahiptir.
* **Hız:** `dnspython` kütüphanesini kullanarak hızlı ve etkili sorgulama yapar.

## 🛠️ Kurulum

Aracı çalıştırmak için sisteminizde Python 3.x yüklü olmalıdır.

1.  **Depoyu Klonlayın:**
```bash
git clone [https://github.com/kullaniciadi/dns-resolver-tool.git](https://github.com/kullaniciadi/dns-resolver-tool.git)
cd dns-resolver-tool
```
2.  **Bağımlılıkları Yükleyin:**
```bash
pip install dnspython colorama
```
## 🚀 Kullanım

```bash
python dns_resolver.py
```
Program başladığında sizden hedef alan adını girmenizi isteyecektir (Örn: google.com).

## 📊 DNS Kayıtları Hakkında Bilgi

A: Alan adının IPv4 adresini gösterir.

AAAA: Alan adının IPv6 adresini gösterir.

MX: E-posta sunucusu yönlendirme kayıtlarını listeler.

NS: Alan adının yetkili isim sunucularını belirtir.

TXT: Doğrulama ve güvenlik kayıtlarını (SPF, DKIM vb.) içerir.

## 📸 Örnek Çıktı

Aracı çalıştırdığınızda aşağıdaki gibi bir analiz raporu alırsınız:
```text
--- google.com için DNS Kayıtları Sorgulanıyor ---

[+] A Kayıtları:
   - 142.250.184.238
[+] MX Kayıtları:
   - 10 smtp.google.com.
[+] NS Kayıtları:
   - ns1.google.com.
   - ns2.google.com.
[!] CNAME kaydı bulunamadı.
```

## 👨‍💻 Geliştirici
GitHub: [arsoybilal](https://github.com/arsoybilal)

LinkedIn: https://www.linkedin.com/in/bilalarsoy

## ⚖️ Yasal Uyarı (Disclaimer)

Bu araç sadece eğitim ve etik siber güvenlik testleri amacıyla geliştirilmiştir. Aracın izinsiz sistemler üzerinde kullanılmasından doğabilecek tüm hukuki sorumluluk son kullanıcıya aittir. Geliştirici, kötüye kullanım durumunda hiçbir sorumluluk kabul etmez.

## 📜 Lisans

Bu proje MIT Lisansı ile korunmaktadır. Detaylar için LICENSE dosyasına göz atabilirsiniz.