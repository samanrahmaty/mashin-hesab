def add(x, y):
    return x + y
def calculator():
    print("عملگر را انتخاب کنید:")
    print("1. برای جمع")

    
    while True:
        choice = input("عدد مورد نظر را برای استفاده از ماشین حساب وارد کنید(1/2): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("اولین عدد را وارد کنید: "))
            num2 = float(input("دومین عدد را وارد کنید: "))

            if choice == '1':
                print(f"نتیجه: {add(num1, num2)}")


        next_calculation = input("آیا می خواهید از ماشین حساب دوباره استفاده کنید؟  (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

calculator()