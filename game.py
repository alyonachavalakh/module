import exceptions
import models



def play():
    name = print(input('Welcome to the game! Please enter your name here: '))
    player_one = models.Player(name)
    enemy_one = models.Enemy()
    while True:
        try:
            player_one.attack(enemy_one)
            player_one.defence(enemy_one)

        except exceptions.EnemyDown:
            if enemy_one.lives == 0:
                player_one.lives += 5
                enemy_two = models.Enemy()
        except exceptions.GameOver:
            with open('scores.txt', 'a+') as file:
                file.write(player_one.name + ' ' + player_one.score + '\n')
            raise

try:
    play()
except exceptions.GameOver:
    print('Game over!')
except KeyboardInterrupt:
    pass
finally:
    print('Good bye!')