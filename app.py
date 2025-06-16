from flask import Flask, render_template, request
import spacy
from pattern.en import conjugate, lemma, lexeme, PAST, PRESENT, PARTICIPLE

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

def extract_verbs(text):
    doc = nlp(text)
    verbs = set()
    for token in doc:
        if token.pos_ == "VERB":
            base = lemma(token.text)
            verbs.add(base.lower())
    return list(verbs)

def convert_tenses(verb):
    try:
        present = conjugate(verb, tense=PRESENT, person=3, number='singular') or '-'
        past = conjugate(verb, tense=PAST) or '-'
        participle = conjugate(verb, tense=PAST + PARTICIPLE) or '-'
    except:
        present = past = participle = '-'
    return {
        'verb': verb,
        'present': present,
        'past': past,
        'past_participle': participle
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        paragraph = request.form['paragraph']
        verbs = extract_verbs(paragraph)
        for verb in verbs:
            results.append(convert_tenses(verb))
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
