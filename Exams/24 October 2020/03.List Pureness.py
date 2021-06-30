from collections import deque


def best_list_pureness(seq, rotations):
    seq = deque(seq)

    best_rotation = 0
    best_pureness = 0
    for i in range(len(seq)):
        best_pureness += seq[i] * i

    for n in range(1, rotations+1):
        current_pureness = 0
        seq.rotate(1)
        for i in range(len(seq)):
            current_pureness += seq[i] * i

        if current_pureness > best_pureness:
            best_pureness = current_pureness
            best_rotation = n

    return f"Best pureness {best_pureness} after {best_rotation} rotations"

# test = ([4, 3, 2, 6], 4)
# result = best_list_pureness(*test)
# print(result)


# test = ([7, 9, 2, 5, 3, 4], 3)
# result = best_list_pureness(*test)
# print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)




