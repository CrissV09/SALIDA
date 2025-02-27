import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def invitacion():
    return render_template('invitacion.html')

@app.route('/gracias')
def gracias():
    return render_template('gracias.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
