# BLM101 - Bilgisayar Mühendisliğine Giriş Dönem Projesi

## 🎓 Öğrenci Bilgileri
* **Ad Soyad:** Ahmet Melih Kaya
* **Öğrenci Numarası:** 24360859406
* **Üniversite:** Bursa Teknik Üniversitesi 
* **Bölüm:** Bilgisayar Mühendisliği 

## 📝 Proje Konusu
**2.Grup: Veri Depolama ve Sıkıştırma Algoritmaları** 
Bu proje, metin verilerinin bit düzeyinde temsilini ve veri sıkıştırma mantığını anlamak amacıyla geliştirilen bir **RLE (Run-Length Encoding) Sıkıştırıcı** uygulamasıdır

## 📺 Sunum ve Video Anlatımı
Projenin teorik anlatımını, algoritma mantığını ve kodun çalışma gösterimini içeren YouTube videoma aşağıdaki bağlantıdan ulaşabilirsiniz:
* **YouTube Linki:** 
* **Sunum Dosyası:** Repoda bulunan `sunum.pdf` dosyasından slaytlara ulaşabilirsiniz.

---

## 💻 Proje Açıklaması ve Algoritma Mantığı

### RLE (Run-Length Encoding) Nedir?
Run-Length Encoding, veride birbirini takip eden aynı karakterlerin (ardışık tekrarların) sayılması esasına dayanan, veri boyutunu azaltmaya yarayan temel bir sıkıştırma yöntemidir.

### Kodun Çalışma Mantığı 
Geliştirilen Python programı, yönergede belirtilen "encode" ve "decode" işlemlerini iki ana fonksiyon ile gerçekleştirmektedir:

1.  **Sıkıştırma (rle_encode):** Kullanıcıdan alınan girdi üzerinde bir döngü kurar. Ardışık tekrar eden karakterleri sayar ve "5A3B2C" gibi bir format oluşturur.
2.  **Geri Açma (rle_decode):** Sıkıştırılmış metindeki rakamları `isdigit()` kontrolü ile tespit eder ve karakterleri ilgili sayı kadar tekrar ettirerek veriyi orijinal haline döndürür.
3.  **Sıkıştırma Oranı:** Program, orijinal metin ile sıkıştırılmış metnin uzunluklarını karşılaştırarak sıkıştırma oranını yüzde (%) cinsinden hesaplar. Eğer 100'ün üzerinde bir oran geliyorsa gelen oran kadar büyümüştür.

### Kullanılan Teknolojiler
* **Dil:** Python 
* **Kütüphane:** Herhangi bir harici kütüphane kurulumu gerektirmez (Standart Python özellikleri kullanılmıştır).

---

## 🚀 Kurulum ve Çalıştırma 
1.  Bu repository'yi bilgisayarınıza indirin veya `RLE_code` dosyasındaki kodu kopyalayın.
2.  Python yüklü terminal veya IDE üzerinden `RLE_code.py` dosyasını çalıştırın.
3.  Ekranda çıkan komut satırına sıkıştırmak istediğiniz metni girin.
4.  Program size orijinal metni, sıkıştırılmış sonucu, sıkıştırma yüzdesini ve verinin geri açılmış halini sunacaktır.
