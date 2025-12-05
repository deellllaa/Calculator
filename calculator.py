import math
import sqlite3


class ShaftCalculator:
    def __init__(self, db_path = 'shaft_data.db'):
        self.db_path = db_path 
        
        
    def get_weight_per_meter(self, diameter , shape):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            'SELECT density FROM shaft_calculations WHERE diameter = ? AND shape =?' ,
            (diameter , shape)
            
        )
        
        
        result = cursor.fetchone()
        conn.close()
        
        
        if result:
            return result[0]
        else :
            return 0 
        
        
    def calculate_final_weight(self , diameter , shape , length_meters=1):
        weight_per_meter = self.get_weight_per_meter(diameter , shape)
        
        if weight_per_meter == 0 :
            return "این قطر از این شکل پیدا نشد "
        
        final_weight = weight_per_meter * length_meters 
        
        
        
        return {
            'weight_per_meter' : weight_per_meter , 
            'length' : length_meters , 
            'final_weight' : final_weight ,
            'diameter' : diameter ,
            'shape' :shape
        }
        
        
    def get_available_diameters(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT DISTINCT diameter From shaft_calculations ORDER BY diameter')
        diameters = [row[0] for row in cursor.fetchall()]
        
        conn.close()
        return diameters 
    
    
    def get_available_shapes(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT DISTINCT shape FROM shaft_calculations')
        shapes = [row[0] for row in cursor.fetchall()]
        
        
        conn.close()
        
        return shapes 
    
    
if __name__ == "__main__" :
    calc = ShaftCalculator()
    
    
    
    result = calc.calculate_final_weight(5.0,'circle' , 2.5) 
    print(f"وزن برای 1 متر : {result['weight_per_meter']} kg")
    print(f"وزن برای {result['length']} متر : {result['final_weight']} kg")
    
    
    print("قطرهای موجود : " , calc.get_available_diameters()[:5]) 
    print("شکل های موجود : " , calc.get_available_shapes())
    
      
        
            
        
        
        
        
        
        