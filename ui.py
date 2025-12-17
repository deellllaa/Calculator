import tkinter as tk 
from tkinter import ttk 
from calculator import ShaftCalculator 

class ShaftCalculatorUI:
    def __init__(self):
        self.calculator = ShaftCalculator()
        self.window = tk.Tk()
        self.window.title("محاسبه کننده وزن شافت")
        self.window.geometry("500x400")
        
        self.selected_shape = tk.StringVar()
        self.selected_diameter = tk.StringVar()
        self.length_var = tk.StringVar(value="1")
        
        self.create_widgets()
        
    def create_widgets(self):
        
        title_label = tk.Label( 
            self.window,
            text="محاسبه وزن شافت های فلزی",
            font=("Arial", 16, "bold"),
            fg="blue"
        )
        title_label.pack(pady=20)
        
        
        shape_frame = tk.LabelFrame(  
            self.window, 
            text="انتخاب شکل شافت", 
            padx=10, 
            pady=10
        )
        shape_frame.pack(pady=10, padx=20, fill="x")  
        
        shapes = self.calculator.get_available_shapes()
        for i, shape in enumerate(shapes):
            persian_name = self.get_persian_name(shape)
            rb = tk.Radiobutton(
                shape_frame,
                text=persian_name, 
                variable=self.selected_shape, 
                value=shape,
                font=("Arial", 12)
            )
            rb.grid(row=0, column=i, padx=10, sticky="w")  
        
        # فریم انتخاب قطر
        diameter_frame = tk.LabelFrame(  
            self.window, 
            text="انتخاب قطر (میلی‌متر)", 
            padx=10, 
            pady=10
        )
        diameter_frame.pack(pady=10, padx=20, fill="x")
        
        diameters = self.calculator.get_available_diameters() 
        diameter_strings = [str(d) for d in diameters]  
        
        diameter_combo = ttk.Combobox(  
            diameter_frame,
            textvariable=self.selected_diameter, 
            values=diameter_strings,  
            state="readonly", 
            font=("Arial", 12)
        )
        diameter_combo.pack(pady=5)
        
        # فریم ورودی طول
        length_frame = tk.LabelFrame(  
            self.window, 
            text="طول شافت (متر)", 
            padx=10, 
            pady=10
        )
        length_frame.pack(pady=10, padx=20, fill="x")
        
        length_entry = tk.Entry(
            length_frame, 
            textvariable=self.length_var,
            font=("Arial", 12),  
            justify="center"  
        )
        length_entry.pack(pady=5)
        
        # دکمه محاسبه
        calculate_btn = tk.Button(  
            self.window, 
            text="محاسبه وزن",
            command=self.calculate_weight, 
            font=("Arial", 14, "bold"),
            bg="green",
            fg="white",
            padx=20,
            pady=10
        )
        calculate_btn.pack(pady=20)
        
        # فریم نمایش نتیجه
        self.result_frame = tk.LabelFrame(  
            self.window, 
            text="نتیجه محاسبه", 
            padx=10, 
            pady=10
        )
        self.result_frame.pack(pady=10, padx=20, fill="x")
        
        self.result_label = tk.Label(  
            self.result_frame, 
            text="لطفا شکل و قطر را انتخاب کنید", 
            font=("Arial", 12), 
            fg="gray"
        )
        self.result_label.pack(pady=10)  
        
    def get_persian_name(self, english_name):
        names = {
            'circle': 'دایره', 
            'square': 'مربع',
            'hexagon': 'شش پر'  
        }
        return names.get(english_name, english_name)
    
    def calculate_weight(self):
     try:
        shape = self.selected_shape.get()
        diameter_str = self.selected_diameter.get()
        length_str = self.length_var.get()
        
        print(f"DEBUG: shape={shape}, diameter={diameter_str}, length={length_str}")  # این خط رو اضافه کن
        
        if not shape:
            self.result_label.config(text="❌ لطفا شکل را انتخاب کنید", fg="red")
            return
            
        if not diameter_str:
            self.result_label.config(text="❌ لطفا قطر را انتخاب کنید", fg="red")
            return
        
        diameter = float(diameter_str)
        length = float(length_str)
        
        print(f"DEBUG: Calculating for diameter={diameter}, length={length}")  
        
        result = self.calculator.calculate_final_weight(diameter, shape, length)
        
        print(f"DEBUG: Result = {result}")  
        
        if isinstance(result, str):
            self.result_label.config(text=result, fg="red")
        else:
            persian_shape = self.get_persian_name(shape)
            message = f"""📐 شکل: {persian_shape}
📏 قطر: {diameter} میلی‌متر
📏 طول: {length} متر
⚖️ وزن: {result['final_weight']:.3f} کیلوگرم"""
            self.result_label.config(text="محاسبه انجام شد", fg="green")
            
     except Exception as e:
        print(f"ERROR: {e}")  
        self.result_label.config(text="خطا در محاسبه", fg="red")     


    def run(self):
        self.window.mainloop()
        
        
    
    
    
if __name__ == "__main__":
    app = ShaftCalculatorUI()
    app.run()