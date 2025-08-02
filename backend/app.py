# app.py üçün test ünvanı əlavə edilmiş son versiya

from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from flask_cors import CORS

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"İstifadə ediləcək cihaz: {device}")

app = Flask(__name__)
CORS(app)

# --- YENİ: Sağlamlıq Yoxlaması Ünvanı ---
@app.route("/")
def health_check():
    return "Salam, Neural Sonata Backend-i işləyir!"
# -----------------------------------------

print("CPU üçün uyğun model yüklənir...")
model_name = "gpt2-medium" 
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
print(f"'{model_name}' modeli uğurla '{device}' cihazına yükləndi!")


@app.route("/generate", methods=["POST"])
def generate_sonata():
    # ... (bu funksiya olduğu kimi qalır) ...
    try:
        data = request.get_json()
        input_text = data["text"]
        if not input_text:
            return jsonify({"error": "Mətn boş ola bilməz"}), 400
    except Exception as e:
        return jsonify({"error": f"JSON datası ilə bağlı problem: {e}"}), 400
        
    inputs = tokenizer(input_text, return_tensors="pt")
    
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits[0, -1, :]

    probabilities = torch.nn.functional.softmax(logits, dim=-1)
    top_k_probabilities, top_k_indices = torch.topk(probabilities, 10)

    results = []
    for i in range(len(top_k_indices)):
        token_id = top_k_indices[i]
        prob = top_k_probabilities[i]
        word = tokenizer.decode(token_id)
        results.append({"word": word.strip(), "probability": prob.item()})
        
    return jsonify(results)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7860)
