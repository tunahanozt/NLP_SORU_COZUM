# 🧮 Gemma-7B Türkçe Matematik Çözücü (Fine-Tuned)

Bu proje, Google'ın **Gemma-7B** modelinin Türkçe matematik problemlerini mantıksal bir silsile ile çözebilmesi için özelleştirilmiş bir çalışmadır. Model, ham metin üretiminden ziyade, problemleri alt basamaklara ayırarak çözen **Chain-of-Thought (CoT)** yeteneği üzerine optimize edilmiştir.

## 🎯 Projenin Amacı

Geleneksel dil modelleri matematiksel sorularda genellikle doğrudan (ve bazen hatalı) sonuçlar üretmektedir. Bu projenin amacı:

  * Modelin işlem önceliği ve mantık zinciri kurmasını sağlamak.
  * Türkçe dil yapısına uygun matematiksel akıl yürütme becerisini geliştirmek.
  * GGUF formatı ile yüksek performansı düşük kaynak tüketimiyle (Edge cihazlar veya Colab) sunmak.

## 🧠 Teknik Mimari ve Eğitim

Model, **Instruction Tuning** yöntemiyle eğitilmiş olup, matematiksel muhakeme yeteneği için özel bir veri seti (GSM8K formatında Türkçe uyarlamalar) kullanılmıştır.

  * **Model Mimarisi:** Gemma-7B (4-bit Quantized)
  * **Yöntem:** Chain-of-Thought (Düşünce Zinciri)
  * **Kuantizasyon:** GGUF (Llama.cpp uyumlu)
  * **Bağlam Penceresi:** 2048 Token

## 📝 Çözüm Formatı (Chain-of-Thought)

Model, bir problemle karşılaştığında aşağıdaki yapısal düzeni takip eder:

1.  **Veri Analizi:** Sorudaki sayısal verileri ve birimleri ayıklar.
2.  **Ara İşlemler:** Adım adım matematiksel formülleri uygular.
3.  **Doğrulama:** Kendi içinde işlemleri kontrol eder (Dahili `<<...>>` belirteçleri ile).
4.  **Final Çıktı:** Sonucu `####` işaretiyle net bir şekilde sunar.

> **Örnek:** "120 TL'den 15 TL'lik elma ve 20 TL'lik muz alımı" gibi bir senaryoda; önce harcamaları ayrı ayrı hesaplar, toplamı bulur ve kalan bakiyeyi en sonda raporlar.

## 🧪 Gözlemler ve Değerlendirme

Modelin gelişimi sırasında yapılan testlerde şu sonuçlar alınmıştır:

  * **Başarı Alanları:** Dört işlem içeren problemler, oran-orantı ve basit maliyet hesaplamaları.
  * **Karakteristik Özellik:** Model, çözüm sırasında eğitim setinden gelen özel belirteçleri (`<< >>`) kullanarak mantıksal tutarlılığı artırmaktadır.
  * **Optimizasyon:** `repeat_penalty` (1.2) ve `temperature` (0.1) ayarları, modelin en tutarlı sonuçları vermesi için ideal parametreler olarak belirlenmiştir.

## 🔗 Model Erişimi

Model dosyalarına ve ağırlıklarına Hugging Face üzerinden ulaşılabilir:
[Hugging Face - Garoz/matematik\_soru\_cozumu](https://www.google.com/search?q=https://huggingface.co/Garoz/matematik_soru_cozumu)

-----