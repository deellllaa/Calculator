import pytest   
import os   
import sys    
import sqlite3



sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculator import ShaftCalculator

class TestShaftCalculator :
    
    def test_get_weight_per_meter_existing_data(self):
        calc = ShaftCalculator()
        weight = calc.get_weight_per_meter(5.0 , 'circle')
        assert weight is not None
        assert isinstance(weight,(int,float))
        
        
        
    def test_get_weight_per_meter_nonexistent_data(self):
        calc = ShaftCalculator()
        weight = calc.get_weight_per_meter(999.0 , 'nonexistent_shape')
        assert weight == 0 
        
    def test_calculate_final_weight_success(self):
        calc = ShaftCalculator()
        result = calc.calculate_final_weight(5.0 , 'circle' , 2.5)
        
        
        
        assert isinstance(result, dict)
        assert 'weight_per_meter' in result
        assert 'length' in result
        assert 'final_weight' in result
        assert 'diameter' in result
        assert 'shape' in result
        assert result['length'] == 2.5
        assert result['diameter'] == 5.0
        assert result['shape'] == 'circle'
        assert result['final_weight'] == result['weight_per_meter'] * 2.5
    
    def test_calculate_final_weight_nonexistent_data(self):
        calc = ShaftCalculator()
        result = calc.calculate_final_weight(999.0, 'nonexistent_shape', 2.5)
        assert result == "این قطر از این شکل پیدا نشد "
    
    def test_get_available_diameters(self):
       
        calc = ShaftCalculator()
        diameters = calc.get_available_diameters()
        
        assert isinstance(diameters, list)
        assert len(diameters) > 0
        assert all(isinstance(d, (int, float)) for d in diameters)
    
    def test_get_available_shapes(self):
        calc = ShaftCalculator()
        shapes = calc.get_available_shapes()
        
        assert isinstance(shapes, list)
        assert len(shapes) > 0
        assert 'circle' in shapes
        assert 'square' in shapes
        assert 'hexagon' in shapes

    def test_calculate_with_default_length(self):
        calc = ShaftCalculator()
        result = calc.calculate_final_weight(5.0, 'circle')  
        
        assert result['length'] == 1  
        assert result['final_weight'] == result['weight_per_meter']  