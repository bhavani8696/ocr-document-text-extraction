import easyocr

def load_model():
    reader = easyocr.Reader(['en'])
    return reader

def predict_text(reader, image_path):
    result = reader.readtext(image_path)
    text = ""
    for detection in result:
        text += detection[1] + " "
    return text