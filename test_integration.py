import pytest
import os   
import sys 


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculator import ShaftCalculator


class TestIntegration :
    def test_database_connection(self):
        calc = ShaftCalculator()
        
        
        test_cases = [
            (5.0 , 'circle') ,
            (10.0 , 'square') , 
            (15.0 , 'hexagon')
        ]
        for diameter , shape in test_cases :
            weight = calc.get_weight_per_meter(diameter,shape)
            assert weight is not None 
            print(f"✅ {shape} با قطر {diameter}: {weight} kg/m")
            
    def test_full_workflow(self):
        calc = ShaftCalculator()
        shapes = calc.get_available_shapes()
        assert 'circle' in shapes 
        
        diameters = calc.get_available_diameters()
        assert len(diameters) > 0 
        
        sample_diameter = diameters[0]
        
        sample_shape = 'circle'
        
        result = calc.calculate_final_weight(sample_diameter , sample_shape , 3.0)
        
        
        assert isinstance(result , dict)
        
        assert result['final_weight'] == result['weight_per_meter'] * 3.0 
            