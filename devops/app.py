from flask import Flask , request


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return "OK", 200


@app.route('/health', methods = ['GET'])
def health():
    return "OK", 200

@app.route('/webhook', methods = ['POST'])
def webhook():
    print(request.data)
    return "OK", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
