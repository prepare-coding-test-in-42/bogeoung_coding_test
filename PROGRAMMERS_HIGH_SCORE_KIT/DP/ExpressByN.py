def solution(N, number):
    if number == 1:
        return 1
    
    set_list = []
    
    for cnt in range(1,9):
        part_set = set()
        part_set.add(int(str(N)*cnt)) 
        for i in range(cnt -1):
            for op1 in set_list[i]:
                for op2 in set_list[cnt-i-2]:
                    part_set.add(op1 + op2)
                    part_set.add(op1 - op2)
                    part_set.add(op2 - op1)
                    part_set.add(op1 * op2)
                    if op2 != 0:
                        part_set.add(op1 / op2)
        
        if number in part_set:
            return cnt
        set_list.append(part_set)
        
    return -1