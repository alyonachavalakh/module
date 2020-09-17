import random
import exceptions
import settings


class Enemy:

    def __init__(self):
        self.lives = settings.lives

    def enemy_decrease_lives(self):
        if self.lives >= 1:
            self.lives -= 1
        if self.lives == 0:
            raise exceptions.EnemyDown

    @staticmethod
    def select_attack():
        return random.randint(1, 3)


class Player:
    allowed_attacks = (1,2,3)

    def __init__(self, name):
        self.name = str(name)
        self.lives = settings.lives
        self.score = 0

    def decrease_lives(self):
        if self.lives >= 1:
            self.lives -= 1
        if self.lives == 0:
            raise exceptions.GameOver

    @staticmethod
    def fight(attack, defence):
        if (attack == 1 and defence == 2) \
                or (attack == 2 and defence == 3) \
                or (attack == 3 and defence == 1):
            return 1
        if attack == defence:
            return 0
        if attack > 3 or defence > 3:
            print('Please choose between 1, 2, 3')
        else:
            return -1

    def attack(self, enemy_obj):
        player_attack = int(input('Please make your choice: \n 1.wizard, 2.warrior, 3. robber \n'))
        fight_result = self.fight(player_attack, enemy_obj.select_attack())
        if fight_result == 0:
            print("It's a draw!")
        if fight_result == 1:
            enemy_obj.enemy_decrease_lives()
            self.score += 1
            print("You attacked successfully! \n Your enemy lives are now: ", enemy_obj.lives,
                  "\n Your lives are: ", self.lives)
        if fight_result == -1:
            self.decrease_lives()
            print("You missed! \n Your lives are now: ", self.lives, "\n Your enemy lives are: ", enemy_obj.lives)

    def defence(self, enemy_obj):
        player_defence = int(input('Please make your choice: \n 1.wizard, 2.warrior, 3. robber \n'))
        fight_result = self.fight(enemy_obj.select_attack(), player_defence)
        if fight_result == 0:
            print("It's a draw!")
        if fight_result == 1:
            self.decrease_lives()
            print("You missed!\n Your lives are now: ", self.lives, "\n Your enemy lives are: ", enemy_obj.lives)
        if fight_result == -1:
            self.score += 1
            enemy_obj.enemy_decrease_lives()
            print("You attacked successfully! \n Your enemy lives are now: ",
                  enemy_obj.lives, "\n Your lives are: ", self.lives)








