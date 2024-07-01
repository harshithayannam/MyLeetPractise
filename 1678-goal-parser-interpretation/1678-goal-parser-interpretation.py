class Solution:
    def interpret(self, command: str) -> str:
        goal = ""
        for i in range(len(command)):
            if command[i] == '(' and command[i+1] == ')':
                goal = goal + 'o'
            elif command[i] == ')' and command[i-1] == '(':
                continue
            elif (command[i] == '(' and command[i+1] != ')') or (command[i] == ')' and command[i-1] != '('):
                continue
            else:
                goal = goal + command[i]
        
        return goal
                