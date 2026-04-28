from prettytable import PrettyTable

pokemon_table = PrettyTable()
pokemon_table.header = True

"""pokemon_table.align = "l"""
"""Changing attribute before finish creating the table won't do anything"""



pokemon_table.add_column(
    "Pokemon Name",
    [
        "Pikachu",
        "Squirtle",
        "Charmander",
    ]
                         
)

pokemon_table.add_column(
    "Type",
    [
        "Electric",
        "Water",
        "Fire",
    ]
)
pokemon_table.align = "l"
print(pokemon_table)