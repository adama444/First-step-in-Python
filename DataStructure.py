social_networks = ["Instagram", "Twitter", "Facebook"]
print(social_networks[0])
programming_language = "Python"
print(programming_language[1])
print(programming_language[-1])
social_networks.append("Tiktok")
print(social_networks)
social_networks.remove("Twitter")
print(social_networks)
print("The length of variable social_networks is", len(social_networks))
print("Before sorting")
print(social_networks)
print("After sorting")
social_networks.sort()
print(social_networks)

social_networks = ("Twitter", "Instagram")
print(social_networks)
print("Data structure as tuple is immutable")

student = {
    "id": "2018-UUT-IN9039-ISTIN",
    "full_name": "Adama SAMAKE",
    "nationality": "Malian"
}
print(student["full_name"])
student["birth_day"] = "04-11-2002"
print(student)
student["nationality"] = "Malian and Togolese"
print(student)
del student["birth_day"]
print(student)
print("birth_day" in student)
