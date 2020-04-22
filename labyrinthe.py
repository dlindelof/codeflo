import matplotlib.pyplot as plt

plt.figure(figsize=(15, 15))

N_COLS = 10
N_ROWS = 10

for cell in list(range(N_COLS * N_ROWS)):
    x = cell % N_COLS
    y = cell // N_COLS
    plt.plot([x, x + 1], [y, y], 'k')          # ligne du bas
    plt.plot([x + 1, x + 1], [y, y + 1], 'k')  # ligne de droite
    plt.plot([x + 1, x], [y + 1, y + 1], 'k')  # ligne du haut
    plt.plot([x, x], [y + 1, y], 'k')          # ligne de gauche
    
