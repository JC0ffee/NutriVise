import sqlite3
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, request, jsonify

app = Flask(__name__)

DISCLAIMER = (
    "Halo! Sebelum kita mulai, perlu diingat bahwa saya bukan pengganti dokter. "
    "Jika kamu mengalami masalah serius atau gejala yang berkelanjutan, sebaiknya segera "
    "konsultasikan dengan dokter atau tenaga medis profesional."
)

# 1. Fungsi untuk memuat data dari database ke DataFrame
def load_data_from_db():
    conn = sqlite3.connect('chatbot.db')
    query = "SELECT * FROM percakapan"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# 2. Fungsi untuk menemukan respons terbaik berdasarkan input pengguna
def cari_respons(input_pengguna, df):
    # Menggabungkan input pengguna dengan data "user" dari database untuk vektorisasi
    semua_input = df['user'].tolist()
    semua_input.append(input_pengguna)

    # Buat vektor TF-IDF untuk seluruh input
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(semua_input)

    # Hitung cosine similarity antara input pengguna dengan setiap "user" di database
    cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()
    indeks_terbaik = cosine_similarities.argmax()  # Mengambil indeks respons dengan kesamaan tertinggi

    # Mengambil respons yang sesuai dari database
    respons = df.iloc[indeks_terbaik]['bot']
    return respons


# # 3. Testing Chatbot
# def chatbot():
#     DISCLAIMER()
#     df = load_data_from_db()
    
#     print("Halo! Saya adalah personal assistance kamu disini, ceritakan gejalamu dan saya akan memberikan saran terbaik untukmu ♡")
#     while True:
#         input_pengguna = input("Kamu: ")
        
#         if input_pengguna.lower() in ['keluar', 'exit', 'bye']:
#             print("Chatbot: Terima kasih! Semoga lekas sembuh dan tetap sehat!")
#             break

#         # Cari respons terbaik dari database
#         respons = cari_respons(input_pengguna, df)
#         print("Chatbot:", respons)

# chatbot()

# Route untuk endpoint chatbot
@app.route('/chatbot', methods=['POST'])
def chat():
    df = load_data_from_db()
    
    # Dapatkan input pengguna dari request JSON
    data = request.get_json()
    input_pengguna = data.get("gejala")

    if not input_pengguna:
        return jsonify({"error": "Gejala tidak boleh kosong."}), 400

    # Cari respons dari chatbot
    respons = cari_respons(input_pengguna, df)

    # Buat respons dengan disclaimer
    response_data = {
        "disclaimer": DISCLAIMER,
        "response": respons
    }
    
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
