# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
selected_nums = []


# 선택된 원소들을 출력해줍니다.
def print_permutation():
    for num in selected_nums:
        print(num, end = " ")
    print()


def find_duplicated_permutations(curr_num, cnt):
    if cnt > m :
        return 
    # n개를 모두 뽑은 경우 답을 출력해줍니다.
    if cnt == m :

        print_permutation()
        return
    
    for i in range(1, n + 1):
        if curr_num > 0 and i <= selected_nums[-1]: 
            continue
        else:
            selected_nums.append(i)
            
            find_duplicated_permutations(curr_num + 1, cnt + 1)
            selected_nums.pop()


find_duplicated_permutations(0, 0)