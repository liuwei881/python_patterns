#coding=utf-8

import time

class Pizza:
    def __init__(self, builder):
        self.queued = builder.queued
        self.preparation = builder.preparation
        self.prepare_dough = builder.prepare_dough
        self.add_sauce = builder.add_sauce
        self.add_topping = builder.add_topping
        self.bake = builder.bake
        self.ready = builder.ready

    def __str__(self):
        queued = 'yes' if self.queued else 'no'
        preparation = 'yes' if self.preparation else 'no'
        prepare_dough = 'thin' if self.prepare_dough else 'no'
        add_sauce = 'tomato' if self.add_sauce else 'no'
        add_topping = ['mozzarella', 'double_mozzarella', 'bacon'] if not self.add_topping else 'no'
        bake = 'yes' if self.bake else 'no'
        ready = 'yes' if self.ready else 'no'
        info = ('queued: {}'.format(queued),
                'preparation: {}'.format(preparation),
                'prepare_dough: {}'.format(prepare_dough),
                'add_sauce: {}'.format(add_sauce),
                'add_topping: {}'.format(add_topping),
                'bake: {}'.format(bake),
                'ready: {}'.format(ready))
        return '\n'.join(info)

    class PizzaBuilder:
        def __init__(self):
            self.queued = False
            self.preparation = False
            self.prepare_dough = False
            self.add_sauce = False
            self.add_topping = []
            self.bake = False
            self.ready = False

        def add_queued(self):
            self.queued = True
            return self

        def add_preparation(self):
            self.preparation = True
            return self

        def add_prepare_dough(self):
            self.prepare_dough = True
            return self

        def _add_sauce(self):
            self.add_sauce = True
            return self

        def _add_topping(self):
            self.add_topping = []
            return self

        def add_bake(self):
            self.bake = True
            return self

        def add_ready(self):
            self.ready = True
            return self

        def build(self):
            return Pizza(self)


if __name__ == '__main__':
    pizza = Pizza.PizzaBuilder().add_queued().add_preparation().add_prepare_dough()._add_sauce()._add_topping().add_bake().add_ready().build()
    print(pizza)