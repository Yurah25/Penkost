from flask import Flask, render_template, request, abort
import os
from datetime import datetime

app = Flask(__name__)

KOST_DATA = [
    {
        "id": 10, "nama": "Kost Pak Hendro", "harga": 800000, "tipe_sewa": "bulan",
        "lokasi": "Belakang FT", "foto": "kost10.jpg",
        "galeri_foto": ["kost10_view1.jpg", "kost10_view2.jpg", "kost10_view3.jpg"],
        "fasilitas": ["Kamar Mandi Dalam", "Dapur", "Wifi", "Parkir Motor Luas"],
        "tipe_kost": "Putra",
        "deskripsi": "Kost khusus putra di belakang Fakultas Teknik. Fasilitas memadai dan strategis.",
        "whatsapp": "62881024501933",
        "instagram": "penkost_pbg",
        "maps_embed_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3956.3353901048695!2d109.33871669999999!3d-7.428087099999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e655941696aadc9%3A0xc227f7fa81c8ac8e!2sKost%20Pak%20Hendro%20(putra)!5e0!3m2!1sid!2sid!4v1750084636400!5m2!1sid!2sid",
        "tanggal_post": datetime(2025, 6, 16)
    },
    {
        "id": 16, 
        "nama": "Kost Putri Wisma Damai 2", 
        "harga": 7000000, 
        "tipe_sewa": "tahun",
        "lokasi": "Karangwangkal, Purwokerto", 
        "foto": "kost16.jpg",
        "galeri_foto": ["kost16_view1.jpg", "kost16_view2.jpg", "kost16_view3.jpg"],
        "fasilitas": ["Kamar Mandi Dalam", "Wifi", "Dapur Umum", "Parkir Motor"],
        "tipe_kost": "Putri",
        "deskripsi": "Kost khusus putri yang nyaman dan strategis di area Karangwangkal. Dekat dengan berbagai fasilitas umum dan universitas.",
        "whatsapp": "62881024501933",
        "instagram": "penkost_pbg",
        "maps_embed_url":"https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d940.1434643786871!2d109.3386997!3d-7.4287128!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e6559002c706615%3A0xd5d01ea002de4064!2sKost%20Putri%20Wisma%20Damai%202!5e1!3m2!1sid!2sid!4v1750141037166!5m2!1sid!2sid",
        "tanggal_post": datetime(2025, 6, 17)
    },
    {
        "id": 17, 
        "nama": "WISMA ALDEN", 
        "harga": 480000, 
        "tipe_sewa": "bulan",
        "lokasi": "Grendeng, Purwokerto", 
        "foto": "kost17.jpg",
        "galeri_foto": ["kost17_view1.jpg", "kost17_view2.jpg"],
        "fasilitas": ["Kamar Mandi Luar", "Dapur Umum", "Wifi", "Parkir Motor"],
        "tipe_kost": "Putra",
        "deskripsi": "Kost putra dengan harga terjangkau di area Grendeng. Lokasi strategis dekat dengan kampus dan fasilitas umum.",
        "whatsapp": "62881034501933", 
        "instagram": "penkost_pbg",
        "maps_embed_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3760.5697607319917!2d109.3394978!3d-7.4291915!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e65599a72da9c57%3A0xc377dff4c3b2c369!2sWisma%20Alden%20Bu%20Ning!5e1!3m2!1sid!2sid!4v1750140813448!5m2!1sid!2sid",
        "tanggal_post": datetime(2025, 6, 14)
    },

    {
        "id": 11, "nama": "Wisma YOLANDAA", "harga": 7500000, "tipe_sewa": "tahun",
        "lokasi": "Desa Blater", "foto": "kost11.jpg",
        "galeri_foto": ["kost11_view1.jpg", "kost11_view2.jpg", "kost11_view3.jpg"], # TAMBAHAN
        "fasilitas": ["Kamar Mandi Dalam", "Dapur", "Wifi", "Tempat Jemuran", "Parkir Motor Beratap"],
        "tipe_kost": "Putra",
        "deskripsi": "Kost khusus putra yang berjarak 100 meter dari kampus. Bisa ditempuh dengan berjalan kaki ke arah timur.",
        "whatsapp": "62881024501933",
        "instagram": "penkost_pbg",
        "maps_embed_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3956.333233949475!2d109.3397938!3d-7.428326599999998!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e6559867d3347b3%3A0x849446a12c94de81!2sWisma%20YOLANDAA!5e0!3m2!1sid!2sid!4v1750084788725!5m2!1sid!2sid",
        "tanggal_post": datetime(2025, 6, 16)
    },
    {
        "id": 12, "nama": "Kost Panorama", "harga": 850000, "tipe_sewa": "bulan",
        "lokasi": "Blater, Kalimanah", "foto": "kost12.jpg",
        "galeri_foto": ["kost12_view1.jpg", "kost12_view2.jpg", "kost12_view3.jpg"], # TAMBAHAN
        "fasilitas": ["Kamar Mandi Dalam", "Lemari Pakaian", "Dapur Umum", "MCB LIstrik Tiap Kamar", "Parkiran Dalam Area"],
        "tipe_kost": "Putra",
        "deskripsi": "Kost putra murah di blater.",
        "whatsapp": "62881024501933",
        "instagram": "penkost_pbg",
        "maps_embed_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3956.29528510913!2d109.3394325!3d-7.432540599999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e6559d23a3e365b%3A0x12c9d94faf23ac44!2sKOST%20PANORAMA!5e0!3m2!1sid!2sid!4v1750084957180!5m2!1sid!2sid",
        "tanggal_post": datetime(2025, 6, 16)
    },
    {
        "id": 18, 
        "nama": "KOST KHANZA", 
        "harga": 800000, 
        "tipe_sewa": "bulan",
        "lokasi": "Grendeng, Purwokerto", 
        "foto": "kost18.jpg", # Anda perlu menambahkan file gambar ini
        "galeri_foto": ["kost18_view1.jpg", "kost18_view2.jpg", "kost18_view3.jpg","kost18_view4.jpg"],
        "fasilitas": ["Kamar Mandi Luar", "AC", "Wifi", "Dapur Umum", "Parkir Motor"],
        "tipe_kost": "Putra",
        "deskripsi": "Kost putra eksklusif di Grendeng. Fasilitas lengkap termasuk AC, lokasi sangat strategis dan dekat dengan kampus.",
        "whatsapp": "62881024501933", # Ganti dengan nomor yang benar
        "instagram": "penkost_pbg",
        "maps_embed_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3760.5756845935!2d109.3392216!3d-7.428499299999998!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e6559004cbb9865%3A0x249c80b4ef429cbd!2sKost%20KhanZa!5e1!3m2!1sid!2sid!4v1750140884392!5m2!1sid!2sid",
        "tanggal_post": datetime(2025, 6, 12)
    },

    {
        "id": 13, "nama": "Wisma nabil blater Unsoed", "harga": 8000000, "tipe_sewa": "tahun",
        "lokasi": "Blater, Kalimanah", "foto": "kost13.jpg",
        "galeri_foto": ["kost13_view1.jpg", "kost13_view2.jpg", "kost13_view3.jpg"], # TAMBAHAN
        "fasilitas": ["Kamar Mandi Dalam", "Lemari Pakaian", "Dapur Umum", "Wifi", "Parkiran Dalam Area"],
        "tipe_kost": "Putra",
        "deskripsi": "Kost putra yang nyaman dan bersih serta fasilitas lengkap.",
        "whatsapp": "62881024501933",
        "instagram": "penkost_pbg",
        "maps_embed_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3956.296694840015!2d109.34088639999999!3d-7.432384099999999!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e6559cc9c833ebb%3A0xad27e89fc76b2dbd!2sWisma%20nabil%20blater%20Unsoed!5e0!3m2!1sid!2sid!4v1750085533726!5m2!1sid!2sid",
        "tanggal_post": datetime(2025, 6, 16)
    },
    {
        "id": 14, "nama": "Kost Blater 34", "harga": 850000, "tipe_sewa": "bulan",
        "lokasi": "Blater, Kalimanah", "foto": "kost14.jpg",
        "galeri_foto": ["kost14_view1.jpg", "kost14_view2.jpg", "kost14_view3.jpg"], # TAMBAHAN
        "fasilitas": ["Kamar Mandi Dalam", "Lemari Pakaian", "Dapur Umum", "Wifi", "Free Air Listirk", "Parkiran Dalam Area"],
        "tipe_kost": "Putra",
        "deskripsi": "Kost putra terletak di desa Blater, dekat dengan kampus.",
        "whatsapp": "62881024501933",
        "instagram": "penkost_pbg",
        "maps_embed_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3956.33472751082!2d109.33912199999999!3d-7.4281607!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e65595958fba3d7%3A0x6f991176e517cba6!2sKost%20Blater%2034!5e0!3m2!1sid!2sid!4v1750086536746!5m2!1sid!2sid",
        "tanggal_post": datetime(2025, 6, 16)
    },
    {
        "id": 15, "nama": "Wisma Biru", "harga": 400000, "tipe_sewa": "bulan",
        "lokasi": "Dekat Kampus", "foto": "kost15.jpg",
        "galeri_foto": ["kost15_view1.jpg", "kost15_view2.jpg", "kost15_view3.jpg"], # TAMBAHAN
        "fasilitas": ["Kamar Mandi Luar", "Dapur Umum", "Wifi", "Parkiran Dalam Area"],
        "tipe_kost": "Putra",
        "deskripsi": "Kost putra di blater. Di sponsori oleh WarBir. Banyak Wibu.",
        "whatsapp": "62881024501933",
        "instagram": "penkost_pbg",
        "maps_embed_url": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3956.3284568512577!2d109.3399714!3d-7.4288571999999995!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e6559f0ac7c1127%3A0xba80289732998829!2sKost%20Wisma%20Biru!5e0!3m2!1sid!2sid!4v1750086955411!5m2!1sid!2sid",
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