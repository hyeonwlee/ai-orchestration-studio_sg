# calculator 함수
def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Error"
        return a / b

print(f"2 + 3 = {calculator(2, 3, "+")}")
print(f"1 / 0 = {calculator(1, 0, "/")}")

# format_receipt 함수
def format_receipt(name, price):
    return f"[{name}] 가격: {price:,}원"

print(format_receipt("라떼", 5500))
print(format_receipt("아메리카노", 4000))

# filter_over 함수
def filter_over(numbers, threshold):
    overNumbers = []
    for number in numbers:
        if number > threshold:
            overNumbers.append(number)
    return overNumbers

print(filter_over([10, 25, 3, 40], 20))
print(filter_over([8, 14, 9, 6, 2], 8))