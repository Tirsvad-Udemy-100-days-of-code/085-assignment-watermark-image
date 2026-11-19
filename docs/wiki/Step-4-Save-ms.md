[Dansk](Step-4-Save-da) · [English](Step-4-Save) · [**Bahasa Malaysia**](Step-4-Save-ms)

# Langkah 4: simpan hasilnya

Langkah terakhir menambah **Save image**. Apabila watermark telah ditambah, butang itu membuka dialog simpan dan menulis gambar bertanda ke fail baharu. Ini ialah fungsi tugasan `save_image`. Fail asal tidak pernah ditimpa.

## Rupanya

Tetingkap dengan watermark ditambah dan butang **Save image** diaktifkan:

![Langkah 4: tetingkap sedia untuk disimpan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/raw/branch/main/docs/screenshots/step-4-save.png)

Selepas disimpan, baris status menyebut nama fail:

![Langkah 4: gambar disimpan](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/raw/branch/main/docs/screenshots/step-4-saved.png)

## Cara mencubanya

```powershell
python -m watermark_image
```

Muat naik gambar, tambah watermark dan tekan **Save image**. Pilih nama yang berakhir dengan `.png`, `.jpg` atau `.jpeg`. Memilih fail asal sekali lagi ditolak dan tiada apa ditulis; akhiran yang tidak disokong atau folder yang tidak boleh ditulis memberi mesej, dan gambar bertanda dikekalkan supaya anda boleh mencuba nama lain.

## Apa yang kita pelajari dalam langkah ini

- **Port di kedua-dua hujung.** Gambar masuk melalui port `ImageReader` dan keluar melalui port `ImageWriter`. Kes guna `SaveImage` tidak mengenali format fail dan diuji dengan penulis palsu.
- **Melindungi fail asal.** Peraturan bahawa sasaran tidak boleh menjadi fail asal terletak dalam domain (`Image.is_source`), membandingkan laluan yang diselesaikan supaya dua ejaan bagi fail yang sama dikesan, dan diuji tanpa menyentuh cakera.
- **Pengendalian ralat.** Setiap kegagalan menjadi ralat bernama dengan puncanya dikekalkan (`raise ... from`), dan model paparan menukar setiap satu kepada mesej biasa. Tiada apa yang ditelan.
- **JPEG tiada kelutsinaran.** Penyesuai meratakan gambar di atas latar belakang putih pepejal sebelum menyimpan JPEG; PNG mengekalkan kelutsinarannya.
- **Seluruh laluan diuji.** Satu ujian memuat naik fail sebenar, menambah watermark, menyimpan, membaca semula hasilnya dan menyemak bahawa fail asal sama bait demi bait.

Itulah seluruh program: muat naik, tanda, simpan. Kembali ke [Utama](Home-ms).
