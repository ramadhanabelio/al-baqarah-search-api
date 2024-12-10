from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

app = Flask(__name__)
CORS(app)

ayat_data = []
tfidf_matrix_idn = None
tfidf_matrix_ar = None
vectorizer_idn = None
vectorizer_ar = None
terjemahan = []
teks_arab = []

def fetch_quran_data():
    """Mengambil data Al-Baqarah dari API."""
    api_url = "https://quran-api.santrikoding.com/api/surah/2"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data["ayat"]
    else:
        raise Exception("Gagal mengambil data dari API.")

def preprocess_text(text):
    """Membersihkan dan menormalisasi teks."""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = text.strip()
    return text

def create_tfidf_matrix(ayat):
    """Membuat matriks TF-IDF untuk teks terjemahan dan teks Arab."""
    terjemahan = [a["idn"] for a in ayat]
    teks_arab = [a["ar"] for a in ayat]
    
    vectorizer_idn = TfidfVectorizer()
    tfidf_matrix_idn = vectorizer_idn.fit_transform(terjemahan)
    
    vectorizer_ar = TfidfVectorizer()
    tfidf_matrix_ar = vectorizer_ar.fit_transform(teks_arab)
    
    return tfidf_matrix_idn, vectorizer_idn, tfidf_matrix_ar, vectorizer_ar, terjemahan, teks_arab

def search_ayat(query, tfidf_matrix_idn, vectorizer_idn, tfidf_matrix_ar, vectorizer_ar, ayat, top_n=5, threshold=0.1):
    """Mencari ayat-ayat yang paling relevan dengan query."""
    query_vector_idn = vectorizer_idn.transform([preprocess_text(query)])
    query_vector_ar = vectorizer_ar.transform([preprocess_text(query)])
    
    similarities_idn = cosine_similarity(query_vector_idn, tfidf_matrix_idn).flatten()
    similarities_ar = cosine_similarity(query_vector_ar, tfidf_matrix_ar).flatten()
    
    combined_similarities = (similarities_idn + similarities_ar) / 2
    
    top_indices = combined_similarities.argsort()[-top_n:][::-1]
    results = [
        {
            "ayat": ayat[i],
            "similarity": int(combined_similarities[i] * 100)
        }
        for i in top_indices if combined_similarities[i] >= threshold
    ]
    
    return results

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    top_n = int(request.args.get('n', 5))
    threshold = float(request.args.get('threshold', 0.1))
    
    if not query:
        return jsonify({"error": "Parameter 'q' (query) harus diisi"}), 400

    results = search_ayat(
        query,
        tfidf_matrix_idn,
        vectorizer_idn,
        tfidf_matrix_ar,
        vectorizer_ar,
        ayat_data,
        top_n=top_n,
        threshold=threshold
    )

    if results:
        return jsonify([
            {
                "nomor": r["ayat"]["nomor"],
                "teks_arab": r["ayat"]["ar"],
                "terjemahan": r["ayat"]["idn"],
                "similarity": f"{r['similarity']}%"
            }
            for r in results
        ])
    else:
        return jsonify({"error": "Tidak ditemukan ayat yang relevan"}), 404

if __name__ == '__main__':
    ayat_data = fetch_quran_data()
    tfidf_matrix_idn, vectorizer_idn, tfidf_matrix_ar, vectorizer_ar, terjemahan, teks_arab = create_tfidf_matrix(ayat_data)
    app.run(debug=True)
