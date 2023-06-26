'''
Create a program to accept the Dog breed and display related information that breed pull the data from the Dog
API and put it into Word file but don't use Document module and the file name should the the Dog breed name
which is input from the user
'''
import requests


def get_dog_breed_info(self):
    url = f"https://api.thedogapi.com/v1/breeds/search?q={breed}"
    response = requests.get(url)
    data = response.json()
    # return data[0]
    if data:
        return data[0]
    else:
        return None


breed = input("Enter the dog breed: ")
breed_info = get_dog_breed_info(breed)
print(breed_info)

if breed_info:
    filename = f"{breed_info['name']}_info.docs"
    with open(filename, 'w') as file:
        file.write(f"Information of {breed_info['name']}:\n")
        for key, value in breed_info.items():
            file.write(f"{key}:{value}\n")
else:
    print("Breed information not found")
