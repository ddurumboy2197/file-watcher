class RealTimeAverageCalculator:
    def __init__(self):
        self.sum = 0
        self.count = 0

    def add(self, value):
        self.sum += value
        self.count += 1

    def get_average(self):
        if self.count == 0:
            return 0
        return self.sum / self.count

    def get_count(self):
        return self.count

    def get_sum(self):
        return self.sum

calculator = RealTimeAverageCalculator()

def calculate_average():
    while True:
        print("1. Qo'shish")
        print("2. O'rtacha hisoblash")
        print("3. Sonlar soni")
        print("4. Jami")
        print("5. Chiqish")
        choice = input("Izoh: ")

        if choice == "1":
            value = float(input("Qo'shish uchun qiymat: "))
            calculator.add(value)
        elif choice == "2":
            print("O'rtacha: ", calculator.get_average())
        elif choice == "3":
            print("Sonlar soni: ", calculator.get_count())
        elif choice == "4":
            print("Jami: ", calculator.get_sum())
        elif choice == "5":
            break
        else:
            print("Xato tanlov")

calculate_average()
