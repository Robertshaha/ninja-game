import random

class NinjaGame:
    def __init__(self):
        self.level = 1
        self.inventory = []
        self.opponents = {
            "Самурай": 20, 
            "Шиноби": 15, 
            "Демон": 30
        }
        self.mission = {
            1: "Соберите 3 ключа, чтобы открыть скрытую дверь.",
            2: "Победите самурая и получите амулет.",
            3: "Избегите демона и найдите свиток мудрости."
        }
        self.keys = set()
        self.opponent = None
        self.game_state = True
        self.stats = {
            "здоровье": 100,
            "атака": 10
        }

    def start_game(self):
        print("Добро пожаловать в NinjaGame! На дворе 1850-ый год, вы являетесь личным ниндзей сегуната в провинции Вано, и он дал вам новое поручение. Спешите обрадовать своего сегуна и заполучите дрогоценный амулет!")
        while self.game_state and self.level <= 3:
            print(f"\\n--- Уровень {self.level} ---")
            self.level_game(self.level)
            if self.level < 3:
                continue_choice = input("Хотите продолжить к следующему уровню? (да/нет): ").lower()
                if continue_choice != "да":
                    print("Вы решили выйти из игры.")
                    break
            self.level += 1
        print("Спасибо за игру. Вы завершили все уровни!")

    def level_game(self, level):
        if level == 1:
            self.level_1()
        elif level == 2:
            self.level_2()
        elif level == 3:
            self.level_3()

    def level_1(self):
        print(self.mission[1])
        while len(self.keys) < 3:
            action = input("Что делать? (взять ключ/посмотреть инвентарь/проверить ключи): ").lower()
            if action == "взять ключ":
                key = f"Ключ{len(self.keys) + 1}"
                self.keys.add(key)
                print(f"Вы взяли {key}.")
            elif action == "посмотреть инвентарь":
                self.out_inventory()
            elif action == "проверить ключи":
                print(f"У вас {len(self.keys)} ключа(ей) из 3.")
                if len(self.keys) == 3:
                    print("Вы собрали все ключи и открыли скрытую дверь на следующий уровень!")
                    break
            else:
                print("Неверное действие.")

    def level_2(self):
        self.opponent = "Самурай"
        print(f"Вы встретили {self.opponent} с {self.opponents[self.opponent]} HP!")
        while self.opponents[self.opponent] > 0:
            action = input("Что делать? (атаковать/убежать/посмотреть инвентарь): ").lower()
            if action == "атаковать":
                damage = random.randint(5, 10)
                self.opponents[self.opponent] -= damage
                print(f"Вы атаковали {self.opponent}. Урон: {damage}. Осталось HP: {self.opponents[self.opponent]}.")
                if self.opponents[self.opponent] <= 0:
                    print(f"Вы победили {self.opponent}!")
                    print("Вы получили амулет!")
                    self.inventory.append("Амулет")
            elif action == "убежать":
                print("Вы убежали из боя!")
                return 
            elif action == "посмотреть инвентарь":
                self.out_inventory()
            else:
                print("Неверное действие.")

    def level_3(self):
        self.opponent = "Демон"
        print(self.mission[3])
        print(f"Вы встретили {self.opponent} с {self.м[self.opponent]} HP!")
        while self.opponents[self.opponent] > 0:
            action = input("Что делать? (избежать/атаковать/посмотреть инвентарь): ").lower()
            if action == "атаковать":
                damage = random.randint(10, 20)
                self.opponents[self.opponent] -= damage
                print(f"Вы атаковали {self.opponent}. Урон: {damage}. Осталось HP: {self.opponents[self.opponent]}.")
                if self.opponents[self.opponent] <= 0:
                    print("Вы победили демона и спасли мир!")
                    self.inventory.append("Святой Свиток")
                    break
            elif action == "избежать":
                print("Вы решили избежать встречи с демоном!")
                break
            elif action == "посмотреть инвентарь":
                self.out_inventory()
            else:
                print("Неверное действие.")

    def out_inventory(self):
        if self.inventory:
            print("Ваш инвентарь:")
            for object in self.inventory:
                print(f"- {object}")
        else:
            print("Ваш инвентарь пуст!")

    def get_stats(self):
        print("\\n--- Статистика ---")
        print(f"Уровень: {self.level}")
        print(f"Ключи: {len(self.keys)} из 3")
        print(f"Здоровье: {self.stats['здоровье']}")
        print(f"Атака: {self.stats['атака']}")
        self.out_inventory()

if __name__ == "__main__":
    игра = NinjaGame()
    игра.start_game()