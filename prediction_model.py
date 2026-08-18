import os
import re
import numpy as np
import joblib
import pytesseract
from PIL import Image
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import PorterStemmer

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

DANGEROUS_SUBSTANCES = ["bleach", "disinfectant", "chlorine", "acid", "urine"]
DISEASE_KEYWORDS = ["covid", "cancer", "diabetes", "virus"]
NEGATION_PHRASES = ["no evidence", "not proven", "does not", "cannot", "false", "myth"]
NEGATION_WORDS = {"not", "no", "never", "without"}

# Load truths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
truth_path = os.path.join(BASE_DIR, "dataset", "medical_truths.txt")

with open(truth_path, "r", encoding="utf-8") as f:
    MEDICAL_TRUTHS = [line.strip().lower() for line in f if len(line.strip()) > 10]

tfidfvect = joblib.load("models/tfidfvect.pkl")
truth_vectors = tfidfvect.transform(MEDICAL_TRUTHS)


class PredictionModel:
    def __init__(self, original_text):
        self.original_text = original_text

    def extract_text_from_image(self, image_path):
        try:
            return pytesseract.image_to_string(Image.open(image_path)).strip()
        except:
            return ""

    def preprocess(self, text):
        text = re.sub('[^a-zA-Z]', ' ', text)
        words = text.lower().split()

        return ' '.join(
        ps.stem(w)
        for w in words
        if w not in stop_words or w in NEGATION_WORDS
        )


    def clean_for_display(self, text):
        text = text.replace("“", "").replace("”", "").replace('"', "")
        text = re.sub(r'\s+', ' ', text)
        return text.strip()


    def predict(self):
        text_lower = self.original_text.lower()

        # ✅ DEFINE processed FIRST (FIXES ERROR)
        processed = self.preprocess(self.original_text)

        # 🚨 Dangerous myth detection
        for s in DANGEROUS_SUBSTANCES:
            if s in text_lower:
                for d in DISEASE_KEYWORDS:
                    if d in text_lower:
                        return self.result("FAKE / DANGEROUS MEDICAL MYTH", processed)

        if len(processed.split()) < 4:
            return self.result("FAKE / NOT MEDICAL", processed)

        input_vec = tfidfvect.transform([processed])
        max_sim = np.max(cosine_similarity(input_vec, truth_vectors)[0])

        # 🚨 Negation override
        if any(n in text_lower for n in NEGATION_PHRASES) and max_sim < 0.60:
            return self.result("FAKE / UNVERIFIED MEDICAL NEWS", processed)

        if max_sim >= 0.45:
            label = "REAL MEDICAL NEWS"
        elif max_sim >= 0.30:
            label = "POSSIBLY TRUE / NEEDS VERIFICATION"
        else:
            label = "FAKE / UNVERIFIED MEDICAL NEWS"

        return self.result(label, processed)


    def result(self, label, processed):
        return {
            "original": self.original_text,
            "preprocessed": processed,
            "prediction": label
        }
