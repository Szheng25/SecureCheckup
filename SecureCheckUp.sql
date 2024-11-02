-- Drop tables if they already exist
DROP TABLE Appointment_Assignments CASCADE CONSTRAINTS;
DROP TABLE S_Billing CASCADE CONSTRAINTS;
DROP TABLE S_Appointments CASCADE CONSTRAINTS;
DROP TABLE S_Patient CASCADE CONSTRAINTS;
DROP TABLE S_Medical_Staff CASCADE CONSTRAINTS;
DROP TABLE S_Department CASCADE CONSTRAINTS;

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

-- Create Appointments table
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

-- Create Billing table
CREATE TABLE S_Billing (
    billing_id INTEGER PRIMARY KEY,
    appt_id INTEGER,
    total_amount FLOAT(10),
    insurance_coverage FLOAT(10),
    payment_status CHAR(1), -- Assuming 'Y'/'N' for payment status
    date_issued DATE,
    FOREIGN KEY (appt_id) REFERENCES S_Appointments(appt_id)
);

-- Create Appointment Assignments table
CREATE TABLE Appointment_Assignments (
    medical_staff_id INTEGER,
    appt_id INTEGER,
    PRIMARY KEY (medical_staff_id, appt_id),
    FOREIGN KEY (medical_staff_id) REFERENCES S_Medical_Staff(medical_staff_id),
    FOREIGN KEY (appt_id) REFERENCES S_Appointments(appt_id)
);
