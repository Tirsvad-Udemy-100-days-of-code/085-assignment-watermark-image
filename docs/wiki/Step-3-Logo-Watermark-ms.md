[Dansk](Step-3-Logo-Watermark-da) · [English](Step-3-Logo-Watermark) · [**Bahasa Malaysia**](Step-3-Logo-Watermark-ms)

# Langkah 3: watermark logo

Langkah ini membolehkan watermark menjadi gambar kecil dan bukan teks. Pilih **Logo** sebagai jenis watermark, tekan **Choose logo**, pilih fail gambar, tetapkan saiznya sebagai peratusan lebar gambar dan tambahkannya dengan kawalan tempat dan kelegapan yang sama seperti teks.

## Rupanya

Watermark logo diletakkan di atas gambar:

![Langkah 3: watermark logo](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/raw/branch/main/docs/screenshots/step-3-logo.png)

Logo yang sama dialihkan ke sudut kanan bawah dengan kelegapan yang lebih kuat:

![Langkah 3: logo diletakkan di sudut](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/raw/branch/main/docs/screenshots/step-3-placed.png)

## Cara mencubanya

```powershell
python -m watermark_image
```

Muat naik gambar, pilih **Logo**, pilih fail logo (PNG dengan latar belakang lutsinar paling sesuai), gerakkan peluncur saiz dan tekan **Add watermark**. Fail logo yang tidak dapat dibaca ditolak dengan mesej, dan gambar kekal seperti asal.

## Apa yang kita pelajari dalam langkah ini

- **Memanjangkan dengan menambah jenis.** `LogoWatermark` ialah jenis `Watermark` yang baharu di sebelah `TextWatermark`. Peraturan yang dikongsi (kelegapan) kekal dalam kelas asas, dan kes guna serta pelukis masing-masing mendapat satu cabang dan bukan mengubah kod teks yang sedia ada.
- **Persampelan semula.** Logo diskalakan dengan persampelan Lanczos, yang memastikan tepi licin apabila logo besar dikecilkan.
- **Kelutsinaran.** Logo dengan latar belakang lutsinar membiarkan gambar kelihatan, kerana alfa logo itu sendiri dikekalkan dan didarab dengan kelegapan.
- **Satu peraturan kedudukan.** Sembilan tempat dan jarak dari tepi dikira dalam satu fungsi yang digunakan oleh teks dan logo.
- **Menggunakan semula port.** Fail logo dibaca melalui port `ImageReader` yang sama seperti gambar, jadi ia mendapat pengendalian ralat dan ujian yang sama dengan pengganti palsu.

Seterusnya: [Langkah 4](Step-4-Save-ms) menyimpan hasilnya.
