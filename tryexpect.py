#Try and Except

try:
    print(1/0)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
except Exception as e:
    print(e)
finally:
    print("This will execute no matter what")