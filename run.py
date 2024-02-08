# by Kwizera Africa Hubert Bonaparte


class Smartphone:
    def __init__(self, type, size, color):
        self.type = type
        self.size = size
        self.color = color

# Createan array
smartphones = []

#adding attributes  to the array
smartphones.append(Smartphone("Android", 60, "red"))
smartphones.append(Smartphone("iPhone", 50, "blue"))
smartphones.append(Smartphone("Android", 70, "white"))
smartphones.append(Smartphone("Android", 50, "black"))
smartphones.append(Smartphone("Android", 60, "purple"))
smartphones.append(Smartphone("iPhone", 60, "black"))
smartphones.append(Smartphone("Android", 50, "green"))
smartphones.append(Smartphone("iPhone", 70, "yellow"))
smartphones.append(Smartphone("iPhone", 80, "purple"))
smartphones.append(Smartphone("Android", 60, "yellow"))

while True:
    # Print table
    print("|---------------------------------|")
    print("|    Type    | Size  |   Color    |")
    print("|------------|-------|------------|")
    for smartphone in smartphones:
        print(f"| {smartphone.type:<10} | {smartphone.size:<5} | {smartphone.color:<10} |")
    print("|            |       |            |")
    print("|---------------------------------|")

    # propmt to a user if they want to add new element
    
    user_input = input("Do you want to add a new smartphone? (Yes/No): ").strip().lower()
    
    if user_input == "no":
        break
    elif user_input == "yes":
        
        # Prompt the user for smartphone details
        
        new_type = input("Enter the smartphone type: ")
        new_size = int(input("Enter the size: "))
        new_color = input("Enter the color: ")

        # Create a new smartphone object and add it to the array
        
        new_smartphone = Smartphone(new_type, new_size, new_color)
        smartphones.append(new_smartphone)
