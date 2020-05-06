import random

import matplotlib.pyplot as plt

N_COLS = 100
N_ROWS = 100
N_CELLS = N_ROWS * N_COLS

PASSAGES = [[-1, 0], [N_CELLS - 1, N_CELLS]]

STACK = [random.choice(range(N_CELLS))]
VISITED = []


plt.figure(figsize=(N_COLS, N_ROWS))
plt.axis('off')


def all_neighbors(cell, N_COLS):
    neighbors = []
    if cell - N_COLS >= 0:
        neighbors.append(cell - N_COLS)  # voisin du sud
    if cell + N_COLS < N_CELLS:
        neighbors.append(cell + N_COLS)  # voisin du nord
    if cell % N_COLS != 0:
        neighbors.append(cell - 1)  # voisin de l'ouest
    if (cell + 1) % N_COLS != 0:
        neighbors.append(cell + 1)  # voisin de l'est
    return neighbors


while STACK:
    cell = STACK[-1]
    VISITED.append(cell)
    neighbors = all_neighbors(cell, N_COLS)
    visitable = [cell for cell in neighbors if cell not in VISITED]
    if visitable:
        cell2 = random.choice(visitable)
        PASSAGES.append(sorted([cell, cell2]))
        STACK.append(cell2)
    else:
        STACK.pop()



for cell in list(range(N_CELLS)):
    x = cell % N_COLS
    y = cell // N_COLS
    
    if [cell - N_COLS, cell] not in PASSAGES:
        plt.plot([x, x + 1], [y, y], 'k')          # ligne du bas
        
    if [cell, cell + 1] not in PASSAGES:
        plt.plot([x + 1, x + 1], [y, y + 1], 'k')  # ligne de droite
    
    if [cell, cell + N_COLS] not in PASSAGES:
        plt.plot([x + 1, x], [y + 1, y + 1], 'k')  # ligne du haut
        
    if [cell - 1, cell] not in PASSAGES:
        plt.plot([x, x], [y + 1, y], 'k')          # ligne de gauche
        
    # plt.text(x + 0.5, y + 0.5, cell)
