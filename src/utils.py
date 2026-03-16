import joblib


def save_model(model, path):
    joblib.dump(model, path)


def load_model(path):
    return joblib.load(path)


def save_text(text, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
