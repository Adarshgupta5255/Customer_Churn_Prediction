from flask import Flask,render_template,request
import pickle
import numpy as np

model=pickle.load(open('model3.pkl','rb'))
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_churn():
    A=float(request.form.get('A'))
    B=float(request.form.get('B'))
    C=float(request.form.get('C'))
    D=float(request.form.get('D'))
    E=float(request.form.get('E'))
    F=float(request.form.get('F'))
    G=float(request.form.get('G'))
    H=float(request.form.get('H'))
    I=float(request.form.get('I'))
    J=float(request.form.get('J'))
    K=float(request.form.get('K'))

    result = model.predict(np.array([A,B,C,D,E,F,G,H,I,J,K]).reshape(1,11))

    if result[0]==1:
        result="Yes Churning"
    else:
        result="NO Churning"

    return render_template('index.html',result=result)

if __name__=='__main__':
    app.run(debug=True)