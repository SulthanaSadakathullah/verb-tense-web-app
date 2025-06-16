📝 Verb Tense Converter Web App

A simple and interactive web application that extracts verbs from a paragraph and displays their present, past, and past participle forms. It also features speech-to-text input, enabling users to speak instead of typing.



 🚀 Features

- 🧠 NLP-powered verb extraction using "spaCy"
- 🔁 Accurate verb conjugation with "Pattern"
- 🎤 **Voice input** via browser-based speech recognition
- 🌐 Clean and responsive "Flask web interface"
- 💻 Easy to run locally or deploy on cloud platforms (e.g., Render)


🔧 Technologies Used

| Component          | Technology            |
|--------------------|-----------------------|
| Backend            | Python, Flask         |
| NLP                | spaCy, Pattern        |
| Frontend           | HTML, CSS, JavaScript |
| Speech Recognition | Web Speech API        |

---
📸 Screenshots
![image](https://github.com/user-attachments/assets/8e6aa07f-68e5-4c1d-a9b2-07bd16ec86f7)

![image](https://github.com/user-attachments/assets/49126fc7-ed80-4e41-9904-59681a1d45f8)

📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SulthanaSadakathullah/verb-tense-web-app.git
   cd verb-tense-web-app

   Install dependencies:

bash :
pip install -r requirements.txt
python -m spacy download en_core_web_sm

Run the app:
python app.py

Visit:
Open your browser and go to: http://localhost:5000

🗣️ How to Use

* Type or speak a paragraph in the text area.
*Click Convert.
*See a table with the extracted verbs and their tense forms.

Project Structure :

verb-tense-web-app/
│
├── app.py                  # Flask app logic
├── requirements.txt        # Python dependencies
├── render.yaml             # Render deployment config
│
├── templates/
│   └── index.html          # Main HTML template
│
├── static/
│   └── style.css 


🙌 Acknowledgments:
   
    spaCy
    Pattern
    Flask
    Web Speech API


✨ Author
👤 Sulthana Sadakathullah





