
class Fighter:
    def __init__(self, name, health, damagePerAttack):
        self.name = name
        self.health = health
        self.damagePerAttack = damagePerAttack

    def __del__(self):
        print(f"Боєць {self.name} видалений")

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_damage(self):
        return self.damagePerAttack

    def set_name(self, name):
        self.name = name

    def set_health(self, health):
        self.health = health

    def set_damage(self, damage):
        self.damagePerAttack = damage

    def __str__(self):
        return (
            f"Ім'я: {self.name}; "
            f"Здоров'я: {self.health}; "
            f"Урон: {self.damagePerAttack}"
        )


class Fight:
    def __init__(self, fighter1, fighter2):
        self.fighter1 = fighter1
        self.fighter2 = fighter2

    def __del__(self):
        print("Об'єкт поєдинку видалений")

    def get_fighter1(self):
        return self.fighter1

    def get_fighter2(self):
        return self.fighter2

    def set_fighter1(self, fighter):
        self.fighter1 = fighter

    def set_fighter2(self, fighter):
        self.fighter2 = fighter

    def __str__(self):
        return (
            f"Поєдинок: {self.fighter1.name} "
            f"проти {self.fighter2.name}"
        )

    def get_winner(self):
        if (self.fighter1.damagePerAttack <= 0 and self.fighter2.damagePerAttack <= 0):
            return None

        while True:
            self.fighter2.health -= self.fighter1.damagePerAttack

            if self.fighter2.health <= 0:
                return self.fighter1.name

            self.fighter1.health -= self.fighter2.damagePerAttack

            if self.fighter1.health <= 0:
                return self.fighter2.name


def main():
    fighter1 = Fighter("Ігор", 100, 20)
    fighter2 = Fighter("Олег", 80, 15)

    print(fighter1)
    print(fighter2)

    fighter1.set_health(120)
    print(f"Нове здоров'я для {fighter1.get_name()}:", fighter1.get_health())

    fight = Fight(fighter1, fighter2)
    print(fight)

    winner = fight.get_winner()

    if winner is None:
        print("Нічия")
    else:
        print("Переможець:", winner)

    print("Після бою:")
    print(fighter1)
    print(fighter2)

    del fight
    del fighter1
    del fighter2


if __name__ == "__main__":
    main()
