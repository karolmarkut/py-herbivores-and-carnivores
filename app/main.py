class Animal:
    alive = []
    def __init__(self, name):
        self.name = name
        self._health = 100
        self.hidden = False
        Animal.alive.append(self)

    def _check_death(self):
        if self.health <= 0:
            self.health = 0
            if self in Animal.alive:
                Animal.alive.remove(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    class Herbivore(Animal):
        def hide(self):
            self.hidden = not self.hidden

    class Carnivore(Animal):
        def bite(self, target):
            if isinstance(target, Herbivore) and not target.hidden:
                target.health -= 50
                target._check_death()