import os
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#deklaracja liczby Prandtla(o), liczby Rayleigha(r), stałej charakteryzującej rozmiary obszaru, w którym odbywa się przepływ konwekcyjny(b).
o = 10
r = 28
b =8./3.

#deklaracja nazwy folderu do której ma być zapisywany obraz
file = 'obrazlorenz'
if not os.path.exists(file):
    os.makedirs(file)

#początek symulacji
start_time = 1
#koniec symulacji, obraz najlepiej widoczny dla wartości ~60
end_time = 60
#odstęp czasowy
interval = 100
#czas symulacji w postaci tablicy numpy, ostatni parametr określa liczbę "kroków" symulacji
time_points = np.linspace(start_time, end_time, end_time * interval)
#zapis czasu symulacji jako faktycznej tablicy(potrzebne aby zastosować funkcję różniczkującą odeint(). inaczej napotkamy ValueError
time_pointss = [time_points[0:i] for i in range(1, len(time_points) + 1)]
#początek układu współrzędnych
startxyz = [0.1,0,0]

#funkcja zwracająca postać równań układu Lorenza jako tablica; wykorzystywana do funkcji różniczkującej odeint(). x,y,z - zmienne
def lorenz_system(variable, t):
    x, y, z = variable
    dx_dt = o * (y - x)
    dy_dt = x * (r - z) - y
    dz_dt = x * y - b * z
    return [dx_dt, dy_dt, dz_dt]


#funkcja rysująca układ Lorenza; wykres ma być zapisany wtedy, kiedy długość tablicy z policzonymi punktami będzie równy ostatniemu "indeksowi" z funkcji enumerate. Zapobiega to zapisowi zbyt dużej ilości plików przeciążającej pamięć
def plot_lorenz_system(constant):
    plt.figure()
    ax = plt.axes(projection ='3d')
    ax.plot(constant[:,0], constant[:,1], constant[:,2], color='green', alpha=0.7, linewidth=0.9)
    ax.set_title('Lorenz system')
    plt.title('Lorenz system')
    plt.show()

# tablica składająca się z punktów uzyskanych poprzez różniczkowanie równań tworzących układ Lorenza. Pierwszy parametr odeint to równania, drugim jest początek układu, trzeci zaś to odstępy czasowe dla których punkty są liczone rosnące monotonicznie
points = [odeint(lorenz_system, startxyz, timepoint) for timepoint in time_pointss]


# Funkcja Loop zawirająca pętlę z enumerate pozwalająca na rysowanie poszczególnych odcinków obrazu
def Loop():
    lista = [0, 500, 1000, 1500, 2000, 2500, 2810, 3400, 3800, 4400, 4800, 5100, 5600, 5999]
    for n, point in enumerate(points):
        for l in range(len(lista)):
            if (n==lista[l]):
                plot_lorenz_system(point)

# Zapisywanie finalnej wersji wykresu w formacie png
#for k, point in enumerate(points):
#   if k == (len(points) - 1):
#      plt.savefig('{}/{:03d}.png'.format(file, k), dpi=60, bbox_inches='tight', pad_inches=0.1)

Loop()