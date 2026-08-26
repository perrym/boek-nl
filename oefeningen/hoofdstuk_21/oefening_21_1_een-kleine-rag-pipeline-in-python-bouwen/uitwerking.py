from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

chunks = [
    "MFA is verplicht voor beheerdersaccounts.",
    "Back-ups worden dagelijks gemaakt en dertig dagen bewaard.",
    "API-endpoints moeten objectautorisatie server-side controleren.",
    "Wachtwoorden moeten minimaal veertien tekens bevatten.",
]

vraag = "Welke controle geldt voor toegang tot admin accounts?"
vectorizer = TfidfVectorizer()
chunk_matrix = vectorizer.fit_transform(chunks)
vraag_vector = vectorizer.transform([vraag])
scores = cosine_similarity(vraag_vector, chunk_matrix).ravel()

beste_indices = scores.argsort()[::-1][:2]
context = [chunks[i] for i in beste_indices]

print("Vraag:", vraag)
print("Opgehaalde context:")
for i in beste_indices:
    print(f"- score={scores[i]:.3f}: {chunks[i]}")
