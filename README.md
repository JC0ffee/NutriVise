# NutriVise: Chatbot Kesehatan

NutriVise atau Nutrition Advice for Wellness adalah chatbot kesehatan yang dirancang untuk memberikan saran kesehatan berdasarkan gejala yang diberikan oleh pengguna. Chatbot ini dapat membantu memberikan informasi dasar tentang kesehatan, memberikan saran kepada pengguna mengenai nutrisi dan multivitamin yang harus dikonsumsinya. NutriVise bukan pengganti profesional medis, jadi pengguna disarankan untuk berkonsultasi dengan dokter jika mengalami masalah kesehatan serius.

## Disclaimer
NutriVise hanya memberikan saran umum berdasarkan data yang ada. **Jika kalian mengalami masalah serius atau gejala yang berkelanjutan, segera konsultasikan dengan dokter atau tenaga medis profesional.**

## Dataset
Dataset percakapan yang digunakan oleh NutriVise berisi **1,000 percakapan** antara pengguna dan chatbot. Setiap entri dalam dataset berisi:
- **id**: ID unik untuk setiap percakapan.
- **user**: Gejala atau keluhan kesehatan yang dilaporkan oleh pengguna.
- **bot**: Respons yang diberikan oleh chatbot berupa saran atau rekomendasi kesehatan.

Dataset ini disimpan dalam database SQLite bernama `chatbot.db` dengan tabel `percakapan`. Chatbot menggunakan data ini untuk mencocokkan input pengguna dan memberikan respons yang sesuai.

## Arsitektur
NutriVise menggunakan pendekatan *retrieval-based* dengan algoritma **TF-IDF** dan **Cosine Similarity** untuk mencocokkan gejala pengguna dengan respons yang paling sesuai dari database.

- **TF-IDF (Term Frequency-Inverse Document Frequency)**: Mengonversi teks menjadi vektor untuk mengidentifikasi kata-kata penting dalam gejala pengguna.
- **Cosine Similarity**: Mengukur kesamaan antara input pengguna dan respons yang tersimpan dalam database untuk menemukan respons yang paling mirip.

## Fitur
- **Pencocokan Gejala**: NutriVise mencocokkan gejala pengguna dengan database untuk menemukan respons paling relevan.
- **Respons dengan Disclaimer**: Chatbot akan menyertakan pesan disclaimer sebelum memberikan saran kesehatan.
- **Endpoint API**: Chatbot dapat diakses melalui API, memungkinkan integrasi dengan aplikasi lain, seperti aplikasi Android.

## Persyaratan (Requirements)
Pastikan untuk menginstal pustaka yang diperlukan dengan perintah berikut:

```bash
pip install Flask pandas scikit-learn
```

# Cara menggunakan NutriVise

API akan berjalan di http://127.0.0.1:8080 secara lokal.

Untuk mengakses API dari perangkat lain, dengan menggunakan [Ngrok](https://ngrok.com/download) dan menjalankan perintah ```ngrok http 8080``` setelah mengaktifkan server Flask.

## Endpoint: /chatbot
- **Method**: ```Post```
- **Request Body**: ```JSON```
- **Contoh di postman**:
```bash
{
    "gejala": "Saya mengalami gangguan pernapasan"
}
```
- **Contoh menguji API menggunakan** ```curl```
```bash
curl -X POST http://127.0.0.1:8080/chatbot -H "Content-Type: application/json" -d '{"gejala": "Saya sering merasa lelah dan tidak bertenaga"}'
```

