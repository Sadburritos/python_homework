import random
import datetime

class Person:
    def __init__(self, name, iin):
        self.name = name
        self.iin = iin
        self.order = None

class Order:
    def __init__(self, hotel_name, room, date_from, date_to, visitor_name, visitor_iin):
        self.hotel_name = hotel_name
        self.id = random.randint(1000, 9999)
        self.room = room
        self.date_from = date_from
        self.date_to = date_to
        self.visitor_name = visitor_name
        self.visitor_iin = visitor_iin

    def show_info(self):
        print(f"Бронь #{self.id} в гостинице {self.hotel_name}")
        print(f"Номер комнаты: {self.room.number}")
        print(f"Дата заезда: {self.date_from}")
        print(f"Дата выезда: {self.date_to}")
        print(f"Посетитель: {self.visitor_name} (ИИН: {self.visitor_iin})")

class Room:
    def __init__(self, number, hotel, bedrooms=1):
        self.number = number
        self.bedrooms = bedrooms
        self.order = None
        self.hotel = hotel

    def is_empty(self, date=None):
        if date is None:
            date = datetime.date.today()
        if self.order:
            return date < self.order.date_from or date > self.order.date_to
        return True

    def show_info(self):
        print(f"Номер комнаты: {self.number}")
        print(f"Количество спален: {self.bedrooms}")
        if self.order:
            print(f"Забронирована до: {self.order.date_to}")
            print(f"Посетитель: {self.order.visitor_name} (ИИН: {self.order.visitor_iin})")

class Hotel:
    def __init__(self, name, balance, room_count):
        self.name = name
        self.balance = balance
        self.rooms = [Room(number=i+1, hotel=self, bedrooms=(i % 2) + 1) for i in range(room_count)]

    def get_price(self, room_number, date_from, date_to):
        room = self.rooms[room_number - 1]
        total_days = (date_to - date_from).days
        price = room.bedrooms * total_days * 1000
        return price

    def buy_order(self, room_number, date_from, date_to, visitor):
        room = self.rooms[room_number - 1]
        price = self.get_price(room_number, date_from, date_to)
        if room.is_empty(date_from):
            if self.balance >= price:
                order = Order(self.name, room, date_from, date_to, visitor.name, visitor.iin)
                room.order = order
                self.balance -= price
                visitor.order = order
                print(f"{visitor.name} успешно забронировал(а) номер {room_number} в гостинице {self.name}.")
            else:
                print(f"Недостаточно средств для бронирования номера {room_number}.")
        else:
            print(f"Номер {room_number} уже занят на указанные даты.")

    def check_in(self, visitor, date):
        if visitor.order:
            if date >= visitor.order.date_from and date <= visitor.order.date_to:
                print(f"{visitor.name} успешно заселился в номер {visitor.order.room.number}.")
            else:
                print(f"{visitor.name}, вы не можете заселиться в номер {visitor.order.room.number} в данную дату")
        else:
            print(f"{visitor.name}, у вас нет активных броней")

    def check_out(self, visitor, date):
        if visitor.order:
            if date > visitor.order.date_to:
                total_days = (date - visitor.order.date_to).days
                price = visitor.order.room.bedrooms * total_days * 1000
                self.balance += price
                print(f"{visitor.name}, вы успешно выселились из номера {visitor.order.room.number}.")
                print(f"Оплачено дополнительных {price} тенге за проживание")
                visitor.order.room.order = None
                visitor.order = None
            else:
                print(f"{visitor.name}, вы не можете выселиться из номера {visitor.order.room.number} до {visitor.order.date_to}.")
        else:
            print(f"{visitor.name}, у вас нет активных броней")


hotel = Hotel("Отель Отельский", 100000, 10)

person1 = Person("Иванов Иван", "123456789012")
person2 = Person("Глебов Глеб", "987654321012")

hotel.buy_order(2, datetime.date(2023, 1, 10), datetime.date(2023, 1, 15), person1)
hotel.buy_order(4, datetime.date(2023, 2, 5), datetime.date(2023, 2, 10), person2)

room_number = 2
date_to_check_in = datetime.date(2023, 1, 12)
hotel.check_in(person1, date_to_check_in)

room_number = 4
date_to_check_out = datetime.date(2023, 2, 12)
hotel.check_out(person2, date_to_check_out)

room_number = 4
date_to_check_out = datetime.date(2023, 2, 8)
hotel.check_out(person2, date_to_check_out)
