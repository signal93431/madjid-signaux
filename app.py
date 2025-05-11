from flask import Flask, jsonify
import os
import random
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Serveur de signaux opérationnel'})

@app.route('/signaux')
def get_signaux():
    # Exemples de paires de devises
    paires = ['EUR/USD', 'USD/JPY', 'GBP/USD', 'AUD/USD', 'USD/CAD']
    stratégies = ['FVG détecté', 'Prise de liquidité détectée']

    # Générer un faux signal
    signal = {
        'paire': random.choice(paires),
        'stratégie': random.choice(stratégies),
        'direction': random.choice(['CALL', 'PUT']),
        'timeframe': random.choice(['1min', '5min']),
        'heure': datetime.now().strftime('%H:%M:%S')
    }

    return jsonify(signal)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
