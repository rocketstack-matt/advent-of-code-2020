class Instruction:

    def __init__(self, instruction) -> None:
        super().__init__()
        self.operation = instruction.strip().split()[0]
        self.argument = int(instruction.strip().split()[1])
        self.executed = 0
    
    def execute(self):
        self.executed+=1
        return self.executed
    
    def __str__(self) -> str:
        return '(' + self.operation + ', ' + str(self.argument) + ')'

class Console:

    def __init__(self, input) -> None:
        super().__init__()
        self.accumulator = 0
        self.program = []
        self.position = 0
        with open(input) as f:
            for line in f:
                self.program.append(Instruction(line))
    
    def acc(self, instruction: Instruction) -> int:
        if instruction.execute() <= 1:
            self.accumulator+=instruction.argument
        return 1

    def nop(self, instruction: Instruction) -> int:
        instruction.execute()
        return 1

    def jmp(self, instruction: Instruction) -> int:
        instruction.execute()
        return instruction.argument

    commands = {
        'acc': acc,
        'nop': nop,
        'jmp': jmp
    }

    def update_instruction(self, instruction_to_swap:int) -> bool:
        if self.program[instruction_to_swap].operation=='acc':
            # print('acc instruction, no action')
            return False
        elif self.program[instruction_to_swap].operation=='jmp':
            self.program[instruction_to_swap].operation='nop'
            # print('flip jpm to nop')
            return True
        else:
            if self.program[instruction_to_swap].argument==0:
                return False

            self.program[instruction_to_swap].operation='jmp'
            # print('flip nop to jmp')
            return True

    def execute(self, instruction_to_swap:int) -> bool:
        if instruction_to_swap>=0:
            if not self.update_instruction(instruction_to_swap):
                return False
        
        self.position = 0
        executing = True
        while executing:
            instruction = self.program[self.position]
            self.position += self.commands.get(instruction.operation)(self, instruction)
            if instruction.executed>1:
                executing = False
                self.update_instruction(instruction_to_swap)
                return False
            if len(self.program)==self.position:
                executing = False
                return True
    
    def reset(self):
        for instruction in self.program:
            instruction.executed = 0
        self.accumulator = 0

    def print(self):
        for instruction in self.program:
            print(instruction)
