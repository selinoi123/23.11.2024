israel_info = {
    "name": "Israel",
    "birth": 1948,
    "population_millions": 9.3,
    "capital": "Jerusalem",
    "language": "Hebrew",
    "cities": ["Jerusalem", "Tel Aviv", "Haifa", "Rishon LeZion", "Petah Tikva", "Ashdod"],
    "currency": "ILS",
    "area_kilometer": 22145,
    "gdp_billion": 450
}
#START Question 1a
print(israel_info.get("capital"))
#END

#START Question 1b
print(israel_info.keys())
#END

#START Question 1c
print(israel_info.values())
#END

#START Question 1d
for key, value in israel_info.items():
    print(f"{key}: {value}")
#END

#START Question 1e
copy_israel_info = israel_info.copy()
#END

#START Question 1f
copy_israel_info = copy_israel_info.pop("gdp_billion")
#END

#START Question 1g
keys = ['name', 'birth', 'population_millions', 'capital', 'language', 'cities', 'currency', 'area_kilometer', 'gdp_billion']

new_dict = dict.fromkeys(keys, None)

new_dict['name']: str = str(input("Enter the country name: "))
new_dict['birth']: int = int(input("Enter the year the country was founded: "))
new_dict['population_millions']: float = float(input("Enter the population in millions: "))
new_dict['capital']: str = str(input("Enter the capital city: "))
new_dict['language']: str = str(input("Enter the official language: "))
new_dict['currency']: str = str(input("Enter the currency: "))
new_dict['area_kilometer']: int = int(input("Enter the area in square kilometers: "))
new_dict['gdp_billion']: float = float(input("Enter the GDP in billions: "))

print("Enter 3 cities:")
cities = []

for i in range(3):
    city_name: str = str(input(f"City {i + 1}: "))
    cities.append(city_name)

new_dict['cities'] = cities
print(new_dict)
#END

#START Question 2
#Example 1:
Input1: str = "Hello World"
last_word_length: list[str] = Input1.split()
print(len(last_word_length[-1]))

#Example 2:
Input2: str = "fly me   to   the moon"
last_word_length2: list[str] = Input2.split()
print(len(last_word_length2[-1]))

#Example 3:
Input3: str = "luffy is still joyboy"
last_word_length3: list[str] = Input3.split()
print(len(last_word_length3[-1]))

#END