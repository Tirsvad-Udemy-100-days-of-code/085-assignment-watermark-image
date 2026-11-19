[Dansk](Step-2-Text-Watermark-da) · [English](Step-2-Text-Watermark) · [**Bahasa Malaysia**](Step-2-Text-Watermark-ms)

# Langkah 2: watermark teks dengan kedudukan dan kelegapan

Langkah ini menambah panel kawalan di sebelah kanan tetingkap. Anda menaip teks, memilih saiz dan warnanya, memilih satu daripada sembilan tempat dan menetapkan kelegapan, dan pratonton menunjukkan gambar dengan watermark. Ini ialah fungsi tugasan `add_watermark`.

## Rupanya

Watermark teks dengan tempat lalai:

![Langkah 2: watermark teks](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/raw/branch/main/docs/screenshots/step-2-text.png)

Watermark yang sama dialihkan ke sudut kanan bawah dengan kelegapan yang lebih kuat:

![Langkah 2: watermark diletakkan di sudut](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/085-assignment-watermark-image/raw/branch/main/docs/screenshots/step-2-placed.png)

## Cara mencubanya

```powershell
python -m watermark_image
```

Muat naik gambar, taip teks, tekan **Add watermark** dan tukar tempat atau kelegapan. Teks kosong, saiz di bawah 1 atau kelegapan di luar 0 hingga 100 ditolak dan baris status memberitahu apa yang salah; gambar kekal seperti asal.

## Apa yang kita pelajari dalam langkah ini

- **Objek nilai yang menyemak dirinya sendiri.** `TextWatermark`, `Position` dan kelegapan menolak nilai yang salah semasa dicipta, jadi tiada watermark yang salah wujud dalam program, dan peraturan diuji tanpa pustaka dan tanpa tetingkap.
- **Adunan alfa.** Teks dilukis pada lapisan lutsinar, alfa lapisan didarab dengan kelegapan, dan lapisan diadun ke atas gambar. Beginilah watermark boleh samar tanpa menjadi tidak boleh dibaca.
- **Gambar asal tidak pernah diubah.** Pelukis bekerja pada salinan dan memulangkan `WatermarkedImage` baharu, jadi perubahan watermark seterusnya sentiasa bermula daripada gambar asal yang tidak disentuh.
- **Sembilan tempat daripada satu peraturan.** Tempat ialah enum ringkas; jarak dari tepi ialah satu pemalar, dan pengiraan sudut berada di satu tempat yang diuji untuk kesemua sembilan tempat.
- **Port kedua.** `WatermarkRenderer` ialah port seperti `ImageReader`: kes guna diuji dengan pengganti palsu, dan lukisan Pillow diuji dengan piksel yang diketahui.

Seterusnya: [Langkah 3](Home-ms) menambah watermark logo.
