def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "خطا نمی توان تقسیم بر صفر شود."
    return x / y

def calculator():
    print("عملگر را انتخاب کنید:")
    print("1. برای جمع")
    print("2. برای تفریق")
    print("3. برای ضرب")
    print("4. برای تقسیم")

    while True:
        choice = input("عدد مورد نظر را برای استفاده از ماشین حساب وارد کنید(1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("اولین عدد را وارد کنید: "))
            num2 = float(input("دومین عدد را وارد کنید: "))

            if choice == '1':
                print(f"نتیجه: {add(num1, num2)}")

            elif choice == '2':
                print(f"نتیجه: {subtract(num1, num2)}")

            elif choice == '3':
                print(f"نتیجه: {multiply(num1, num2)}")

            elif choice == '4':
                print(f"نتیجه: {divide(num1, num2)}")
        else:
            print(" عدد وارد شده اشتباه است")


        next_calculation = input("آیا می خواهید از ماشین حساب دوباره استفاده کنید؟  (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

calculator()