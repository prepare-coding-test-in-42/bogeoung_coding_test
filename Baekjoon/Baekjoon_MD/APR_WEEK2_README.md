## [사다리 조작](https://www.acmicpc.net/problem/15684)

#### 소요시간
- 

#### 간단 풀이 방식
- 

#### Pseudo Code
```

```

#### 시간복잡도
- 

#### 소요시간 및 메모리
- 메모리 :  KB
- 소요시간 : ms

## [드래곤 커브](https://www.acmicpc.net/problem/15685)

#### 소요시간
- 

#### 간단 풀이 방식
- 

#### Pseudo Code
```

```

#### 시간복잡도
- 

#### 소요시간 및 메모리
- 메모리 :  KB
- 소요시간 : ms

## [카드 놓기](https://www.acmicpc.net/problem/5568)

#### 소요시간
- 10분 내

#### 간단 풀이 방식
- itertools의 permutations(순열)과 set을 활용하여 중복되지 않는 숫자의 수를 구하였다.

#### Pseudo Code
```
def make_added_numbers(numbers, k):
    perms = permutations(numbers, k)

    addedNumbers = set()

    for perm in perms:
        addedNumbers.add(int(''.join(perm)))

    return len(addedNumbers)

```

#### 시간복잡도
- `permutations` : $O(\frac{(n−k)!}{n!})$
- `for 루프` : $O(N)$
- 종합 : $O(N \cdot \frac{(n-k)!}{n!})$

#### 소요시간 및 메모리 
- 메모리 : 32924 KB
- 소요시간 : 36 ms

## [도영이가 만든 맛있는 음식 ](https://www.acmicpc.net/problem/2961)

#### 소요시간
- 10분 내

#### 간단 풀이 방식
- itertools의 combinations(조합)을 활용하여 구하였다.
- 재료는 한 개 이상 무조건 활용되고, 신 맛은 곱해지기 때문에 초기값을 1로 두었다.

#### Pseudo Code
```
def run(ingredients):
    n = len(ingredients)
    min_diff = 1000000000

    for num_ingredients in range(n, 0, -1):
        combs = combinations(ingredients, num_ingredients)

        for comb in combs:
            added_sour = 1
            added_bitter = 0
            for sour, bitter in comb:
                added_sour *= sour
                added_bitter += bitter
            min_diff = min(min_diff, abs(added_sour - added_bitter))

    return min_diff
```

#### 시간복잡도
- 전체 조합의 수 : $\sum_{k=1}^{n} \binom{n}{k} = 2^n - 1$
- `run` : $O(n \cdot 2^n)$

#### 소요시간 및 메모리
- 메모리 : 32412 KB
- 소요시간 : 32 ms
