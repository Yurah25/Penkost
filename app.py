from flask import Flask, render_template, request, abort
import os
from datetime import datetime

app = Flask(__name__)

# --- Data Dummy Kost (Lengkap dengan info detail) ---
KOST_DATA = [
    {
        "id": 1, "nama": "Kost Melati Tipe A", "harga": 750000, "tipe_sewa": "bulan",
        "lokasi": "Purbalingga Lor", "foto": "outdoor3.jpg",
        "galeri_foto": ["centro.jpg", "hero.jpeg", "outdoor2.jpg"], # TAMBAHAN
        "fasilitas": ["Isi Lengkap", "Kamar Mandi Dalam", "Wifi"],
        "tipe_kost": "Campur",
        "deskripsi": "Kost nyaman dengan fasilitas lengkap, sangat cocok untuk mahasiswa atau karyawan. Lokasi strategis dekat dengan pusat perbelanjaan dan area perkantoran. Lingkungan aman dan tenang.",
        "whatsapp": "6281234567890",
        "instagram": "kostmelati.pbg",
        "maps_embed_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3956.403920993514!2d109.3664973142756!3d-7.420038975101034!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e65598da2355555%3A0x863375888e2f0332!2sAlun-Alun%20Purbalingga!5e0!3m2!1sid!2sid!4v1626325345123!5m2!1sid!2sid",
        "tanggal_post": datetime(2025, 5, 20)
    },
    {
        "id": 2, "nama": "Kost Mawar Exclusive", "harga": 1200000, "tipe_sewa": "bulan",
        "lokasi": "Pusat Kota", "foto": "kost2.jpg",
        "galeri_foto": ["kost2_view1.jpg", "kost2_view2.jpg", "kost2_view3.jpg"], # TAMBAHAN
        "fasilitas": ["Isi Lengkap", "Kamar Mandi Dalam", "AC", "TV Kabel"],
        "tipe_kost": "Campur",
        "deskripsi": "Kost exclusive di jantung kota Purbalingga. Akses mudah ke mana saja. Dilengkapi dengan AC dan fasilitas modern untuk kenyamanan maksimal Anda.",
        "whatsapp": "6281234567891",
        "instagram": "kostmawar.exclusive",
        "maps_embed_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3956.403920993514!2d109.3664973142756!3d-7.420038975101034!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e65598da2355555%3A0x863375888e2f0332!2sAlun-Alun%20Purbalingga!5e0!3m2!1sid!2sid!4v1626325345123!5m2!1sid!2sid",
        "tanggal_post": datetime(2025, 6, 1)
    },
    {
        "id": 8, "nama": "Kost Putri Anggrek", "harga": 850000, "tipe_sewa": "bulan",
        "lokasi": "Dekat Kampus", "foto": "kost8.jpg",
        "galeri_foto": ["kost8_view1.jpg", "kost8_view2.jpg", "kost8_view3.jpg"], # TAMBAHAN
        "fasilitas": ["Isi Lengkap", "Kamar Mandi Dalam", "AC", "Khusus Putri"],
        "tipe_kost": "Putri",
        "deskripsi": "Kost khusus putri yang aman dan bersih. Berada di lingkungan yang kondusif untuk belajar, hanya 5 menit jalan kaki dari kampus.",
        "whatsapp": "6281234567898",
        "instagram": "kostputri.anggrek",
        "maps_embed_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3956.403920993514!2d109.3664973142756!3d-7.420038975101034!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e65598da2355555%3A0x863375888e2f0332!2sAlun-Alun%20Purbalingga!5e0!3m2!1sid!2sid!4v1626325345123!5m2!1sid!2sid",
        "tanggal_post": datetime(2025, 6, 8)
    },
    {
        "id": 9, "nama": "Kost Putra Gagah", "harga": 800000, "tipe_sewa": "bulan",
        "lokasi": "Dekat GOR", "foto": "kost9.jpg",
        "galeri_foto": ["kost9_view1.jpg", "kost9_view2.jpg", "kost9_view3.jpg"], # TAMBAHAN
        "fasilitas": ["Kamar Mandi Dalam", "Wifi", "Parkir Motor Luas"],
        "tipe_kost": "Putra",
        "deskripsi": "Kost khusus putra yang strategis dekat GOR. Suasana tenang, cocok untuk istirahat. Parkir motor aman dan luas.",
        "whatsapp": "6281234567899",
        "instagram": "kostputra.gagah",
        "maps_embed_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3956.403920993514!2d109.3664973142756!3d-7.420038975101034!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e65598da2355555%3A0x863375888e2f0332!2sAlun-Alun%20Purbalingga!5e0!3m2!1sid!2sid!4v1626325345123!5m2!1sid!2sid",
        "tanggal_post": datetime(2025, 6, 10)
    },
    {
        "id": 10, "nama": "Kost Pak Hendro", "harga": 800000, "tipe_sewa": "bulan",
        "lokasi": "Belakang FT", "foto": "kost10.jpg",
        "galeri_foto": ["kost10_view1.jpg", "kost10_view2.jpg", "kost10_view3.jpg"], # TAMBAHAN
        "fasilitas": ["Kamar Mandi Dalam", "Dapur", "Wifi", "Parkir Motor Luas"],
        "tipe_kost": "Putra",
        "deskripsi": "Kost khusus putra di belakang Fakultas Teknik. Fasilitas memadai dan strategis.",
        "whatsapp": "6281234567910",
        "instagram": "hendrokost_",
        "maps_embed_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3956.3353901048695!2d109.33871669999999!3d-7.428087099999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e655941696aadc9%3A0xc227f7fa81c8ac8e!2sKost%20Pak%20Hendro%20(putra)!5e0!3m2!1sid!2sid!4v1750084636400!5m2!1sid!2sid",
        "tanggal_post": datetime(2025, 6, 16)
    },
    {
        "id": 11, "nama": "Wisma YOLANDAA", "harga": 7500000, "tipe_sewa": "tahun",
        "lokasi": "Desa Blater", "foto": "kost11.jpg",
        "galeri_foto": ["kost11_view1.jpg", "kost11_view2.jpg", "kost11_view3.jpg"], # TAMBAHAN
        "fasilitas": ["Kamar Mandi Luar & Dalam", "Dapur", "Wifi", "Tempat Jemuran", "Parkir Motor Beratap"],
        "tipe_kost": "Putra",
        "deskripsi": "Kost khusus putra yang berjarak 100 meter dari kampus. Bisa ditempuh dengan berjalan kaki ke arah timur.",
        "whatsapp": "6281234567911",
        "instagram": "wisma_yolandaa",
        "maps_embed_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3956.333233949475!2d109.3397938!3d-7.428326599999998!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e6559867d3347b3%3A0x849446a12c94de81!2sWisma%20YOLANDAA!5e0!3m2!1sid!2sid!4v1750084788725!5m2!1sid!2sid",
        "tanggal_post": datetime(2025, 6, 16)
    },
    {
        "id": 12, "nama": "Kost Panorama", "harga": 850000, "tipe_sewa": "bulan",
        "lokasi": "Blater, Kalimanah", "foto": "kost12.jpg",
        "galeri_foto": ["kost12_view1.jpg", "kost12_view2.jpg", "kost12_view3.jpg"], # TAMBAHAN
        "fasilitas": ["Kamar Mandi Dalam", "Lemari Pakaian", "Dapur Umum", "MCB LIstrik Tiap Kamar", "Parkiran Dalam Area"],
        "tipe_kost": "Putra",
        "deskripsi": "Kost putar murah di blater.",
        "whatsapp": "6281234567912",
        "instagram": "kost_panorama",
        "maps_embed_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3956.29528510913!2d109.3394325!3d-7.432540599999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e6559d23a3e365b%3A0x12c9d94faf23ac44!2sKOST%20PANORAMA!5e0!3m2!1sid!2sid!4v1750084957180!5m2!1sid!2sid",
        "tanggal_post": datetime(2025, 6, 16)
    },
    {
        "id": 13, "nama": "Wisma nabil blater Unsoed", "harga": 8000000, "tipe_sewa": "tahun",
        "lokasi": "Blater, Kalimanah", "foto": "kost13.jpg",
        "galeri_foto": ["kost13_view1.jpg", "kost13_view2.jpg", "kost13_view3.jpg"], # TAMBAHAN
        "fasilitas": ["Kamar Mandi Dalam", "Lemari Pakaian", "Dapur Umum", "Wifi", "Parkiran Dalam Area"],
        "tipe_kost": "Putra",
        "deskripsi": "Kost putra yang nyaman dan bersih serta fasilitas lengkap.",
        "whatsapp": "6281234567913",
        "instagram": "wisma.nabil",
        "maps_embed_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3956.296694840015!2d109.34088639999999!3d-7.432384099999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e6559cc9c833ebb%3A0xad27e89fc76b2dbd!2sWisma%20nabil%20blater%20Unsoed!5e0!3m2!1sid!2sid!4v1750085533726!5m2!1sid!2sid",
        "tanggal_post": datetime(2025, 6, 16)
    }
]
def format_rupiah(value):
    return f"Rp {value:,.0f}".replace(",", ".")

app.jinja_env.filters['rupiah'] = format_rupiah

@app.route('/')
def index():
    pilihan_kost = sorted(KOST_DATA, key=lambda x: x['tanggal_post'], reverse=True)[:3]
    return render_template('index.html', pilihan_kost=pilihan_kost)

@app.route('/kost')
def search_kost():
    # Mengambil nilai dari form filter
    sort_by = request.args.get('urutkan', 'terbaru')
    tipe_sewa = request.args.get('tipe_sewa', 'semua')
    tipe_kost = request.args.get('tipe_kost', 'semua') # --- BARU: Ambil filter tipe kost
    wc_dalam = request.args.get('wc_dalam')

    filtered_kosts = list(KOST_DATA)

    # --- DIHAPUS: Filter "include_barang" / Isi Lengkap ---

    # Filter berdasarkan tipe sewa
    if tipe_sewa != 'semua':
        filtered_kosts = [k for k in filtered_kosts if k['tipe_sewa'] == tipe_sewa]

    # --- BARU: Filter berdasarkan tipe kost (Putra/Putri/Campur) ---
    if tipe_kost != 'semua':
        filtered_kosts = [k for k in filtered_kosts if k.get('tipe_kost') == tipe_kost]

    # Filter berdasarkan WC Dalam
    if wc_dalam:
        filtered_kosts = [k for k in filtered_kosts if "Kamar Mandi Dalam" in k['fasilitas']]
    
    # --- DIBERSIHKAN: Menghapus baris 'if putra' dan 'if putri' yang error ---

    # Mengurutkan hasil
    if sort_by == 'termurah':
        filtered_kosts.sort(key=lambda x: x['harga'])
    elif sort_by == 'termahal':
        filtered_kosts.sort(key=lambda x: x['harga'], reverse=True)
    else: # default ke terbaru
        filtered_kosts.sort(key=lambda x: x['tanggal_post'], reverse=True)
        
    return render_template('kost.html', kosts=filtered_kosts, filter_args=request.args)

@app.route('/kost/<int:kost_id>')
def kost_detail(kost_id):
    kost_terpilih = next((kost for kost in KOST_DATA if kost["id"] == kost_id), None)
    if kost_terpilih is None:
        abort(404)
    return render_template('detail_kost.html', kost=kost_terpilih)

@app.route('/tentang')
def about():
    return render_template('tentang.html')

@app.route('/kontak')
def contact():
    return render_template('kontak.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)