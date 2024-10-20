from address import Address
from mailing import Mailing

to_address = Address("2344567", "Сызрань", "Блюхера", "24", "38")
from_address = Address("5651929", "Москва", "Щорса", "37", "22")


mailing = Mailing(to_address, from_address, 2100, "4586")


print(f"Отправка {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
       f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.flat}"
       f" в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
       f" {mailing.to_address.house} - {mailing.to_address.flat}. "
       f" Стоимость {mailing.cost} рублей.")