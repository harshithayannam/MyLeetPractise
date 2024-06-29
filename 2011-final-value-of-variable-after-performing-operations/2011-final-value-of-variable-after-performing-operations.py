class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for i in range(len(operations)):
            if operations[i] == '--X' or operations[i] == 'X--':
                X = X - 1
            elif operations[i] == '++X' or operations[i] == 'X++':
                X = X + 1
            
        return X