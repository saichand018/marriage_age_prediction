from flask import Flask,render_template,request
import tensorflow as tf

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/thankyou')
def thankyou():
    import joblib
    model=joblib.load('mrg_pred.pkl')
   
    

    gender=request.args.get('gender')
    religion=request.args.get('religion') 
    caste=request.args.get('caste')  
    height_cms=request.args.get('height_cms')  

    prediction=model.predict([[gender,religion,caste,height_cms]])



   


    return render_template('thankyou.html',prediction=prediction)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404







if __name__ == '__main__':
    app.run(debug=True)