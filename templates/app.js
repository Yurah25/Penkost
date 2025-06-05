document.addEventListener("DOMContentLoaded", function() {
    // Ambil semua elemen kamar-item yang sudah ada di HTML
    const kamarItems = document.querySelectorAll(".kamar-item");

    // Tambahkan event listener untuk menampilkan detail kamar
    kamarItems.forEach(function(kamarItem) {
        kamarItem.addEventListener("click", function() {
            const nama = kamarItem.querySelector("h3").textContent;
            const deskripsi = kamarItem.getAttribute('data-deskripsi'); // Mengambil deskripsi dari atribut data
            alert(`Detail Kamar: ${deskripsi}`);
        });
    });
});