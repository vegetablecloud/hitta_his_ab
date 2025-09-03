def calculator(salary, apm_price, rent, fee, threshold):
    rent_price_month = (apm_price * (rent/100)) / 12 # 1000000 * 0.035 / 12 = 2900
    decimal_threshold = threshold / 100 # 0.5
    rest = int(salary - (rent_price_month + fee))
    salary_threshold = int(salary * decimal_threshold)
    # 30000 - 2900 + 5000(7900) = om 22100 <= 15000
    if rest <= salary_threshold:
        return (False, rest, salary_threshold)
    else:
        return (True, rest, salary_threshold)
    
# calculator(30000, 1000000, 3.5, 5000, 50)

def user_input():
    user_salary = int(input("Månadslön: ").replace("kr","").strip())
    apt_price = int(input("Lägenhetspris: ").replace("kr","").strip())
    fee = int(input("Månadsavgift: ").replace("kr","").strip())
    result, rest, threshold = calculator(user_salary, apt_price, 3.5, fee, 50)
    if result:
        print(f"Grattis, du har råd. Du har {rest}kr kvar att leva på")
    else:
        print(f"Tyvärr, du har inte råd. Du skulle ha {rest}kr kvar att leva på. Du måste ha minst {threshold}kr kvar att leva på")

if __name__ == "__main__":
    user_input()