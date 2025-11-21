# hm3
Hospital Database Project (Python + SQLite)
Цей проєкт реалізує:
1.створення бази даних лікарні (Doctors, Patients, Departments, Appointments);
2.заповнення таблиць даними;
3.виконання SELECT-запитів;
4.оновлення даних через UPDATE;
5.повторний запуск SELECT, щоб побачити зміни.
Роботу виконано на основі структури БД із Д/З-1 та SQL-запитів із Д/З-2.
Структура таблиць (ER-діаграма)
Використані таблиці:
1.Departments (id, name, location)
2.Doctors (id, name, surname, phone_numb, specialization, department_id)
3.patient (id, name, surname, address, birth_date, phone_numb)
4.Appointments (id, patient_id, doctor_id, appointment_date)
Звʼязки:
Doctor → Department (many-to-one)
Appointment → Doctor (many-to-one)
Appointment → Patient (many-to-one)
Реалізована функціональність
1. Створення бази даних
Код автоматично створює файл hospital.db і всі таблиці.
2. Наповнення бази тестовими даними
Таблиці заповнюються INSERT-запитами.
3. SELECT-запити
Код виконує такі вибірки:
Пацієнт, лікар і дата візиту
Лікар та його відділення
Результати виводяться у консоль через print().
4. UPDATE
Оновлюється адреса одного пацієнта.
5. Повторні SELECT
Запити виконуються повторно — видно, як змінився результат.

Запити виконуються повторно — видно, як змінився результат.
