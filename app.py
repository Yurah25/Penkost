from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/home')
def home():
    # Data dummy kamar kos dengan foto
    kamar_list = [
        {"nama": "Centro", "harga": "Rp 1.000.000/bulan", "lokasi": "Boyolali", "foto": "centro.jpg"},
        {"nama": "TengahKota 1", "harga": "Rp 800.000/bulan", "lokasi": "Boyolali", "foto": "tengahkota1.jpg"},
        {"nama": "TengahKota 2", "harga": "Rp 700.000/bulan", "lokasi": "Boyolali", "foto": "tengahkota2.jpg"},
    ]
    return render_template('index.html', kamar_list=kamar_list)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)