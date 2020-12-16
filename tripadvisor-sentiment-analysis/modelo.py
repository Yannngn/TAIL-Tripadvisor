from joblib import dump, load

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import unicodedata

class Modelo:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('wordnet')
        nltk.download('stopwords')

        self._tfidf = load('./assets/models/tfidf.joblib')
        self._rf = load('./assets/models/random_forest.joblib')

    def _normalizar(self, texto):
        words = texto.split()
        line = " ".join(word for word in words if word not in stopwords.words() and word.isalpha())

        # Normalização
        line = unicodedata.normalize("NFKD", line).encode("ascii", "ignore").decode("utf8")
        line = line.casefold()

        return line

    def _lemmatizar(self, texto):
        lemmatizer = WordNetLemmatizer()

        words = texto.split()
        lemma = ' '.join([lemmatizer.lemmatize(word) for word in words])
        return lemma


    def predict(self, texto):
        texto_norm = self._normalizar(texto)
        texto_lemma = self._lemmatizar(texto_norm)

        texto_lemma = [texto_lemma]
        vetorizado = self._tfidf.transform(texto_lemma)

        return self._rf.predict(vetorizado)