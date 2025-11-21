import sqlite3

conn = sqlite3.connect("hospital.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Appointments")
cur.execute("DROP TABLE IF EXISTS Doctors")
cur.execute("DROP TABLE IF EXISTS patient")
cur.execute("DROP TABLE IF EXISTS Departments")

cur.execute("""
CREATE TABLE Departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    location TEXT
)
""")

cur.execute("""
CREATE TABLE Doctors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    phone_numb TEXT,
    specialization TEXT,
    department_id INTEGER,
    FOREIGN KEY(department_id) REFERENCES Departments(id)
)
""")

cur.execute("""
CREATE TABLE patient (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    address TEXT,
    birth_date TEXT,
    phone_numb TEXT
)
""")

cur.execute("""
CREATE TABLE Appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER,
    doctor_id INTEGER,
    appointment_date TEXT,
    FOREIGN KEY(patient_id) REFERENCES patient(id),
    FOREIGN KEY(doctor_id) REFERENCES Doctors(id)
)
""")

conn.commit()


cur.execute("INSERT INTO Departments (name, location) VALUES ('Cardiology', '1st floor')")
cur.execute("INSERT INTO Departments (name, location) VALUES ('Neurology', '2nd floor')")

cur.execute("""
INSERT INTO Doctors (name, surname, phone_numb, specialization, department_id)
VALUES 
('Ivan', 'Shevchenko', '123456', 'Cardiologist', 1),
('Petro', 'Bondar', '987654', 'Neurologist', 2)
""")

cur.execute("""
INSERT INTO patient (name, surname, address, birth_date, phone_numb)
VALUES
('Anna', 'Koval', 'Kyiv', '1999-05-10', '555111'),
('Oleh', 'Dmytrenko', 'Lviv', '2001-03-22', '555222')
""")

cur.execute("""
INSERT INTO Appointments (patient_id, doctor_id, appointment_date)
VALUES
(1, 1, '2025-01-10'),
(2, 2, '2025-02-12')
""")

conn.commit()


print("\n===== SELECT 1: Пацієнти та їх лікарі =====\n")
query1 = """
SELECT patient.name || ' ' || patient.surname AS Patient,
       Doctors.name || ' ' || Doctors.surname AS Doctor,
       appointment_date
FROM Appointments
JOIN patient ON patient.id = Appointments.patient_id
JOIN Doctors ON Doctors.id = Appointments.doctor_id
"""
cur.execute(query1)
for row in cur.fetchall():
    print(row)

print("\n===== SELECT 2: Лікарі та їх відділення =====\n")
query2 = """
SELECT Doctors.name || ' ' || Doctors.surname AS Doctor,
       Departments.name AS Department
FROM Doctors
JOIN Departments ON Departments.id = Doctors.department_id
"""
cur.execute(query2)
for row in cur.fetchall():
    print(row)

print("\n===== UPDATE: змінюємо адресу пацієнта =====\n")
cur.execute("UPDATE patient SET address = 'Kharkiv' WHERE id = 1")
conn.commit()

print("===== SELECT 1 після UPDATE =====\n")
cur.execute(query1)
for row in cur.fetchall():
    print(row)

conn.close()
