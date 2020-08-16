    from random import randint

    class Actor:
        def __init))(self, name, level):
            self.name = name
            self.level = level
            self.hp = 100 * level

            def __repr__(self):
                return ('<Actor: {} at Level {}>'.format(self.name,self.level))

            def get_attack_power(self):
                return randint (1, 100) * self.level

                def is_alive(self):
                    return self.hp > 0

                def stats(self):
                    print('{} has {} HP'.format(self.name, self.hp))

                def attacks(self, other):
                    raise NotImplementedError()

        class Player(Actor):
            def __init__(self, name, level)
                self.name = name
                self.level = level

                def heal(self):
                    self.hp += 10

            def __repr__(self):
                return ('<Player: {} at Level {}>'
                            .format(self.name,
                                    self.level))

            def get_attack_power(self):
                return randint (1, 100) * self.level

            def attacks(self, enemy):
                power = self.get_attack_power()
                enemy_power = enemy.get_attack_power()
                print('You summon {} power!'.format(power))
                print('{} summons {}power!'.format(enemy.kind, enemy_power))

                if power >= enemy_power:
                    print('You slay the{}!'.format(enemy.kind))
                    return True
                else:
                    print('You were Defeated!')
                    return False

        class Enemy(Actor):
            def __init__(self,name , level, kind)
            super().__init__(name, level)
                self.kind = kind
                self.level = Level

            def __repr__(self):
            return '<Enemy: {}>'.format(self.kind)'

            def attacks(self, player):
                print('{} the {} attack {}'.format(self.name, self.kind, player))
                e_power = self.get_attack_power()
                player_power = player.get_attack_power()
                print('{} has {} attack power'.format(self.name, e_power))

    class Ogre(enemy):
        def __init__(self, name, level, size):
            super.__init__(name, level, 'Ogre')
            self.size = size

            def get_attack_power(self)
                return randint(1, 50) * (self.size * self.level)
    class Imp(enemy):
        def __init__(self, name, level, size):
            super.__init__(name, level, 'Imp')
            self.size = size

                def get_attack_power(self)
                    return randint(1, 50) * (self.size * self.level)


                    if __name__ == '__main__':
                player = Player(name='Hercules', level=1)
                print(player)
                print(player.get_attack_power())
                enemy = Enemy(kind='Ogre', level=1)
                print(enemy)
                print(enemy.level)
                print(player.hp)
                ogre.attacks(player)
                print(player.hp)
                player.heal()
                print(player.hp)
