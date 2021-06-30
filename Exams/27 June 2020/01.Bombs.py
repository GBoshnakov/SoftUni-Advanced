from collections import deque


bomb_effect = deque([int(el) for el in input().split(", ")])
bomb_casing = [int(el) for el in input().split(", ")]
is_fulfill = False

bombs = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0
}

checker = {
    40: "Datura Bombs",
    60: "Cherry Bombs",
    120: "Smoke Decoy Bombs"
}

while bomb_effect and bomb_casing:
    sum_of_bombs = bomb_effect[0] + bomb_casing[-1]
    if sum_of_bombs in checker:
        bombs[checker[sum_of_bombs]] += 1
        bomb_effect.popleft()
        bomb_casing.pop()
    else:
        bomb_casing[-1] -= 5

    if bombs["Datura Bombs"] >= 3 and bombs["Cherry Bombs"] >= 3 and bombs["Smoke Decoy Bombs"] >= 3:
        is_fulfill = True
        break

if is_fulfill:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effect:
    print(f"Bomb Effects: {', '.join(str(el) for el in bomb_effect)}")
else:
    print("Bomb Effects: empty")
if bomb_casing:
    print(f"Bomb Casings: {', '.join(str(el) for el in bomb_casing)}")
else:
    print("Bomb Casings: empty")

for key, val in sorted(bombs.items()):
    print(f"{key}: {val}")
