import pygame

class Character:
    def __init__(self, name, description, path):
        self.name = name
        self.description = description
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (350, 400))



characters = [Character("Alice", "Always positive", "images/alice.webp"),
    Character("Clara", "Has her own business", "images/clara.webp"),
    Character("Kamila", "Professional model", "images/kamila.jpeg"),
    Character("Bob", "Enjoys sunbathing", "images/bob.webp"),
    Character("Simon", "Very funny", "images/simon.webp"),
    Character("Rayan", "Likes to drive", "images/rayan.png"),
    Character("Rick", "Likes to sing", "images/rick.png"),]


