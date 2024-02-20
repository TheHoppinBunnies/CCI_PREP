def spice_level(spice_list):
    Poblano = 1500
    Mirasol = 6000
    Serrano = 15500
    Cayenne = 40000
    Thai = 75000
    Habanero = 125000

    spice_level = 0

    for spice in spice_list:
        if spice == "Poblano":
            spice_level += Poblano

        elif spice == "Mirasol":
            spice_level += Mirasol

        elif spice == "Serrano":
            spice_level += Serrano

        elif spice == "Cayenne":
            spice_level += Cayenne

        elif spice == "Thai":
            spice_level += Thai

        elif spice == "Habanero":
            spice_level += Habanero

    return spice_level


number_of_spices = int(input())
spice_list = [str(input()) for _ in range(number_of_spices)]
print(spice_level(spice_list))