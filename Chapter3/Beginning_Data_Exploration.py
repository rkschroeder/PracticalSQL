import sqlite3

def main():
    conn = sqlite3.connect('Chapter2/chap2_database.db')
    cursor = conn.cursor()
    
    results_q_orderby=queries_order_by(cursor)
    results_q_distinct=queries_distinct(cursor)
    results_q_where=queries_where(cursor)
    results_q_like=queries_like(cursor)
    results_q_AND_OR=queries_and_or(cursor)
    results_q_final_exer=queries_final_exercise(cursor)

    all_results = {
        "results_q_orderby": results_q_orderby,
        "results_q_distinct": results_q_distinct,
        "results_q_where": results_q_where,
        "results_q_like": results_q_like,
        "results_q_and_or": results_q_AND_OR,
        "results_q_final_exer": results_q_final_exer
    }

    print_results(all_results)
    conn.close() 


def print_results(results):
    for table_name, result in results.items():
        print(f"\n--- {table_name} ---")

        if result:  # Checking if the result is not empty
            for key, data in result.items():
                print(f"\n{key}:")
                
                for row in data:
                    print(row)

def queries_final_exercise(cursor):
    cursor.execute('''
    SELECT first_name, last_name, school
    FROM teachers
    ORDER BY school ASC, last_name ASC;
    ''')
    results_1=cursor.fetchall()

    cursor.execute('''
    SELECT first_name, salary
    FROM teachers
    WHERE first_name LIKE 'S%' AND salary > 40000;   
    ''')
    results_2=cursor.fetchall()

    cursor.execute('''
    SELECT first_name, last_name, salary, hire_date
    FROM teachers
    WHERE hire_date>'2010-01-1'
    ORDER BY salary DESC; ''')
    results_3=cursor.fetchall()

    return {
        "table1_results": results_1,
        "table2_results": results_2,
        "table3_results": results_3
    }
    
                
def queries_and_or(cursor):
    cursor.execute('''
    SELECT first_name,last_name, school, salary
    FROM teachers
    WHERE school = 'Myers Middle School' AND salary <40000;''')
    results_1=cursor.fetchall()

    cursor.execute('''
    SELECT first_name, last_name 
    FROM teachers
    WHERE last_name = 'Cole' or last_name='Bush';''')
    results_2=cursor.fetchall()

    # If we use AND and OR without (), the database will evaluate the AND condition first and then the OR condition
    cursor.execute('''
    SELECT first_name,last_name,school,salary 
    FROM teachers
    WHERE school='F.D Roosevelt HS' AND (salary<38000 OR salary>40000);''')
    results_3=cursor.fetchall()

    return {
        "table1_results": results_1,
        "table2_results": results_2,
        "table3_results": results_3
    }


def queries_like(cursor):
    cursor.execute('''
    SELECT first_name
    FROM teachers
    WHERE first_name LIKE 'sam%';''')
    results_1=cursor.fetchall()
    return {"table1_results": results_1}

def queries_where(cursor):
    cursor.execute('''
    SELECT last_name,school,hire_date
    FROM teachers
    WHERE school='Myers Middle School';''')
    results_1 = cursor.fetchall()

    cursor.execute('''
    SELECT first_name, last_name,school
    FROM teachers
    WHERE first_name='Janet';''')
    results_2 = cursor.fetchall()

    #The command <> is 'not equal to'. So, we will list all the names except F.D Roosevelt 
    cursor.execute('''
    SELECT school
    FROM teachers
    WHERE school <> 'F.D Roosevelt HS'; ''')
    results_3 = cursor.fetchall()

    cursor.execute('''
    SELECT first_name, last_name, hire_date
    FROM teachers
    WHERE hire_date <'2000-01.01';''')
    results_4=cursor.fetchall()  

    cursor.execute('''
    SELECT first_name, last_name, salary
    FROM teachers
    WHERE salary >=43500;''')  
    results_5=cursor.fetchall() 

    # Caution with 'BETWEEN' because it is inclusive
    # It can lead to double counting of values 
    cursor.execute('''
    SELECT first_name, last_name, school, salary
    FROM teachers
    WHERE salary BETWEEN 40000 AND 65000;''')  
    results_6=cursor.fetchall()  
    
    # Better alternative
    cursor.execute('''
    SELECT first_name, last_name, school, salary
    FROM teachers
    WHERE salary>=40000 AND salary<=65000;''')  
    results_7=cursor.fetchall()  

    return {
        "table1_results": results_1,
        "table2_results": results_2,
        "table3_results": results_3,
        "table4_results": results_4,
        "table5_results": results_5,
        "table6_results": results_6,
        "table7_results": results_7
    }

def queries_distinct(cursor):
    cursor.execute('''
    SELECT DISTINCT school, salary
    FROM teachers
    ORDER BY school,salary;''')
    results_1 = cursor.fetchall()
    return {"table1_results": results_1}

def queries_order_by(cursor):
    cursor.execute('''
    SELECT first_name,last_name,salary
    FROM teachers
    ORDER BY 3 DESC;''')
    results_1 = cursor.fetchall()

    cursor.execute('''
    SELECT last_name, school, hire_date
    FROM teachers
    ORDER BY school ASC, hire_date DESC;''')
    results_2 = cursor.fetchall()


    return {
        "table1_results": (results_1),
        "table2_results": (results_2)
    }   

if __name__ == '__main__':
    main()