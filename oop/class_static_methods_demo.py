class Calculator:
    Calculator_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculator Type: {cls.Calculator_type}")
        return a * b