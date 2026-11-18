from enum import Enum


class gender(Enum):
    FEMALE = "Жіноча"
    MALE = "Чоловіча"
    NON_BINARY = "Небінарна"
    OTHER = "Інша"


class Guest:
    def __init__(self, guest_id: int, name: str, age: int, city: str, phone_number: str, guest_gender: gender):
        self.__id = guest_id
        self.__name = name
        self.__age = age
        self.__city = city
        self.__phone_number = phone_number
        self.__gender = guest_gender

    def __del__(self):
        pass

    def get_id(self):
        return self.__id

    def set_id(self, guest_id: int):
        self.__id = guest_id

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age: int):
        if age < 0:
            raise ValueError("Вік не може бути від'ємним.")
        self.__age = age

    def get_city(self):
        return self.__city

    def set_city(self, city: str):
        self.__city = city

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number: str):
        self.__phone_number = phone_number

    def get_gender(self):
        return self.__gender

    def set_gender(self, guest_gender: gender):
        self.__gender = guest_gender

    def isLuckyPhoneNumber(self):
        return self.__phone_number.count("7") > 3

    def print_info(self):
        lucky = "Так" if self.isLuckyPhoneNumber() else "Ні"
        print(
            f"ID: {self.__id:<3} | Ім'я: {self.__name:<18} | Вік: {self.__age:<2} | "
            f"Місто: {self.__city:<10} | Стать: {self.__gender.value:<10} | "
            f"Телефон: {self.__phone_number} (Щасливий: {lucky})"
        )


class Party:
    def __init__(self, day: str, reason: str, guests: list[Guest] | None = None):
        self.__day = day
        self.__reason = reason
        self.__guests = list(guests) if guests is not None else []

    def __del__(self):
        pass

    def get_day(self):
        return self.__day

    def set_day(self, day: str):
        self.__day = day

    def get_reason(self):
        return self.__reason

    def set_reason(self, reason: str):
        self.__reason = reason

    def get_guests(self):
        return self.__guests

    def set_guests(self, guests: list[Guest]):
        self.__guests = guests

    def add_guest(self, guest: Guest):
        self.__guests.append(guest)

    def sort_guests_by_id(self):
        self.__guests.sort(key=lambda guest: guest.get_id())

    def print_info(self):
        print(f"Подія: {self.__reason} | Дата: {self.__day} | Кількість гостей: {len(self.__guests)}")
        print("-" * 95)
        for guest in self.__guests:
            guest.print_info()
        print("-" * 95)


def findAverageAge(guests: list[Guest], target_gender: gender):
    ages = [g.get_age() for g in guests if g.get_gender() == target_gender]
    return sum(ages) / len(ages) if ages else 0.0


def main():
    guests_list = [
        Guest(4, "Ірина", 23, "Київ", "+380977771277", gender.FEMALE),
        Guest(1, "Тарас", 30, "Львів", "+380507771234", gender.MALE),
        Guest(3, "Софія", 25, "Вінниця", "+380671234567", gender.FEMALE),
        Guest(2, "Максим", 26, "Одеса", "+380937777890", gender.MALE),
        Guest(5, "Робін", 27, "Дніпро", "+380637707711", gender.NON_BINARY)
    ]


    party = Party("П'ятниця, 18:00", "Річниця компанії", guests_list)

    print("=== Список гостей до сортування ===")
    party.print_info()

    party.sort_guests_by_id()
    print("\n=== Список гостей після сортування за ID ===")
    party.print_info()

    for guest in party.get_guests():
        print(guest.get_age(), guest.get_name())

    print("\n=== Середній вік гостей за статтю ===")
    for g_type in (gender.FEMALE, gender.MALE, gender.NON_BINARY):
        avg = findAverageAge(party.get_guests(), g_type)
        print(f"{g_type.value}: {avg:.1f} р.")



if __name__ == "__main__":
    main()