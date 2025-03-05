from flask import Flask, render_template,request
import pickle
import re




app = Flask(__name__)

vectorizer, model = pickle.load(open("model_and_vectorizer.pkl", "rb"))



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
    



def predict():
    try:
       
        def optwords(text):
            text=text.lower()

            text=re.sub(r'https?://\S+|www\.\S','',text)

            text=re.sub(r'<.*?>','',text)

            text=re.sub(r'\d','',text)

            text=re.sub(r'\n',' ',text)

            return text
        
        input=request.form.get('text').strip()
        input_opt=optwords(input)
        
        input_features=vectorizer.transform([input_opt])
        prediction=model.predict(input_features)
        return render_template('index.html',pred=prediction)
    except Exception as e:
        return str(e)

    


if __name__ == '__main__':
    app.run(debug=True)
