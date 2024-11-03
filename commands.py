import mysql.connector

# Create the database
def create_db(db):
    curs = db.cursor()
    query = "CREATE DATABASE hospital;"
    curs.execute(query)

def use_db(db):
    curs = db.cursor()
    query = "USE hospital;"
    curs.execute(query)
    
def show_table(db):
    curs = db.cursor()
    query = "SHOW TABLES;"
    curs.execute(query)
    
# Check if a database exists
def check_db(db):
    curs = db.cursor()
    query = "SHOW DATABASES;"
    curs.execute(query)
    database = curs.fetchall()
    db_exists = False
    for d in database:
        print(d)
        if 'hospital' in d:
            db_exists = True
            break
        
    return db_exists
# Drop tables if they already exist
def clean_db(db):
    curs = db.cursor()
    query = """
        DROP TABLE Appointment_Assignments;
        DROP TABLE S_Billing;
        DROP TABLE S_Appointments;
        DROP TABLE S_Patient;
        DROP TABLE S_Medical_Staff;
        DROP TABLE S_Department;
        """
    curs.execute(query, multi=True)

# Create Table Section
## Create Department Table
def create_department_table(db):
    curs = db.cursor()
    query = """CREATE TABLE S_Department (
        department_id INTEGER PRIMARY KEY,
        department_name varchar(50),
        num_staff int,
        max_capacity int
        );
        """
    curs.execute(query)

## Create Medical Staff Table
def create_medical_staff_table(db):
    curs = db.cursor()
    query = """
        CREATE TABLE S_Medical_Staff (
        medical_staff_id INTEGER PRIMARY KEY,
        department_id INTEGER,
        first_name varchar(50),
        last_name varchar(50),
        role varchar(30),
        hours INT,
        salary FLOAT(10),
        specialty varchar(50),
        ethnicity varchar(50),
        race varchar(50),
        experience INT(4),
        FOREIGN KEY (department_id) REFERENCES S_Department(department_id)
        );
    """
    curs.execute(query)

## Create Patient table
def create_department_table(db):
    curs = db.cursor()
    query = """
        CREATE TABLE S_Patient (
            patient_id INTEGER PRIMARY KEY,
            first_name varchar(50),
            last_name varchar(50),
            gender CHAR(1),
            birth_date DATE,
            age INT(3),
            height FLOAT(5),
            weight FLOAT(5),
            diagnosis varchar(100),
            insurance varchar(50),
            ethnicity varchar(50),
            race varchar(50)
        );
    """
    curs.execute(query)
    
## Create Appointments table without foreign key on billing_id
def appointments_table(db):
    curs = db.cursor()
    query = """
        CREATE TABLE S_Appointments (
            appt_id INTEGER PRIMARY KEY,
            patient_id INTEGER,
            billing_id INTEGER,
            appt_reason varchar(100),
            admission_date DATE,
            discharge_date DATE,
            doctor_assigned varchar(50),
            FOREIGN KEY (patient_id) REFERENCES S_Patient(patient_id)
        );
    """
    curs.execute(query)



## Create Billing table without foreign key constraint on appt_id
def create_billing_table(db):
    curs = db.cursor()
    query = """    
        CREATE TABLE S_Billing (
            billing_id INTEGER PRIMARY KEY,
            appt_id INTEGER,
            total_amount FLOAT(10),
            insurance_coverage FLOAT(10),
            payment_status CHAR(1), -- Assuming 'Y'/'N' for payment status
            date_issued DATE
        );  
    """
    curs.execute(query)
    
## Create Appointment Assignments table
def create_appointment_assignments_table(db):
    curs = db.cursor()
    query = """ 
        CREATE TABLE Appointment_Assignments (
            medical_staff_id INTEGER,
            appt_id INTEGER,
            PRIMARY KEY (medical_staff_id, appt_id),
            FOREIGN KEY (medical_staff_id) REFERENCES S_Medical_Staff(medical_staff_id),
            FOREIGN KEY (appt_id) REFERENCES S_Appointments(appt_id)
        );
    """
    curs.execute(query)
    
# Insert into S_Department, S_Medical_Staff, S_Patient, and S_Appointments using INSERT ALL
def insert_test_data(db):
    curs = db.cursor()
    query = """     
        INSERT ALL
            INTO S_Department (department_id, department_name, num_staff, max_capacity)
            VALUES (1, 'Cardiology', 15, 50)
            INTO S_Department (department_id, department_name, num_staff, max_capacity)
            VALUES (2, 'Neurology', 10, 40)
            INTO S_Department (department_id, department_name, num_staff, max_capacity)
            VALUES (3, 'Oncology', 20, 60)
            
            INTO S_Medical_Staff (medical_staff_id, department_id, first_name, last_name, role, hours, salary, specialty, ethnicity, race, experience)
            VALUES (101, 1, 'John', 'Doe', 'Doctor', 40, 120000.00, 'Cardiologist', 'Caucasian', 'White', 10)
            INTO S_Medical_Staff (medical_staff_id, department_id, first_name, last_name, role, hours, salary, specialty, ethnicity, race, experience)
            VALUES (102, 2, 'Jane', 'Smith', 'Nurse', 36, 70000.00, 'Neurology', 'Asian', 'Asian', 5)
            INTO S_Medical_Staff (medical_staff_id, department_id, first_name, last_name, role, hours, salary, specialty, ethnicity, race, experience)
            VALUES (103, 3, 'Emily', 'Jones', 'Technician', 38, 60000.00, 'Oncology', 'Hispanic', 'Latino', 7)
            
            INTO S_Patient (patient_id, first_name, last_name, gender, birth_date, age, height, weight, diagnosis, insurance, ethnicity, race)
            VALUES (201, 'Michael', 'Brown', 'M', TO_DATE('1985-06-15', 'YYYY-MM-DD'), 39, 180.3, 85.5, 'Hypertension', 'Medicare', 'Caucasian', 'White')
            INTO S_Patient (patient_id, first_name, last_name, gender, birth_date, age, height, weight, diagnosis, insurance, ethnicity, race)
            VALUES (202, 'Anna', 'Taylor', 'F', TO_DATE('1992-03-21', 'YYYY-MM-DD'), 32, 165.2, 70.3, 'Migraine', 'Aetna', 'African American', 'Black')
            INTO S_Patient (patient_id, first_name, last_name, gender, birth_date, age, height, weight, diagnosis, insurance, ethnicity, race)
            VALUES (203, 'Sophia', 'Garcia', 'F', TO_DATE('2000-10-30', 'YYYY-MM-DD'), 24, 170.5, 65.0, 'Cancer', 'Blue Cross', 'Hispanic', 'Latino')
            
            INTO S_Appointments (appt_id, patient_id, billing_id, appt_reason, admission_date, discharge_date, doctor_assigned)
            VALUES (301, 201, NULL, 'Routine Check-up', TO_DATE('2024-10-01', 'YYYY-MM-DD'), TO_DATE('2024-10-02', 'YYYY-MM-DD'), 'John Doe')
            INTO S_Appointments (appt_id, patient_id, billing_id, appt_reason, admission_date, discharge_date, doctor_assigned)
            VALUES (302, 202, NULL, 'Consultation', TO_DATE('2024-10-03', 'YYYY-MM-DD'), TO_DATE('2024-10-04', 'YYYY-MM-DD'), 'Jane Smith')
            INTO S_Appointments (appt_id, patient_id, billing_id, appt_reason, admission_date, discharge_date, doctor_assigned)
            VALUES (303, 203, NULL, 'Treatment', TO_DATE('2024-10-05', 'YYYY-MM-DD'), TO_DATE('2024-10-10', 'YYYY-MM-DD'), 'Emily Jones')
        SELECT * FROM dual;
    """
    curs.execute(query)

# Insert into S_Billing using INSERT ALL
def insert_billing_data(db):
    curs = db.cursor()
    query = """        
        INSERT ALL
            INTO S_Billing (billing_id, appt_id, total_amount, insurance_coverage, payment_status, date_issued)
            VALUES (401, 301, 300.00, 200.00, 'Y', TO_DATE('2024-10-02', 'YYYY-MM-DD'))
            INTO S_Billing (billing_id, appt_id, total_amount, insurance_coverage, payment_status, date_issued)
            VALUES (402, 302, 500.00, 350.00, 'N', TO_DATE('2024-10-04', 'YYYY-MM-DD'))
            INTO S_Billing (billing_id, appt_id, total_amount, insurance_coverage, payment_status, date_issued)
            VALUES (403, 303, 1000.00, 750.00, 'Y', TO_DATE('2024-10-10', 'YYYY-MM-DD'))
        SELECT * FROM dual;
    """
    curs.execute(query)

# Update S_Appointments to set billing_id after S_Billing is populated
def update_appointments_with_billing(db):
    curs = db.cursor()
    query = """            
        UPDATE S_Appointments SET billing_id = 401 WHERE appt_id = 301;
        UPDATE S_Appointments SET billing_id = 402 WHERE appt_id = 302;
        UPDATE S_Appointments SET billing_id = 403 WHERE appt_id = 303;
    """
    curs.execute(query)

# Add foreign key constraint to S_Billing on appt_id
def add_foreign_key(db):
    curs = db.cursor()
    query = """            
        ALTER TABLE S_Billing
        ADD CONSTRAINT fk_appt_id FOREIGN KEY (appt_id) REFERENCES S_Appointments(appt_id);
    """
    curs.execute(query)
    

# Create view for Patient and Appointment Details
def create_patient_appointment_view(db):
    curs = db.cursor()
    query = """            
        CREATE OR REPLACE VIEW Patient_Appointment_Details AS
        SELECT 
            P.patient_id, 
            P.first_name AS patient_first_name, 
            P.last_name AS patient_last_name, 
            P.diagnosis, 
            A.appt_id, 
            A.admission_date, 
            A.discharge_date, 
            A.appt_reason, 
            A.doctor_assigned
        FROM 
            S_Patient P
        JOIN 
            S_Appointments A ON P.patient_id = A.patient_id;
    """
    curs.execute(query)
    

# Create view for Billing and Patient Details
def create_patient_billing_view(db):
    curs = db.cursor()
    query = """            
        CREATE OR REPLACE VIEW Patient_Appointment_Details AS
        SELECT 
            P.patient_id, 
            P.first_name AS patient_first_name, 
            P.last_name AS patient_last_name, 
            P.diagnosis, 
            A.appt_id, 
            A.admission_date, 
            A.discharge_date, 
            A.appt_reason, 
            A.doctor_assigned
        FROM 
            S_Patient P
        JOIN 
            S_Appointments A ON P.patient_id = A.patient_id;
    """
    curs.execute(query)

# Create view for Medical Staff and Assignments
def create_medical_staff_assignments_view(db):
    curs = db.cursor()
    query = """            
        CREATE OR REPLACE VIEW Medical_Staff_Assignments AS
        SELECT 
            M.medical_staff_id, 
            M.first_name AS staff_first_name, 
            M.last_name AS staff_last_name, 
            M.role, 
            A.appt_id, 
            A.admission_date, 
            A.discharge_date, 
            A.appt_reason
        FROM 
            S_Medical_Staff M
        JOIN 
            Appointment_Assignments AA ON M.medical_staff_id = AA.medical_staff_id
        JOIN 
            S_Appointments A ON AA.appt_id = A.appt_id;
    """
    curs.execute(query)

# Grant SELECT privileges on tables to public or specific user (e.g., 'my_user')
def grant_table_privileges(db):
    curs = db.cursor()
    query = """            
        GRANT SELECT ON S_Department TO PUBLIC;
        GRANT SELECT ON S_Medical_Staff TO PUBLIC;
        GRANT SELECT ON S_Patient TO PUBLIC;
        GRANT SELECT ON S_Appointments TO PUBLIC;
        GRANT SELECT ON S_Billing TO PUBLIC;
        GRANT SELECT ON Appointment_Assignments TO PUBLIC;
    """
    curs.execute(query, multi=True)


# Grant SELECT privileges on views to public or specific user (e.g., 'my_user')
def grant_view_privilege(db):
    curs = db.cursor()
    query = """            
        GRANT SELECT ON Patient_Appointment_Details TO PUBLIC;
        GRANT SELECT ON Billing_Patient_Details TO PUBLIC;
        GRANT SELECT ON Medical_Staff_Assignments TO PUBLIC;
    """
    curs.execute(query, multi=True)


