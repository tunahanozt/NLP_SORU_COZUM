import torch
import re
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

# Kendi Hugging Face deponun adını buraya yaz
ADAPTER_REPO = "Garoz/gemma-NLP_SORU_COZUM_TUNA"
BASE_MODEL = "google/gemma-7b"

def temizle(metin):
    # Modelin ürettiği << >> ve #### işaretlerini temizler
    return re.sub(r'<<.*?>>|####\s*', '', metin).strip()

print("1. Taban model ve tokenizer yükleniyor (Bu biraz sürebilir)...")
tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)
base_model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL,
    device_map="auto",
    torch_dtype=torch.float16 # Test için float16 yeterlidir
)

print("2. Sizin eğittiğiniz matematik adaptörü yükleniyor...")
model = PeftModel.from_pretrained(base_model, ADAPTER_REPO)
model.eval()

# Test Sorusu
soru = "Bir çiftlikte 5 inek ve 3 tavuk vardır. Bu hayvanların ayaklarının toplam sayısı kaçtır?"
prompt = f"Aşağıdaki matematik problemini adım adım düşünerek çöz.\n\nSoru: {soru}\n\nÇözüm:"

inputs = tokenizer(prompt, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")

print("3. Model problemi çözüyor...\n")
print("=" * 60)

with torch.no_grad():
    outputs = model.generate(
        **inputs, 
        max_new_tokens=200,
        temperature=0.1,
        top_p=0.95,
        repetition_penalty=1.0,
        do_sample=True
    )

# Sadece modelin yeni ürettiği kısmı alıyoruz
uretilen_tokenler = outputs[0][inputs['input_ids'].shape[1]:]
ham_cevap = tokenizer.decode(uretilen_tokenler, skip_special_tokens=True)

# Çıktıyı temizle ve yazdır
temiz_cevap = temizle(ham_cevap)
print(temiz_cevap)
print("=" * 60)