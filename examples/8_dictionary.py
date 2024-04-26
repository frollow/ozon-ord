from ozon_ord.dictionary import Dictionary
from ozon_ord.models import (
    BankDictionaryRequest,
    CountryDictionaryRequest,
    FiasDictionaryRequest,
    OkvedDictionaryRequest,
)

# Справочник с данными банков (поиск для одного банка по БИК)
request_data = BankDictionaryRequest(search="044525652", pageSize=5)

response = Dictionary.get_bank_info(request_data)
print(response[0].address)
print(response)


# Справочник с данными банков (выводит 5 элементов)
request_data = BankDictionaryRequest(search="", pageSize=5, gtBik="")

response = Dictionary.get_bank_info(request_data)
print(response[0].address)
print(response[1].address)
print(response)


# Справочник идентификаторов стран ОКСМ (поиск по одной стране)
request_data = CountryDictionaryRequest(search="RU")

response = Dictionary.get_country_info(request_data)
print(response)
print(response[0].shortName)

# Справочник идентификаторов стран ОКСМ (показать все элементы)
request_data = CountryDictionaryRequest(search="")

response = Dictionary.get_country_info(request_data)
print(response)


# Справочник ФИАС (поиск по одному адресу)
request_data = FiasDictionaryRequest(search="город Славгород")

response = Dictionary.get_fias_info(request_data)
print(response)
print(response[0].path)

# Справочник идентификаторов стран ОКСМ (показать все элементы)
request_data = FiasDictionaryRequest(search="")

response = Dictionary.get_fias_info(request_data)
print(response)


# Справочник по видам экономической деятельности (ОКВЭД) (поиск по одному номеру или названию ОКВЭД)
request_data = OkvedDictionaryRequest(search="98.10")

response = Dictionary.get_okved_info(request_data)
print(response)
print(response[0].name)

# Справочник по видам экономической деятельности (ОКВЭД) (показать все элементы)
request_data = OkvedDictionaryRequest(search="")

response = Dictionary.get_okved_info(request_data)
print(response)
