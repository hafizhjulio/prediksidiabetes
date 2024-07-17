from flask import Flask, render_template, request, url_for, jsonify
import pickle
import numpy as np

app = Flask(__name__, template_folder="templates")
model = pickle.load(open(r"Final3.pkl", "rb"))

# Tambahkan akurasi model
model_accuracy = 78  # Contoh akurasi model dalam persen

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("Home.html")

@app.route('/AboutMe', methods=['GET', 'POST'])
def aboutme():
    return render_template('AboutMe.html')

@app.route('/ContactUs', methods=['GET', 'POST'])
def contactus():
    return render_template('ContactUs.html')

@app.route('/HealthTools', methods=['GET', 'POST'])
def healthtools():
    return render_template('HealthTools.html')

@app.route('/ExpertAdv', methods=['GET', 'POST'])
def expertadv():
    return render_template('ExpertAdv.html')

@app.route('/Diet&Exer', methods=['GET', 'POST'])
def dietandexer():
    return render_template('Diet&Exer.html')

@app.route('/Test', methods=['GET', 'POST'])
def test():
    return render_template('Form.html')

@app.route('/process_data', methods=['POST'])
def process_data():
    # Get data from the request
    data = request.get_json().get('data')
    print(data)
    dt1 = int(data[0])
    dt2 = int(data[1])
    dt3 = int(data[2])
    dt4 = int(data[3])
    dt5 = int(data[4])
    dt6 = float(data[5])
    dt7 = float(data[6])
    dt8 = int(data[7])
    dat = (dt1, dt2, dt3, dt4, dt5, dt6, dt7, dt8)
    print(dat)
    final = np.array([dat])
    print(final)
    prediction = model.predict(final)
    print(prediction)
    res1 = prediction[0]
    if res1 == 0:
        msg = "Jangan khawatir! Kamu tampak benar-benar sehat dan baik-baik saja"
    elif res1 == 1:
        msg = "Anda rentan terhadap gaya hidup diabetes. Tolong perhatikan kebiasaan Anda"

    # Return the prediction and model accuracy as JSON response
    return jsonify({'result': msg, 'accuracy': model_accuracy})

if __name__ == "__main__":
    app.run(debug=True)
