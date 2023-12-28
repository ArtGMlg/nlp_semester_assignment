from Model import Model

from flask import Flask, request, jsonify

app = Flask(__name__, static_url_path='')

model = Model()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    text = data['text']
    
    print('Text:', text)
    
    result = model.conv(text)
    
    print('Result:', result)
    
    return jsonify({
        'answer': result
    })
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)