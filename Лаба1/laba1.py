class Animal:
    def __init__(self, name, species, section):
        self.name = name
        self.species = species
        self.section = section

class Section:
    def __init__(self, name):
        self.name = name
        self.animals = []


class Zoo:
    def __init__(self):
        self.sections = []


def get_manul_neighbors(zoo):
    manul_neighbors = []
    
    manul_section = None
    for section in zoo.sections:
        if section.name == "Манулы":
            manul_section = section
            break
    
    if manul_section:
        for animal in manul_section.animals:
            if animal.name != "Тимофей":
                manul_neighbors.append(animal.name)
    
    return manul_neighbors


zoo = Zoo()

manul_section = Section("Манулы")
lion_section = Section("Львы")

manul_section.animals.append(Animal("Тимофей", "Манул", manul_section))
manul_section.animals.append(Animal("Барсик", "Манул", manul_section))
manul_section.animals.append(Animal("Мурзик", "Манул", manul_section))
manul_section.animals.append(Animal("Васька", "Манул", manul_section))

lion_section.animals.append(Animal("Симба", "Лев", lion_section))
lion_section.animals.append(Animal("Муфаса", "Лев", lion_section))
lion_section.animals.append(Animal("Нала", "Лев", lion_section))

zoo.sections.append(manul_section)
zoo.sections.append(lion_section)

manul_neighbors = get_manul_neighbors(zoo)
print(manul_neighbors)  
