#coding=utf-8


class Computer:
    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None
        self.hdd = None
        self.gpu = None

    def __str__(self):
        info = ('SerialNumber: {}'.format(self.serial),
                'Memory: {}GB'.format(self.memory),
                'Hard Disk: {}GB'.format(self.hdd),
                'Graphics Card: {}'.format(self.gpu))
        return '\n'.join(info)


class TabletComputer:
    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None
        self.hdd = None

    def __str__(self):
        info = ('SerialNumber: {}'.format(self.serial),
                'Memory: {}GB'.format(self.memory),
                'Hard Disk: {}GB'.format(self.hdd))
        return '\n'.join(info)


class ComputerBuilder:
    def __init__(self, serial_number):
        self.computer = Computer(serial_number)

    def configure_memory(self, amount):
        self.computer.memory = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model


class TabletComputerBuilder:
    def __init__(self, serial_number):
        self.tablet_computer = TabletComputer(serial_number)

    def configure_memory(self, amount):
        self.tablet_computer.memory = amount

    def configure_hdd(self, amount):
        self.tablet_computer.hdd = amount


class HardwareEngineer:
    def __init__(self):
        self.builder = None
        self.tablet_builder = None

    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder('AB345126')
        self.builder.configure_memory(memory)
        self.builder.configure_hdd(hdd)
        self.builder.configure_gpu(gpu)

    def construct_tablet(self, memory, hdd):
        self.tablet_builder = TabletComputerBuilder('GH123453')
        self.tablet_builder.configure_memory(memory)
        self.tablet_builder.configure_hdd(hdd)

    @property
    def computer(self):
        return self.builder.computer

    @property
    def tablet_computer(self):
        return self.tablet_builder.tablet_computer


def main():
    print('create computer')
    engineer = HardwareEngineer()
    engineer.construct_computer(hdd=500, memory=8, gpu='GeForce GTX 650 Ti')
    computer = engineer.computer
    print(computer)
    print('create tablet_computer')
    engineer.construct_tablet(memory=16, hdd=256)
    tablet_computer = engineer.tablet_computer
    print(tablet_computer)


if __name__ == '__main__':
    main()