from pydantic import BaseModel, Field, field_validator

class Calculator(BaseModel):
    result: bool
    rest: int
    threshold: int
   

class UserVal(BaseModel):
    salary: int = Field(gt=-1)
    apt_price: int = Field(gt=-1)
    fee: int = Field(gt=-1)

    @field_validator("salary", "apt_price", "fee", mode="before")
    def salary_validator(cls, v: str) -> int:
        if isinstance(v, str):
            v = v.replace("kr", "").strip()
        return int(v)


def calculator(values: UserVal, rent=3.5, threshold=50):
    rent_price_month = (values.apt_price * (rent/100)) / 12 # 1000000 * 0.035 / 12 = 2900
    decimal_threshold = threshold / 100 # 0.5
    rest = int(values.salary - (rent_price_month + values.fee))
    salary_threshold = int(values.salary * decimal_threshold)
    # 30000 - 2900 + 5000(7900) = om 22100 <= 15000
    if rest <= salary_threshold:
        result = False
        #return (False, rest, salary_threshold)
    else:
        result =True 
    return Calculator(result=result, rest=rest, threshold=salary_threshold)

        #return (True, rest, salary_threshold)
    
# calculator(30000, 1000000, 3.5, 5000, 50)

def user_input():
    user_salary = input("Månadslön: ")#.replace("kr","").strip())
    apt_price = input("Lägenhetspris: ")#.replace("kr","").strip())
    fee = input("Månadsavgift: ")#.replace("kr","").strip())
    values= UserVal(salary=user_salary, apt_price=apt_price, fee=fee)
    calc = calculator(values)
    if calc.result:
        print(f"Grattis, du har råd. Du har {calc.rest}kr kvar att leva på")
    else:
        print(f"Tyvärr, du har inte råd. Du skulle ha {calc.rest}kr kvar att leva på. Du måste ha minst {calc.threshold}kr kvar att leva på")

if __name__ == "__main__":
    user_input()