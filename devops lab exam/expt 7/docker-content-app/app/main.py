from flask import Flask, request, jsonify

app = Flask(__name__)
content_store = []

@app.route('/content', methods=['GET', 'POST'])
def manage_content():
    if request.method == 'POST':
        content = request.json.get('content')
        content_store.append(content)
        return jsonify({"message": "Content added", "content": content}), 201
    return jsonify(content_store)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
