#coding=utf-8

import abc


class SensitiveInfo(metaclass=abc.ABCMeta):

    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']

    @abc.abstractmethod
    def read(self):
        print('There are {} users: {}'.format(len(self.users), ','.join(self.users)))

    @abc.abstractmethod
    def add(self, user):
        self.users.append(user)
        print('Added user {}'.format(user))

    @abc.abstractmethod
    def remove(self, user):
        self.users.remove(user)
        print('Removed user {}'.format(user))


class ConcreteOverride(SensitiveInfo):
    def read(self):
        super(ConcreteOverride, self).read()

    def add(self, user):
        super(ConcreteOverride, self).add(user)

    def remove(self, user):
        super(ConcreteOverride, self).remove()


class Info:
    """SensitiveInfo的保护代理"""
    def __init__(self):
        self.protected = ConcreteOverride()
        self.secret = '0xdeadbeef'

    def read(self):
        self.protected.read()

    def add(self, user):
        sec = input('what is the secret? ')
        self.protected.add(user if sec == self.secret else print("That's wrong!"))

    def remove(self, user):
        sec = input('what is the secret? ')
        self.protected.remove(user if sec == self.secret else print("That's wrong!"))


def main():
    info = Info()
    while 1:
        print('1. read list |==| 2. add user |==| 3. remove user |==| 4. quit')
        key = input('choose option: ')
        if key == '1':
            info.read()
        elif key == '2':
            name = input('choose username: ')
            info.add(name)
        elif key == '3':
            name = input('choose username: ')
            info.remove(name)
        elif key == '4':
            exit()
        else:
            print('unknown option: {}'.format(key))

if __name__ == '__main__':
    main()