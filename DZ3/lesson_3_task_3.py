from address import Address
from mailing import Mailing

mailing1 = Mailing(
    Address(636363, "Moscow", "Pushkina", 44, 2),
    Address(252525, "Novosibirsk", "Frunze", 47, 123),
    654.32,
    "1245789632"
)

print("Отправление " + mailing1.track + " из " + mailing1.from_adress.str() + " в " + mailing1.to_adress.str() + ". " + "Стоимость " + str(mailing1.cost) + " рублей.")