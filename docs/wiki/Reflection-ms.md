[English](Reflection) · [Dansk](Reflection-da) · **Bahasa Malaysia**

# Refleksi

Tugasan berakhir dengan refleksi: bagaimana projek didekati, apa yang sukar dan mudah, dan apa yang perlu dilakukan secara berbeza. Ini ialah draf; Product Owner menulisnya semula dengan perkataan sendiri.

## Bagaimana saya mendekati projek ini?

Saya menulis pelan dan reka bentuk sebelum kod: untuk siapa program ini, satu kes guna (muat naik, tambah tera air, simpan), model domain dan gambar rajah kelas. Kemudian saya membinanya dalam empat langkah, satu cabang dan satu pull request setiap langkah, dengan tangkapan skrin untuk setiap satu, supaya setiap langkah dapat disemak sendiri.

## Apa yang sukar?

- **Tkinter sahaja tidak cukup.** Ia tidak boleh membaca fail JPEG atau menggabungkan tera air dengan lut sinar, jadi Pillow menjadi satu-satunya kebergantungan masa jalan.
- **Mengasingkan tetingkap daripada peraturan.** Gambar dan peraturan tera air berada dalam lapisan yang tidak mengenali Tkinter; tetingkap hanya memaparkannya. Ini memerlukan lebih pemikiran pada awalnya dan memberi hasil kemudian.
- **Menguji tetingkap.** Ujian grafik tidak boleh mengambil alih desktop, jadi ujian grafik dan tangkapan skrin dijalankan dalam bekas Linux dengan paparan maya.

## Apa yang mudah?

- Meletakkan tera air di salah satu daripada sembilan tempat ialah pengiraan biasa setelah peraturan margin ditulis.
- Peraturan tera air mudah diuji kerana tidak memerlukan tetingkap.

## Apakah pembelajaran terbesar saya?

Menulis kes guna dan kontrak dahulu menjadikan setiap langkah kecil dan jelas. Kod kebanyakannya mengikut reka bentuk, dan apabila tidak, saya mengubah reka bentuk dengan sengaja dan menyemaknya semula.

## Apa yang akan saya lakukan secara berbeza?

- Bermula dengan keputusan tentang Pillow, supaya kod pertama yang membaca gambar ditulis sekali sahaja.
- Mengambil tangkapan skrin sejak langkah pertama, bukannya menambah alat kemudian.
- Mencuba dua tera air serentak (teks dan logo bersama) dan sekumpulan gambar sebagai projek seterusnya.
