class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range(len(operations)):
            print(record)
            if operations[i] == '+':
                s1, s2 = int(record[len(record)-2]), int(record[len(record)-1])
                print(s1,s2)
                record.append(s1+s2)
            elif operations[i] == 'C':
                record.pop()
            elif operations[i] == 'D':
                record.append(record[len(record)-1] * 2)
            else:
                record.append(int(operations[i]))
        return sum(record)
