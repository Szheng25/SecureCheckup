# Secure Checkup
# @authors: Tahiba Rahman, Aparnaa Senthilnathan, Stacey Zheng
# A Hack.COMS 2024 Hackathon Project

from flask import Flask, jsonify, request

  
he = {'test':'testing', 'test2':'testing22'}
app = Flask(__name__) 
  
@app.route('/', methods = ['GET']) 
def home(): 
    if(request.method == 'GET'): 
        return jsonify(he) 
  
  
@app.route('/home/<int:num>', methods = ['GET']) 
def disp(num): 
    return jsonify({'data': num**2}) 
  
  
if __name__ == '__main__': 
    app.run(debug = True) 