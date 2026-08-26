from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

chunks = [
    "Controleer objectautorisatie om BOLA te voorkomen.",
    "Gebruikers mogen alleen hun eigen klantrecord lezen.",
    "De firewall blokkeert ongewenst inkomend verkeer.",
]
vraag = "Welke maatregel voorkomt BOLA?"

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(chunks + [vraag])
semantisch = cosine_similarity(X[-1], X[:-1]).ravel()

term = "bola"
lexicaal = [1.0 if term in chunk.lower() else 0.0 for chunk in chunks]
hybrid = [0.6 * s + 0.4 * l for s, l in zip(semantisch, lexicaal)]

for chunk, s, l, h in sorted(zip(chunks, semantisch, lexicaal, hybrid), key=lambda x: x[3], reverse=True):
    print(f"hybrid={h:.3f}, semantisch={s:.3f}, lexicaal={l:.1f} | {chunk}")
