<div align="center">

### Al-Baqarah Search API

</div>

## 📙 Description

**Al-Baqarah Search API** is a project that provides an API service to search for the most relevant verses from Surah Al-Baqarah in the Quran. Users can search by Arabic text, Indonesian translation, or keywords, and receive results based on similarity scores using TF-IDF and cosine similarity.

### API Endpoints

Below is the table of available API endpoints:

| Method | Endpoint   | Description                                                              |
| ------ | ---------- | ------------------------------------------------------------------------ |
| GET    | /search?q= | Search for relevant verses based on query (`q`) and optional parameters. |

### Query Parameters for `/search`

| Parameter | Type   | Description          |
| --------- | ------ | -------------------- |
| `q`       | string | Query to search for. |

### Example

- Endpoint: `/search?q=berdoa`
- Returns up to 3 verses that match the query "kitab" with a similarity score of at least 20%.

## 📖 Features

1. Search for verses from Surah Al-Baqarah using Indonesian or Arabic text.
2. Results ranked by similarity score using TF-IDF and cosine similarity.
3. Adjustable parameters for number of results (`n`) and minimum similarity threshold (`threshold`).

## 🛠️ Project Resources

1. Python
2. Flask
3. Scikit-learn
4. Flask-CORS
5. Requests

## 🛠️ Project Installation Guide

### Prerequisites

Make sure you have Python installed on your system. The recommended version is **Python 3.8 or newer**.

### Steps

**1.** Clone the repository project into a local directory:

```bash
git clone https://github.com/username/al-baqarah-search-api.git
```

**2.** Navigate to the project directory:

```bash
cd al-baqarah-search-api
```

**3.** Install required libraries:

```bash
pip install -r requirements.txt
```

**4.** Run the API server:

```bash
python app.py
```

After following these steps, the API server is now running and can be accessed via a browser or an API testing tool such as Postman.

### Example API Response

Request:

```bash
GET /search?q=berdoa
```

Response:

```bash
[
    {
        "nomor": 186,
        "similarity": "14%",
        "teks_arab": "وَاِذَا سَاَلَكَ عِبَادِيْ عَنِّيْ فَاِنِّيْ قَرِيْبٌ ۗ اُجِيْبُ دَعْوَةَ الدَّاعِ اِذَا دَعَانِۙ فَلْيَسْتَجِيْبُوْا لِيْ وَلْيُؤْمِنُوْا بِيْ لَعَلَّهُمْ يَرْشُدُوْنَ ",
        "terjemahan": "Dan apabila hamba-hamba-Ku bertanya kepadamu (Muhammad) tentang Aku, maka sesungguhnya Aku dekat. Aku Kabulkan permohonan orang yang berdoa apabila dia berdoa kepada-Ku. Hendaklah mereka itu memenuhi (perintah)-Ku dan beriman kepada-Ku, agar mereka memperoleh kebenaran."
    },
    {
        "nomor": 201,
        "similarity": "11%",
        "teks_arab": "وَمِنْهُمْ مَّنْ يَّقُوْلُ رَبَّنَآ اٰتِنَا فِى الدُّنْيَا حَسَنَةً وَّفِى الْاٰخِرَةِ حَسَنَةً وَّقِنَا عَذَابَ النَّارِ ",
        "terjemahan": "Dan di antara mereka ada yang berdoa, “Ya Tuhan kami, berilah kami kebaikan di dunia dan kebaikan di akhirat, dan lindungilah kami dari azab neraka.”"
    },
    {
        "nomor": 127,
        "similarity": "10%",
        "teks_arab": "وَاِذْ يَرْفَعُ اِبْرٰهٖمُ الْقَوَاعِدَ مِنَ الْبَيْتِ وَاِسْمٰعِيْلُۗ رَبَّنَا تَقَبَّلْ مِنَّا ۗ اِنَّكَ اَنْتَ السَّمِيْعُ الْعَلِيْمُ ",
        "terjemahan": "Dan (ingatlah) ketika Ibrahim meninggikan pondasi Baitullah bersama Ismail, (seraya berdoa), “Ya Tuhan kami, terimalah (amal) dari kami. Sungguh, Engkaulah Yang Maha Mendengar, Maha Mengetahui."
    },
    {
        "nomor": 250,
        "similarity": "10%",
        "teks_arab": "وَلَمَّا بَرَزُوْا لِجَالُوْتَ وَجُنُوْدِهٖ قَالُوْا رَبَّنَآ اَفْرِغْ عَلَيْنَا صَبْرًا وَّثَبِّتْ اَقْدَامَنَا وَانْصُرْنَا عَلَى الْقَوْمِ الْكٰفِرِيْنَ ۗ ",
        "terjemahan": "Dan ketika mereka maju melawan Jalut dan tentaranya, mereka berdoa, “Ya Tuhan kami, limpahkanlah kesabaran kepada kami, kukuhkanlah langkah kami dan tolonglah kami menghadapi orang-orang kafir.”"
    }
]
```
