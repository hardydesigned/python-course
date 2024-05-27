#Functions
#Man kann sogar Typen angeben, die die Funktionen erwarten

def add(a: int, b: float) -> float:
    return a+b

int_number = 1
float_number = 2.5
sum = add(int_number, float_number)