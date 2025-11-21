# hm3
Hospital Database Project (Python + SQLite)
Опис проєкту

Цей проєкт реалізує:

створення бази даних лікарні (Doctors, Patients, Departments, Appointments);

заповнення таблиць даними;

виконання SELECT-запитів;

оновлення даних через UPDATE;

повторний запуск SELECT, щоб побачити зміни.

Роботу виконано на основі структури БД із Д/З-1 та SQL-запитів із Д/З-2.

Структура таблиць (ER-діаграма)

Використані таблиці:

Departments (id, name, location)

Doctors (id, name, surname, phone_numb, specialization, department_id)

patient (id, name, surname, address, birth_date, phone_numb)

Appointments (id, patient_id, doctor_id, appointment_date)

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
