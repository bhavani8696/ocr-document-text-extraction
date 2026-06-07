from flask import Flask, request, jsonify
from flask_cors import CORS
import easyocr

app = Flask(__name__)
CORS(app)

# OCR Reader
reader = easyocr.Reader(['en'])

# Home Route
@app.route("/")
def home():
    return "OCR Server Running ✅"

# OCR Route
@app.route("/ocr", methods=["POST"])
def run_ocr():

    if "image" not in request.files:
        return jsonify({
            "text": "No image uploaded"
        })

    image = request.files["image"]

    image_path = "temp.jpg"
    image.save(image_path)

    # OCR Extraction
    result = reader.readtext(image_path, detail=0)

    extracted_text = " ".join(result)

    return jsonify({
        "text": extracted_text
    })

# Run Server
if __name__ == "__main__":
    app.run(debug=True)