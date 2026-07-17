import sqlite3
import os
import pandas as pd
from populate import populate_all

def build_db(db_path="data/virtual_university.db"):
    print("--- Building SQLite Database ---")
    
    # 1. Generate the population
    students_df, enrollments_df = populate_all()
    
    # 2. Open sqlite connection
    if os.path.exists(db_path):
        print(f"Removing existing database at {db_path} to recreate...")
        os.remove(db_path)
        
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 3. Create tables and upload
    print("Writing 'students' table to database...")
    students_df.to_sql("students", conn, if_exists="replace", index=False)
    
    print("Writing 'enrollments' table to database...")
    enrollments_df.to_sql("enrollments", conn, if_exists="replace", index=False)
    
    # 4. Build indices
    print("Creating indices...")
    cursor.execute("CREATE UNIQUE INDEX idx_students_id ON students(student_id);")
    cursor.execute("CREATE INDEX idx_students_plan ON students(academic_plan);")
    cursor.execute("CREATE INDEX idx_students_school ON students(plan_school_college);")
    cursor.execute("CREATE INDEX idx_enrollments_sid ON enrollments(student_id);")
    cursor.execute("CREATE INDEX idx_enrollments_virtual ON enrollments(is_virtual);")
    
    # Commit and close
    conn.commit()
    conn.close()
    print(f"Database successfully built at: {db_path}")

if __name__ == "__main__":
    build_db()
