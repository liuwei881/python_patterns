#coding=utf-8


from enum import Enum
import time

PizzaProgress = Enum('PizzaProgress', 'queued preparation baking ready')
PizzaDough = Enum('PizzaDough', 'thin thick')
PizzaSauce = Enum('PizzaSauce', 'tomato creme_fraiche')
PizzaTopping = Enum('PizzaTopping', 'mozzarella double_mozzarella bacon ham mushrooms red_onion oregano')
STEP_DELAY = 3


class Pizza:
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        self.dough = dough
        print('preparing the {} dough of your {}...'.format(self.dough.name, self))
        time.sleep(STEP_DELAY)
        print('done with the {} dough'.format(self.dough.name))


class MargaritaBuilder:
    def __init__(self, name):
        self.pizza = Pizza(name)
        self.progress = PizzaProgress.queued
        self.baking_time = 5

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print('adding the tomato sauce to your margarita...')
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print('done with the tomato sauce')

    def add_topping(self):
        print('adding the topping (double mozzarella, oregano) to your margarita')
        self.pizza.topping.append([i for i in (PizzaTopping.double_mozzarella, PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print('done with the topping (double mozzarrella, oregano)')

    def bake(self):
        self.progress = PizzaProgress.baking
        print('baking your margarita for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your margarita is ready')


class CreamyBaconBuilder:
    def __init__(self, name):
        self.pizza = Pizza(name)
        self.progress = PizzaProgress.queued
        self.baking_time = 7

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaProgress.thick)

    def add_sauce(self):
        print('adding the creme fraiche sauce to your creamy bacon')
        self.pizza.sauce = PizzaSauce.creme_fraiche
        time.sleep(STEP_DELAY)
        print('done with the creme fraiche sauce')

    def add_topping(self):
        print('adding the topping (mozzarella, bacon, ham ,mushrooms, red onion, oregano) to your creamy bacon')
        self.pizza.topping.append([t for t in (PizzaTopping.mozzarella,
                                                PizzaTopping.bacon,
                                                PizzaTopping.ham,
                                                PizzaTopping.mushrooms,
                                                PizzaTopping.red_onion,
                                                PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print('done with the topping (mozarella, bacon, ham, mushrooms, red onion, oregano)')

    def bake(self):
        self.progress = PizzaProgress.baking
        print('baking your creamy bacon for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your creamy bacon is ready')


class HawaiianBuilder(MargaritaBuilder, CreamyBaconBuilder):
    def __init__(self, name):
        self.baking_time = 7
        MargaritaBuilder.__init__(self, name)
        CreamyBaconBuilder.__init__(self, name)

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        MargaritaBuilder.prepare_dough(self)

    def add_sauce(self):
        print('adding the hawaiian sauce to your hawaiian')
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print('done with the hawaiian sauce')

    def add_topping(self):
        CreamyBaconBuilder.add_topping(self)

    def bake(self):
        self.progress = PizzaProgress.baking
        print('baking your Hawaiian for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your Hawaiian is ready')


class Waiter:
    def __init__(self):
        self.builder = None

    def construct_pizza(self, builder):
        self.builder = builder
        [step() for step in (builder.prepare_dough, builder.add_sauce, builder.add_topping, builder.bake)]

    @property
    def pizza(self):
        return self.builder.pizza


def validate_style(builders):
    try:
        pizza_style = input('What pizza would you like, [m]argarita or [c]reamy bacon or [h]awaiian?')
        b = {'m': 'margarita', 'c': 'creamy', 'h': 'hawaiian'}
        builder = builders[pizza_style](b[pizza_style])
        valid_input = True
    except KeyError as err:
        print('Sorry, only margarita (key m) and creamy bacon (key c) are available')
        return (False, None)
    return (True, builder)


def main():
    builders = dict(m=MargaritaBuilder, c=CreamyBaconBuilder, h=HawaiianBuilder)
    valid_input = False
    while not valid_input:
        valid_input, builders = validate_style(builders)
    print()
    waiter = Waiter()
    waiter.construct_pizza(builders)
    pizza = waiter.pizza
    print()
    print('Enjoyu your {}!'.format(pizza))


if __name__ == '__main__':
    main()