from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

def fourier_series(x, n_terms):
    # Define your Fourier series function here
    # For example, a square wave Fourier series
    f = 0
    for n in range(1, n_terms + 1):
        if n % 2 != 0:
            f += (4 / (np.pi * n)) * np.sin(2 * np.pi * n * x)
    return f

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot', methods=['POST'])
def plot():
    n_terms = int(request.form['n_terms'])
    x_values = np.linspace(0, 2 * np.pi, 1000)
    y_values = fourier_series(x_values, n_terms)

    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_values, label=f'Fourier Series (N={n_terms})')
    plt.legend()
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Fourier Series Graph')

    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    return f'<img src="data:image/png;base64,{plot_url}" />'

if __name__ == '__main__':
    app.run(debug=True)
