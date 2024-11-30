# DSA210
# DSA210 project
# Yemeksepeti Sipariş Analizi Projesi

## **Motivasyon**
Yemek alışkanlıklarımı ve finansal farkındalığımı artırmak amacıyla Yemeksepeti geçmiş sipariş verilerimi analiz etmeye karar verdim. Bu projede, kupon kullanımımın etkisini anlamak, yemek siparişi verme alışkanlıklarımı tespit etmek ve yemek yapmanın olası tasarruf potansiyelini incelemek istiyorum. Ayrıca, zamanla sipariş trendlerini analiz ederek uzun vadeli davranışlarım hakkında öngörülerde bulunmayı hedefliyorum.

---

## **Veri Kaynağı**
Bu proje tamamen kendi geçmiş Yemeksepeti sipariş verilerimden oluşmaktadır. Veriyi, Yemeksepeti hesabımdan manuel olarak indirip düzenleyeceğim. Siparişlerimin tarih, saat, maliyet, kullanılan kuponlar ve sipariş içeriği gibi detaylarını içermektedir. Ayrıca, yemek yapma maliyetlerini karşılaştırmak için çeşitli tariflerden malzeme fiyatlarını manuel olarak topladım.

---

## **Projede Kullanılan Teknikler**

### **1. Keşifsel Veri Analizi (EDA)**

#### Amaç:
- Veriyi anlamak, temizlemek ve ilk bulguları ortaya koymak.
- Aşağıdaki sorulara yanıt aramak:
  - Hangi saatlerde daha çok sipariş veriyorum?
  - Kuponlar hangi durumlarda daha çok kullanılıyor?
  - Sipariş maliyetlerim ne düzeyde?

#### Kullanılan Araçlar:
- **Pandas**: Veri temizleme ve manipülasyon işlemleri için.
- **Matplotlib ve Seaborn**: Sipariş saatleri, kupon kullanımı ve maliyetlerin görselleştirilmesi.

#### Örnek Analizler:
- Saatlere göre sipariş yoğunluklarını çubuk grafikle göstermek.
- Kupon kullanımının sipariş maliyetlerine etkisini kutu grafiği (box plot) ile görselleştirmek.

---

### **2. Kupon Analizi**
#### Amaç:
- Kupon kullanımıyla maliyetlerin nasıl değiştiğini anlamak.
- Hangi durumlarda kupon kullanımının maksimum fayda sağladığını belirlemek.

#### Kullanılan Modeller:
- **Birliktelik Kuralı Madenciliği (Association Rule Mining)**:
  - Kupon kullanımı ile yemek kategorileri arasındaki ilişkiyi tespit etmek.
- **Lojistik Regresyon**:
  - Kupon kullanımını etkileyen faktörleri modellemek.

---

### **3. Yemek Yapmanın Tasarruf Analizi**
#### Amaç:
- Evde yemek yapmanın siparişlere kıyasla sağlayacağı tasarrufu tahmin etmek.
- Yemek yapmanın maliyetini, siparişlerin toplam maliyetleriyle karşılaştırmak.

#### Kullanılan Araçlar:
- **Veri Toplama**: Tarif bazlı malzeme maliyetlerini manuel olarak derlemek.
- **Karşılaştırmalı Analiz**:
  - Yemek tariflerinin maliyeti ile sipariş maliyetini yan yana analiz etmek.
- **Zaman ve Tasarruf Modeli**:
  - Evde yemek yapmanın zaman ve tasarruf açısından avantajlarını hesaplamak.

---

### **4. Saatlik Sipariş Analizi**
#### Amaç:
- Siparişlerin saatlik dağılımını analiz ederek, belirli saat dilimlerindeki davranışlarımı tespit etmek.
- En sık sipariş verilen saat dilimlerini bulmak.

#### Kullanılan Teknikler:
- **Zaman Serisi Analizi**:
  - Belirli saatlerdeki sipariş yoğunluklarını anlamak için.
- **Görselleştirme**:
  - Çizgi grafikleriyle saat bazlı sipariş eğilimlerini göstermek.

---

### **5. Trend Analizi**
#### Amaç:
- Zaman içerisindeki sipariş alışkanlıklarımı ve harcamalarımı analiz etmek.
- Mevsimsel, aylık veya haftalık değişiklikleri tespit etmek.

#### Kullanılan Modeller:
- **Zaman Serisi Modelleri (ARIMA, Prophet)**:
  - Sipariş trendlerini tahmin etmek.
- **Regresyon Analizi**:
  - Maliyetlerin zamanla nasıl değiştiğini modellemek.

---

## **Projenin Bulgu ve Sonuçları**
1. Kupon kullanımının hangi yemek kategorilerinde ve ne tür siparişlerde en etkili olduğunu öğrendim.
2. Yemek yaparak siparişlere kıyasla belirli bir tasarruf oranına ulaşabileceğimi hesapladım.
3. Siparişlerimin genellikle hafta içi akşam saatlerinde yoğunlaştığını ve bu saatlerde kupon kullanma eğilimimin arttığını gözlemledim.
4. Zamanla artan harcama alışkanlıklarımı fark ederek, daha planlı bir yemek bütçesi oluşturmayı planlıyorum.

---

## **Kısıtlamalar ve Gelecek Çalışmalar**
- Verinin sınırlılığı: Daha fazla veri toplayarak modelleme işlemlerimi geliştirebilirim.
- Yemek tarifleri için daha kesin maliyetler toplanabilir.
- Gelecekte bir öneri sistemi geliştirerek, hangi yemeklerin hangi saatlerde daha uygun olabileceğini önermeyi planlıyorum.

---
