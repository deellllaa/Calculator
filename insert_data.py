import sqlite3


conn = sqlite3.connect('shaft_data.db')

cursor = conn.cursor()



data = [
    (3 , 'circle' , 0.056) , 
    (3 , 'square' , 0.071) ,
    (3 , 'hexagon' , 0.061) ,
    (3.5 , 'circle' , 0.076) , 
    (3.5 , 'square' , 0.096) ,
    (3.5 , 'hexagon' , 0.083) ,
    (4 , 'circle' , 0.099) , 
    (4 , 'square' , 0.126) ,
    (4 , 'hexagon' , 0.109) ,
    (4.5 , 'circle' , 0.125) , 
    (4.5 , 'square' , 0.159) ,
    (4.5 , 'hexagon' , 0.138) ,
    (5 , 'circle' , 0.154) , 
    (5 , 'square' , 0.196) ,
    (5 , 'hexagon' , 0.170) ,
    (5.5 , 'circle' , 0.187) , 
    (5.5 , 'square' , 0.237) ,
    (5.5 , 'hexagon' , 0.206) ,
    (6 , 'circle' , 0.222) , 
    (6 , 'square' , 0.283) ,
    (6 , 'hexagon' , 0.245) ,
  
  
    
]

cursor.executemany('INSERT INTO shaft_calculations VALUES (?,?,?)' , data)
conn.commit()
conn.close()

print("داده ها وارد شدند ")


