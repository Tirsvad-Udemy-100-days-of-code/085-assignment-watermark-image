[Dansk](Step-1-Upload-da) · [English](Step-1-Upload) · [**Bahasa Malaysia**](Step-1-Upload-ms)

# Langkah 1: tetingkap dan muat naik imej

Dalam langkah ini program mendapat tetingkap dengan butang **Upload image** dan kawasan pratonton. Anda memilih fail JPEG, PNG, BMP, GIF atau WebP dan gambar dipaparkan, diskalakan supaya muat. Ini ialah fungsi tugasan `upload_image`.

## Rupanya

Tetingkap apabila program bermula, tanpa apa-apa dimuatkan:

![Langkah 1: tetingkap kosong](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/raw/branch/main/docs/screenshots/step-1-empty.png)

Tetingkap selepas imej dimuat naik:

![Langkah 1: tetingkap dengan imej yang dimuat naik](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/raw/branch/main/docs/screenshots/step-1-loaded.png)

## Cara mencubanya

```powershell
python -m watermark_image
```

Tekan **Upload image**, pilih fail gambar dan lihat pratonton serta baris status. Jika anda memilih fail yang bukan gambar, baris status memberitahunya dan gambar terdahulu kekal.

## Apa yang kita pelajari dalam langkah ini

- **Reka bentuk berlapis.** Kod dibahagikan kepada `domain`, `application`, `infrastructure` dan `presentation`. Peraturan tidak pernah mengimport Tkinter atau Pillow, jadi ia boleh diuji tanpa tetingkap dan tanpa fail.
- **Port dengan pengganti palsu.** Kes guna `UploadImage` meminta port `ImageReader` membaca gambar. Dalam ujian, pembaca palsu yang kecil menggantikannya, jadi kes guna diuji dalam sekelip mata; `PillowImageReader` diuji berasingan dengan fail sebenar.
- **Paparan tanpa peraturan.** Tetingkap hanya melukis dan menghantar klik. Model paparan menentukan apa yang dikatakan baris status, jadi tingkah laku diuji tanpa membuka tetingkap.
- **Mengapa Pillow.** Tkinter sahaja tidak dapat membaca fail JPEG, jadi Pillow membaca fail dan menukarnya kepada bait RGBA biasa yang digunakan oleh seluruh program.
- **Ujian grafik yang tidak pernah mengambil tetikus anda.** Tangkapan skrin di atas dibuat dalam bekas Linux dengan paparan maya, bukan pada desktop.

Seterusnya: [Langkah 2](Step-2-Text-Watermark-ms) menambah watermark teks.
