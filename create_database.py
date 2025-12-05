import sqlite3

def create_database():
    conn = sqlite3.connect('shaft_data.db')
    cursor = conn.cursor()
    
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS shaft_calculations (
            diameter REAL,
            shape TEXT, 
            density REAL
        )
    ''')
    
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS calculation_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            shape TEXT NOT NULL,
            diameter REAL NOT NULL,
            length REAL NOT NULL,
            weight REAL NOT NULL,
            calculated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ دیتابیس و جدول تاریخچه ساخته شد!")

if __name__ == "__main__":
    create_database()