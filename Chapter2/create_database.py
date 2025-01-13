import sqlite3


def main():
    db_filename = 'chap2_database.db'

    conn, cursor = create_db_connection_and_cursor(db_filename)

    create_table(cursor) 

    initial_data_book(cursor)

    teacher_data = get_teacher_input()

    handle_teacher_insertion(cursor, teacher_data)

    conn.commit()

    fetch_and_print_all_teachers(cursor)

    conn.close()


def create_db_connection_and_cursor(db_filename):
    """Create and return a connection and cursor object for the SQLite database."""
    conn = sqlite3.connect(db_filename)
    cursor = conn.cursor()
    return conn, cursor


def create_table(cursor):
    """Create the 'teachers' table if it doesn't already exist."""
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers (
        id vifserial,
        first_name varchar(25),
        last_name varchar(50),
        school varchar(50),
        hire_date date,
        salary numeric
    )
    ''')

def initial_data_book(cursor):
    cursor.execute('''
    INSERT INTO teachers (first_name, last_name, school, hire_date, salary)
    VALUES ('Janet','Smith', 'F.D Roosevelt', '2011-10-30', 36200),
           ('Lee','Reynolds','F.D Roosevelt','1993-05-22',65000),
           ('Samuel','Coel','Myers Middle School','2005-08-01',43500),
           ('Samantha','Bush','Myers Middle School','2011-10-30',36200),
           ('Betty','Diaz','Myers Middle School','2005-08-30',43500),
           ('Kathleen','Roush','F.D Roosevelt HS','2010-10-22',38500)                                 
    ''')

def get_teacher_input():
    first_name = input("Enter first name (lim 25 characters): ").strip()
    last_name = input("Enter last name (lim 50 characters): ").strip()
    school = input("Enter school name (lim 50 characters): ").strip()

   # Get the hire date in the 'YYYY-MM-DD' format
    while True:
        hire_date = input("Enter hire date (YYYY-MM-DD): ").strip()
        if len(hire_date) == 10 and hire_date[4] == '-' and hire_date[7] == '-':
            try:
                year, month, day = map(int, hire_date.split('-'))
                if 1 <= month <= 12 and 1 <= day <= 31:
                    break
            except ValueError:
                print("Invalid date format. Please enter in 'YYYY-MM-DD' format.")
        else:
            print("Invalid format. Please enter in 'YYYY-MM-DD' format.")


    # Get the salary
    while True:
        try:
            salary = float(input("Enter salary: ").strip())
            break
        except ValueError:
            print("Invalid salary. Please enter a valid number.")
    return first_name, last_name, school, hire_date, salary

def insert_teacher(cursor, teacher_data):
    cursor.execute('''
    INSERT INTO teachers (first_name, last_name, school, hire_date, salary)
    VALUES (?, ?, ?, ?, ?)
    ''', teacher_data)

def check_teacher_exists(cursor, teacher_data):
    cursor.execute('''
    SELECT * FROM teachers WHERE first_name = ? AND last_name = ?
    ''', (teacher_data[0], teacher_data[1]))
    
    existing_teacher = cursor.fetchone()
    
    return existing_teacher

def handle_teacher_insertion(cursor, teacher_data):
    existing_teacher = check_teacher_exists(cursor, teacher_data)
    
    if existing_teacher:
        print(f"Teacher {teacher_data[0]} {teacher_data[1]} already exists. No action taken.")
    else:
        insert_teacher(cursor, teacher_data)
        print(f"Teacher {teacher_data[0]} {teacher_data[1]} added to the database.")

def fetch_and_print_all_teachers(cursor):
    cursor.execute('SELECT * FROM teachers')
    teachers = cursor.fetchall()
    
    for teacher in teachers:
        print(f"First Name: {teacher[1]}, Last Name: {teacher[2]}, School: {teacher[3]}, Hire Date: {teacher[4]}, Salary: {teacher[5]}")        


if __name__ == '__main__':
    main()

