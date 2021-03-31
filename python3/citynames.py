def city_country(city, country):
    message = print(f"{city} is in the {country}! ")
    return message

city_n = input("What is the city called? ")
country_n = input("Where is it located? ")

final_message = city_country(city_n , country_n)
print(final_message)