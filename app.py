from flask import Flask, render_template, request
from forms import OriginalTextForm
from prediction_model import PredictionModel
import os
from werkzeug.utils import secure_filename
import urllib.parse


app = Flask(__name__)
app.secret_key = "secret123"

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def home():
    form = OriginalTextForm()
    output = None

    if request.method == "POST":
        text = form.original_text.data.strip()
        image = form.image.data

        # IMAGE FIRST
        if image and image.filename:
            filename = secure_filename(image.filename)
            image_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            image.save(image_path)

            predictor = PredictionModel("")
            extracted_text = predictor.extract_text_from_image(image_path)

            if extracted_text.strip():
                predictor = PredictionModel(extracted_text)
                output = predictor.predict()
                output["image_url"] = "/" + image_path.replace("\\", "/")
                output["extracted_text"] = extracted_text
                output["display_text"] = extracted_text.replace("“","").replace("”","").replace('"','')


                # ✅ Use extracted medical text for search
                # ✅ Use cleaned display text for Google search
                search_text = output["display_text"].strip()

                if search_text:
                    query = urllib.parse.quote_plus(search_text)
                    output["google_search"] = f"https://www.google.com/search?q={query}"



            else:
                output = {
                    "prediction": "❌ IMAGE TEXT NOT CLEAR",
                    "original": "",
                    "preprocessed": "",
                    "extracted_text": "No readable text found"
                }

        # TEXT ONLY
        elif text:
            predictor = PredictionModel(text)
            output = predictor.predict()

            # ✅ Use original medical text for search
            search_text = text.strip()

            if search_text:
                query = urllib.parse.quote(search_text)
                output["google_search"] = f"https://www.google.com/search?q={query}"

    # FINAL FALLBACK (prevents emoji / empty search)
    if output and "google_search" not in output:
        fallback_text = output.get("original", "").strip()
        if fallback_text:
            query = urllib.parse.quote(fallback_text)
            output["google_search"] = f"https://www.google.com/search?q={query}"


    return render_template("home.html", form=form, output=output)


if __name__ == "__main__":
    app.run(debug=True)
