class StackSimulator:
    def __init__(self):
        self.stack = []
        self.registers = {'r1': 0, 'r2': 0, 'r3': 0, 'r4': 0, 'r5': 0}
        self.stack_pointer = 100000

    def push(self, register):
        value = self.registers[register]
        self.stack.append(value)
        self.stack_pointer -= 4

    def pop(self, register):
        if self.stack:
            value = self.stack.pop()
            self.registers[register] = value
            self.stack_pointer += 4

    def mv(self, dest_register, source_register):
        # Check if the source register is a number and convert it to a register name
        if source_register.isdigit():
            source_register = 'r' + source_register
        self.registers[dest_register] = self.registers[source_register]

    def add(self, dest_register, source_register):
        self.registers[dest_register] += self.registers[source_register]

    def sub(self, dest_register, source_register):
        self.registers[dest_register] -= self.registers[source_register]

    def mul(self, dest_register, source_register):
        self.registers[dest_register] *= self.registers[source_register]

    def xor(self, dest_register, source_register):
        self.registers[dest_register] ^= self.registers[source_register]

    def nop(self):
        pass

    def jump(self, target_line):
        return target_line - 1

    def prt(self):
        print(self.registers['r1'])


def main():
    n = int(input())
    simulator = StackSimulator()

    for _ in range(n):
        command = input().split()
        operation = command[0]

        if operation == 'push':
            simulator.push(command[1])
        elif operation == 'pop':
            simulator.pop(command[1])
        elif operation == 'mv':
            simulator.mv(command[1], command[2])
        elif operation == 'add':
            simulator.add(command[1], command[2])
        elif operation == 'sub':
            simulator.sub(command[1], command[2])
        elif operation == 'mul':
            simulator.mul(command[1], command[2])
        elif operation == 'xor':
            simulator.xor(command[1], command[2])
        elif operation == 'nop':
            simulator.nop()
        elif operation == 'jump':
            n = simulator.jump(int(command[1]))
        elif operation == 'prt':
            simulator.prt()


if __name__ == "__main__":
    main()
