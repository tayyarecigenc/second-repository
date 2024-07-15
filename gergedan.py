employees = []
def add_employee():
    name = input("Çalışanın adını girin: ")
    salary = input("Çalışanın maaşını girin: ")
    employees.append({"name": name, "salary": salary})
    print(f"{name} adlı çalışan, {salary} maaşıyla eklendi.")
def list_employees():
    if not employees:
        print("Henüz çalışan eklenmedi.")
    else:
        for employee in employees:
            print(f"Ad: {employee['name']}, Maaş: {employee['salary']}")
def filter_employees_by_salary():
    min_salary = input("Minimum maaş değerini girin: ")
    filtered_employees = [e for e in employees if float(e['salary']) > float(min_salary)]
    if filtered_employees:
        for employee in filtered_employees:
            print(f"Ad: {employee['name']}, Maaş: {employee['salary']}")
    else:
        print(f"{min_salary} maaşından yüksek çalışan yok.")
def main():
    while True:
        print("\n--- Çalışan Maaş Yönetim Sistemi ---")
        print("1. Çalışan Ekle")
        print("2. Çalışanları Listele")
        print("3. Belirli Maaştan Yüksek Olan Çalışanları Filtrele")
        print("4. Çıkış")
        choice = input("Seçiminizi yapın: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            list_employees()
        elif choice == "3":
            filter_employees_by_salary()
        elif choice == "4":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek, lütfen tekrar deneyin.")
if __name__ == "__main__":
    main()


import os

def add_income(income_list):
    income  = float(input("eklemek istediginiz geliri giriniz."))
    income_list.append(income)

def add_expense(expense_list):
    expense = float(input("eklemek istediginiz gider miktarini giriniz."))
    expense_list.append(expense)

def show_incomes(income_list):
    print("gelir listesi:")
    for income in income_list:
        print(f"-{income}")

def show_expense(expense_list):
    print("gider listesi:")
    for expense in expense_list:
        print(f"+{expense}")

def calculate_budget(income_list, expense_list):
    total_income = sum(income_list)
    total_expense = sum(expense_list)
    budget = total_income - total_expense
    return budget

def save_to_file(file_name, data):
    with open(file_name,"w") as file:
        for item in data:
            file.write(f"{item}\n")

def read_from_file(file_name):
    if not os.path.exists(file_name):
        return []
    with open(file_name, "r") as file:
        return [float(line.strip())for line in file.readlines()]

def main():
    income_list = read_from_file("incomes.txt")
    expense_list = read_from_file("expense.txt")

    while True:
        print("""
             kisisel finans yonetim uygulamasi
              
        1. gelir ekle
        2. gider ekle
        3. gelirleri goster
        4. giderleri goster
        5. aylik butceyi hesapla
        6. kaydet ve ayril




                """)
        choise = input("bir secenek seciniz (1-6):")
        
        if choise == "1":
            add_income(income_list)
        elif choise == "2":
            add_expense(expense_list)
        elif choise == "3":
            show_incomes(income_list)
        elif choise == "4":
            show_expense(expense_list)
        elif choise == "5":
            budget = calculate_budget(income_list, expense_list)
            print(f"aylik butceniz:{budget}")
        elif choise == "6":
            save_to_file("income.txt", income_list)
            save_to_file("expense.txt", expense_list)
            print("veriler kaydediliyor... ")

            break
        else:
            print("gecersiz")
if __name__ == "__main__":
    main()











