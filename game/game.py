import exceptions
import models
import settings


def play():
    name = input('Welcome to the game! Please enter your name to start: ')
    player_one = models.Player(name)
    enemy_one = models.Enemy()
    while True:
        try:
            player_one.attack(enemy_one)
            player_one.defence(enemy_one)
        except exceptions.GameOver:
            with open('scores.txt', 'a+') as file:
                file.write(str(player_one.name) + ' ' + str(player_one.score) + '\n')
            break
        except exceptions.EnemyDown:
            print('Your enemy has been slain \n New enemy is ready to fight. ')
            player_one.score += 5
            enemy_two = models.Enemy()
            while True:
                player_one.attack(enemy_two)
                player_one.defence(enemy_two)
                if player_one.lives == 0 or enemy_two.lives == 0:
                    break


def show_scores():
    with open('scores.txt') as f:
        for line in f:
            print(line)


def main_menu():
    print('Main menu: \n 1.show scores \n 2.exit \n 3.help \n Please choose your option')
    choice = input()
    if choice == '1':
        show_scores()
    if choice == '2':
        print('Thank you! Good bye!')
    if choice == '3':
        print('- 1.about the game \n - 2.instruction \n - 3.contact us')
        choice2 = input()
        if choice2 == '1':
            desc = settings.about_the_game
            print(desc)
        if choice2 == '2':
            inst = settings.instruction
            print(inst)
        if choice2 == '3':
            cont = settings.contact_us
            print(cont)


try:
    play()
    main_menu()
except exceptions.GameOver:
    print('Game over!')
except exceptions.EnemyDown:
    pass
except KeyboardInterrupt:
    pass
except ValueError:
    pass
finally:
    print('Good bye!')
