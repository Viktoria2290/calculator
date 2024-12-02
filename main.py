import sys
def main(input: str) -> str:
    try:
        result = eval(input)
        return str(result)
    except Exception as e:
        return f"Ошибка: {e}"

if __name__ == "__main__":
    while True:
        user_input = input("Введите арифметическое выражение или 'exit' для выхода: ")
        if user_input.lower() == 'exit':
            print("Выход из калькулятора.")
            sys.exit(0)
        result = main(user_input)
        print(f"Результат: {result}")
