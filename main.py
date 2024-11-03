# Secure Checkup
# @authors: Tahiba Rahman, Aparnaa Senthilnathan, Stacey Zheng
# A Hack.COMS 2024 Hackathon Project

from flask import Flask, jsonify, request
import mysql.connector
from commands import *

def main():
    username, password = load_acc()
    db = mysql.connector.connect(
        host = "localhost",
        user = username,
        password = password
    )
    
    # test run using commands from the file
    if check_db(db):
        use_db(db)
        # show_table(db)
        clean_db(db)
    else:
        create_db(db)
        use_db(db)
    print(db)
    
    # create_department_table(db)
    # create_medical_staff_table(db)
    # create_department_table(db)
    # appointments_table(db)
    # create_billing_table(db)
    # create_appointment_assignments_table(db)
    # insert_test_data(db)
    # insert_billing_data(db)
    # update_appointments_with_billing(db)
    # add_foreign_key(db)
    # create_patient_appointment_view(db)
    # create_patient_billing_view(db)
    # create_medical_staff_assignments_view(db)
    # grant_table_privileges(db)
    # grant_view_privilege(db)
    
def load_acc():
    with open(".envtemplate", "r") as f:
        return f.readline().strip(), f.readline().strip()

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
    main()
    # app.run(debug = True) 