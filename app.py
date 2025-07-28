import os
from flask import Flask, request, jsonify
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

PRODUCTS = {
    "internet-basic": {
        "name": "Plano Basic",
        "description": "Internet 50Mbps",
        "price": 59.99,
        "link": "https://example.com/comprar/internet-basic"
    },
    "internet-premium": {
        "name": "Plano Premium",
        "description": "Internet 200Mbps",
        "price": 99.99,
        "link": "https://example.com/comprar/internet-premium"
    }
}

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')

    system_prompt = "Voce e um bot de vendas de servicos de internet. Responda as duvidas rapidamente e seja objetivo."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ]
    )

    chat_reply = response.choices[0].message['content']

    # simple link detection
    links = []
    for key, product in PRODUCTS.items():
        if product['name'].lower() in message.lower() or key in message.lower():
            links.append(product['link'])
    return jsonify({'reply': chat_reply, 'links': links})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
