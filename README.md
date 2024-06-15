# ماشین حساب 
 برنامه ای که با زبان پایتون توسعه داده شده است
  ومی تواند 4 عمل <ضرب،تقسیم ،جمع و تفریق را انجام دهد 
## مستندات کد

def add(x, y):
    """
    جمع دو عدد را برمی‌گرداند.
    پارامترها:
    x (float): اولین عدد.
    y (float): دومین عدد.

    بازگشتی:
    float: حاصل جمع دو عدد.

    مثال:
    >>> add(10, 5)
    15
    >>> add(-1, 1)
    0
    >>> add(-1, -1)
    -2
    """
    return x + y

def subtract(x, y):
    """
    تفریق دو عدد را برمی‌گرداند.

    پارامترها:
    x (float): اولین عدد.
    y (float): دومین عدد.

    بازگشتی:
    float: حاصل تفریق دو عدد.

    مثال:
    >>> subtract(10, 5)
    5
    >>> subtract(-1, 1)
    -2
    >>> subtract(-1, -1)
    0
    """
    return x - y

def multiply(x, y):
    """
    ضرب دو عدد را برمی‌گرداند.

    پارامترها:
    x (float): اولین عدد.
    y (float): دومین عدد.

    بازگشتی:
    float: حاصل ضرب دو عدد.

    مثال:
    >>> multiply(10, 5)
    50
    >>> multiply(-1, 1)
    -1
    >>> multiply(-1, -1)
    1
    """
    return x * y

def divide(x, y):
    """
    تقسیم دو عدد را برمی‌گرداند.

    پارامترها:
    x (float): اولین عدد.
    y (float): دومین عدد.

    بازگشتی:
    float یا str: حاصل تقسیم دو عدد یا پیغام خطا در صورت تقسیم بر صفر.

    مثال:
    >>> divide(10, 5)
    2.0
    >>> divide(-1, 1)
    -1.0
    >>> divide(-1, -1)
    1.0
    >>> divide(5, 2)
    2.5
    >>> divide(5, 0)
    'خطا نمی توان تقسیم بر صفر شود.'
    """
    if y == 0:
        return "خطا نمی توان تقسیم بر صفر شود."
    return x / y

def calculator():
    """
    یک ماشین حساب ساده که عملیات جمع، تفریق، ضرب و تقسیم را انجام می‌دهد.
    
    از کاربر می‌خواهد که عملگر را انتخاب کند و دو عدد را وارد کند. سپس نتیجه عملیات را نمایش می‌دهد.
    
    بعد از هر عملیات، از کاربر می‌پرسد که آیا می‌خواهد دوباره از ماشین حساب استفاده کند یا نه.
    """
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

# اجرای تابع ماشین حساب
calculator()

# مستند تست 
 برای بررسی این کد از unittest استفاده شده است 

  قطعه کد : 
 
  import unittest


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(2, 1), 1)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)
        with self.assertRaises(ValueError):
            divide(1, 0)

if name == 'main':
    unittest.main()
# نحوه احرای برنامه :
می توانید از کامپایلر(compiler) یا همان مترجم برنامه آنلاین استفاده کنید 
  
  یک نمومه از کامپایلر آنلاین https://www.online-python.com
