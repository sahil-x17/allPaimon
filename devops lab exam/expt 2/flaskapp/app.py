from flask import Flask, render_template, request

app = Flask(__name__)

# In-memory list to store registrations
registrations = []

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        registrations.append({'name': name, 'email': email})
        return f'Thank you {name}, you have registered successfully!'
    return render_template('register.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
