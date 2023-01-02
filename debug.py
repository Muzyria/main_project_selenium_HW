
from faker import Faker

faker_ru = Faker("ru_RU")
faker_en = Faker("en")

Faker.seed()

# class Person:
#     full_name: str = None
#     firstname: str = None
#     lastname: str = None
#     age: int = None
#     salary: int = None
#     department: str = None
#     email: str = None
#     current_address: str = None
#     permanent_address: str = None
#     mobile: str = None
#     # subject: str = None

def generated_person():
    for item in [faker_ru.first_name(), faker_ru.middle_name(),faker_ru.first_name(), faker_ru.last_name()]:
        yield item
        # age=random.randint(10, 80),
        # salary=random.randrange(10000, 100000, 10000),
        # department=faker_ru.job(),
        # email=faker_ru.email(),
        # current_address=faker_ru.address(),
        # permanent_address=faker_ru.address(),
        # mobile=faker_ru.msisdn()
        # subject=generated_subject()

coun = generated_person()
print(next(coun))
print(next(coun))
print(next(coun))
print(next(coun))
