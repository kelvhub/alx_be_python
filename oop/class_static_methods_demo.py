class Calculator:
    Calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation Type: {cls.Calculation_type}")
        return a * b