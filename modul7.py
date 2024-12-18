import os 

os.system('cls')



    
cars = [
    {"brand": "Volvo", "model": "XC90", "year": 2020, "color": "Black"},
    {"brand": "BMW", "model": "X5", "year": 2022, "color": "White"},
    {"brand": "Tesla", "model": "Model S", "year": 2021, "color": "Red"}
]





def print_cars(car_list):
    print("\nLista över bilar:")
    for i, car in enumerate(car_list, start=1):
        print(f"Bil {i}:")
        for key, value in car.items():
            print(f"  {key.capitalize()}: {value}")
      

print_cars(cars)




print("Add new car:")

for _ in range(1):  
    brand = input("brand: ")
    model = input("model: ")
    year = int(input("year: "))
    color = input("color: ")


new_car = {"brand": brand, "model": model, "year": year, "color": color}
cars.append(new_car)


def print_cars(car_list):
    print("\n Ny listax:")
    for i, car in enumerate(car_list, start=1):
        print(f"Bil {i}:")
        for key, value in car.items():
            print(f"  {key.capitalize()}: {value}")

  
print_cars(cars)


print("\nTa bort bil:")
car_to_remove = int(input(f"Vilken bil ska bort? 1-4 (1-{len(cars)}): "))

if 1 <= car_to_remove <= len(cars):
    removed_car = cars.pop(car_to_remove - 1)  
    print(f"\nDenna försvann: {removed_car}")
else:
    print("\nInge nbil")
