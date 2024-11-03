-- Step 1: Drop tables if they already exist
DROP TABLE Appointment_Assignments CASCADE CONSTRAINTS;
DROP TABLE S_Billing CASCADE CONSTRAINTS;
DROP TABLE S_Appointments CASCADE CONSTRAINTS;
DROP TABLE S_Patient CASCADE CONSTRAINTS;
DROP TABLE S_Medical_Staff CASCADE CONSTRAINTS;
DROP TABLE S_Department CASCADE CONSTRAINTS;

-- Step 2: Create Tables (same as before)
-- Create Department table
CREATE TABLE S_Department (
    department_id INTEGER PRIMARY KEY,
    department_name VARCHAR2(50),
    num_staff NUMBER,
    max_capacity NUMBER
);

-- Create Medical Staff table
CREATE TABLE S_Medical_Staff (
    medical_staff_id INTEGER PRIMARY KEY,
    department_id INTEGER,
    first_name VARCHAR2(50),
    last_name VARCHAR2(50),
    role VARCHAR2(30),
    hours NUMBER,
    salary FLOAT(10),
    specialty VARCHAR2(50),
    ethnicity VARCHAR2(50),
    race VARCHAR2(50),
    experience NUMBER(4),
    FOREIGN KEY (department_id) REFERENCES S_Department(department_id)
);

-- Create Patient table
CREATE TABLE S_Patient (
    patient_id INTEGER PRIMARY KEY,
    first_name VARCHAR2(50),
    last_name VARCHAR2(50),
    gender CHAR(1),
    birth_date DATE,
    age NUMBER(3),
    height FLOAT(5),
    weight FLOAT(5),
    diagnosis VARCHAR2(100),
    insurance VARCHAR2(50),
    ethnicity VARCHAR2(50),
    race VARCHAR2(50)
);

-- Create Appointments table without foreign key on billing_id
CREATE TABLE S_Appointments (
    appt_id INTEGER PRIMARY KEY,
    patient_id INTEGER,
    billing_id INTEGER,
    appt_reason VARCHAR2(100),
    admission_date DATE,
    discharge_date DATE,
    doctor_assigned VARCHAR2(50),
    FOREIGN KEY (patient_id) REFERENCES S_Patient(patient_id)
);

-- Create Billing table without foreign key constraint on appt_id
CREATE TABLE S_Billing (
    billing_id INTEGER PRIMARY KEY,
    appt_id INTEGER,
    total_amount FLOAT(10),
    insurance_coverage FLOAT(10),
    payment_status CHAR(1), -- Assuming 'Y'/'N' for payment status
    date_issued DATE
);

-- Create Appointment Assignments table
CREATE TABLE Appointment_Assignments (
    medical_staff_id INTEGER,
    appt_id INTEGER,
    PRIMARY KEY (medical_staff_id, appt_id),
    FOREIGN KEY (medical_staff_id) REFERENCES S_Medical_Staff(medical_staff_id),
    FOREIGN KEY (appt_id) REFERENCES S_Appointments(appt_id)
);

-- Step 3: Insert into S_Department, S_Medical_Staff, S_Patient, and S_Appointments using INSERT ALL
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

-- Step 4: Insert into S_Billing using INSERT ALL
INSERT ALL
    INTO S_Billing (billing_id, appt_id, total_amount, insurance_coverage, payment_status, date_issued)
    VALUES (401, 301, 300.00, 200.00, 'Y', TO_DATE('2024-10-02', 'YYYY-MM-DD'))
    INTO S_Billing (billing_id, appt_id, total_amount, insurance_coverage, payment_status, date_issued)
    VALUES (402, 302, 500.00, 350.00, 'N', TO_DATE('2024-10-04', 'YYYY-MM-DD'))
    INTO S_Billing (billing_id, appt_id, total_amount, insurance_coverage, payment_status, date_issued)
    VALUES (403, 303, 1000.00, 750.00, 'Y', TO_DATE('2024-10-10', 'YYYY-MM-DD'))
SELECT * FROM dual;

-- Step 5: Update S_Appointments to set billing_id after S_Billing is populated
UPDATE S_Appointments SET billing_id = 401 WHERE appt_id = 301;
UPDATE S_Appointments SET billing_id = 402 WHERE appt_id = 302;
UPDATE S_Appointments SET billing_id = 403 WHERE appt_id = 303;

-- Step 6: Add foreign key constraint to S_Billing on appt_id
ALTER TABLE S_Billing
ADD CONSTRAINT fk_appt_id FOREIGN KEY (appt_id) REFERENCES S_Appointments(appt_id);

-- Create view for Patient and Appointment Details
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

-- Create view for Billing and Patient Details
CREATE OR REPLACE VIEW Billing_Patient_Details AS
SELECT 
    B.billing_id, 
    P.first_name AS patient_first_name, 
    P.last_name AS patient_last_name, 
    B.total_amount, 
    B.insurance_coverage, 
    B.payment_status, 
    B.date_issued
FROM 
    S_Billing B
JOIN 
    S_Appointments A ON B.appt_id = A.appt_id
JOIN 
    S_Patient P ON A.patient_id = P.patient_id;

-- Create view for Medical Staff and Assignments
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

-- Grant SELECT privileges on tables to public or specific user (e.g., 'my_user')
GRANT SELECT ON S_Department TO PUBLIC;
GRANT SELECT ON S_Medical_Staff TO PUBLIC;
GRANT SELECT ON S_Patient TO PUBLIC;
GRANT SELECT ON S_Appointments TO PUBLIC;
GRANT SELECT ON S_Billing TO PUBLIC;
GRANT SELECT ON Appointment_Assignments TO PUBLIC;

-- Grant SELECT privileges on views to public or specific user (e.g., 'my_user')
GRANT SELECT ON Patient_Appointment_Details TO PUBLIC;
GRANT SELECT ON Billing_Patient_Details TO PUBLIC;
GRANT SELECT ON Medical_Staff_Assignments TO PUBLIC;


