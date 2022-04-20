def jointAttack(array):
    if (len(array)<=1):
        return array.pop()

    return array.pop(0) + 1 / (jointAttack(array))

N = int(input())
array = [int(_) for _ in input().split()]

print(jointAttack(array))