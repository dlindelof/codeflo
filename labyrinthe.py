import random

import matplotlib.pyplot as plt

N_COLS = 30
N_ROWS = 30

PASSAGES = []

plt.figure(figsize=(N_COLS, N_ROWS))
plt.axis('off')

for cell in list(range(N_COLS * N_ROWS - 1)):
    if (cell + 1) % N_COLS == 0:  # sur le mur de droite
        cell2 = cell + N_COLS
    elif cell + N_COLS >= N_COLS * N_ROWS:  # sur le mur du haut
        cell2 = cell + 1
    else:
        cell2 = random.choice([cell + 1, cell + N_COLS])
    PASSAGES.append([cell, cell2])


for cell in list(range(N_COLS * N_ROWS)):
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
