import random
from actors import Player, Enemy, Ogre, Imp

class Game:
    def __init__(self, player, enemies):
        self.player = player
        self.enemies = enemies

      def main():
        print_intro()
        play()

      def print_intro():
          print('''
            Monster Slash!!!
            Ready Player One!
            [Press Enter to Continue]
            ''')
            input()

  def play():
          enemies = [
            Enemy('Ogre', 1),
            Enemy('Imp', 1)
          ]
          player = Player('Hercules', 1)
          print(enemies)
          print(player)
          while True:
              next_enemy = random.choice(enemies)
              cmd = input('You see a {}. [R]un, [A]ttack, [P]ass ').format(next_enemy.kind)
            if cmd == 'R':
                print('{} runs away!'.format(player.name))
                print('{} heals thyself!'.format(self.player.name))
                self.player.heal()
                print(self.player.hp)
            elif cmd == 'A':
                self.player.attacks(next_enemy
                if not next_enemy.is_alive():
                    self.enemies.remove(next_enemy)
                    next_enemy = None
                    if next_enemy:
                    next_enemy_attacks(self.player)
                if not self.player.is_alive():
                    print('Game over!')
                    break
            elif cmd == 'P':
                print ('You are still considering your next move')
                if random.randint(1,11) < 5:
                    next_enemy.attacks(self.player)
            else:
                print('Please choose a valid option');

                self.print_linebreak()
                self.player.stats()
                for e in self.enemies:
                    e.stats()
                self.print.linebreak()
        print()
        print('*'*30)
        print()

        if not enemies:
            print('You win!  Congrats!')
            break;

  if __name__ == '__main__':
    main()

 enemies = [
   Enemy('Bob', 1, , 'Ogre'),
   Enemy('Alice', 1, 'Imp')
 ]
 player = Player('Hercules', 1)
 game = Game(player, enemies)
 print (game.player)
 print (game.enemies)
