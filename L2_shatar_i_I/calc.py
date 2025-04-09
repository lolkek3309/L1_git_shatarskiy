while True:
    expr = input("Введите выражение (или 'выход'): ")
    if expr.lower() == 'выход':
        break
    try:
        a, op, b = expr.split()
        a = float(a)
        b = float(b)
        if op == '+':
            print(a + b)
        elif op == '-':
            print(a - b)
        elif op == '*':
            print(a * b)
        elif op == '/':
            print(a / b)
    except:
        print("Ошибка ввода")