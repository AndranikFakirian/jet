ro = 1.2
p = 0.119 * 979
steps=800
length=44
ls=length/steps*10

def finder(location, pxx):
    f = open(location)
    for i in range(0, 109):
        p0 = f.readline()
        if p0 == "":
            break
        pxx.append(0.119 * int(p0))
    vxx = []
    for i in range(0, 109):
        dp=pxx[i]-p
        if (dp<=0):
            v0=0
        else:
            v0 = (dp * 2 / ro) ** 0.5
        vxx.append(v0)
    f.close()
    return vxx

p00=[]
p10=[]
p20=[]
p30=[]
p40=[]
p50=[]
p60=[]
p70=[]
p80=[]
p90=[]
v00 = finder("00 mm.txt", p00)
v10 = finder("10 mm.txt", p10)
v20 = finder("20 mm.txt", p20)
v30 = finder("30 mm.txt", p30)
v40 = finder("40 mm.txt", p40)
v50 = finder("50 mm.txt", p50)
v60 = finder("60 mm.txt", p60)
v70 = finder("70 mm.txt", p70)
v80 = finder("80 mm.txt", p80)
v90 = finder("90 mm.txt", p90)

def findmax(a):
    max = a[0]
    maxi = 0
    for i in range(0,len(a)):
        if a[i] > max:
            max = a[i]
            maxi = i
    return maxi           # - индекс максимального элемента массива

def centering(a):         # - сдвиг графика путем добавления нулей или удаления элементов в начале или конце
    shift = -findmax(a)
    r=[]
    for i in range(shift, 109+shift):
        r.append(i)
    return r

import numpy as np
r00=np.array(centering(v00))*ls
r10=np.array(centering(v10))*ls
r20=np.array(centering(v20))*ls
r30=np.array(centering(v30))*ls
r40=np.array(centering(v40))*ls
r50=np.array(centering(v50))*ls
r60=np.array(centering(v60))*ls
r70=np.array(centering(v70))*ls
r80=np.array(centering(v80))*ls
r90=np.array(centering(v90))*ls

def q(a, r):
    qxx = 0
    for i in range(0, 108):
        qxx += 3.14159 * ro * (abs(r[i] * a[i] + r[i + 1] * a[i + 1]))*ls*10**(-3)
    return qxx

qall = [q(v00, r00), q(v10, r10), q(v20, r20), q(v30, r30), q(v40, r40), q(v50, r50), q(v60, r60), q(v70, r70), q(v80, r80), q(v90, r90)]

from matplotlib import pyplot as plt
import matplotlib.ticker as tic
from scipy.interpolate import make_interp_spline as mis

fig, ax = plt.subplots()
ax.plot(r00, p00, marker=".", label = "r = 00 мм")
ax.plot(r10, p10, marker=".", label = "r = 10 мм")
ax.plot(r20, p20, marker=".", label = "r = 20 мм")
ax.plot(r30, p30, marker=".", label = "r = 30 мм")
ax.plot(r40, p40, marker=".", label = "r = 40 мм")
ax.plot(r50, p50, marker=".", label = "r = 50 мм")
ax.plot(r60, p60, marker=".", label = "r = 60 мм")
ax.plot(r70, p70, marker=".", label = "r = 70 мм")
ax.plot(r80, p80, marker=".", label = "r = 80 мм")
ax.plot(r90, p90, marker=".", label = "r = 90 мм")
ax.set_xlim([-40, 40])
ax.set_ylim([100, 500])
ax.yaxis.set_minor_locator(tic.MultipleLocator(10)) #делаем сетку
ax.xaxis.set_minor_locator(tic.MultipleLocator(1))
ax.yaxis.set_major_locator(tic.MultipleLocator(50))
ax.xaxis.set_major_locator(tic.MultipleLocator(5))
ax.grid(axis= 'both', which = 'minor', linestyle='--', linewidth=0.5, alpha=0.4, color='lightgrey', zorder=0)
ax.grid(axis= 'both', which = 'major', linestyle='-', linewidth=1, alpha=0.4, color='lightgrey', zorder=0)
ax.set_title("График зависимости давления торможения от расстояния до трубки Пито")
ax.set_ylabel('Давление торможения, Па')
ax.set_xlabel('Расстояние, мм')
ax.legend(loc=0)
plt.show()
fig.savefig('pressure.png')

del fig
del ax

fig, ax = plt.subplots()
X_Y_Spline = mis(r00, p00)
X_ = np.linspace(r00.min(), r00.max(), 500)
Y_ = X_Y_Spline(X_)
ax.plot(X_, Y_, marker=".", markersize=4, label = "r = 00 мм")
X_Y_Spline = mis(r10, p10)
X_ = np.linspace(r10.min(), r10.max(), 500)
Y_ = X_Y_Spline(X_)
ax.plot(X_, Y_, marker=".", markersize=4, label = "r = 10 мм")
X_Y_Spline = mis(r20, p20)
X_ = np.linspace(r20.min(), r20.max(), 500)
Y_ = X_Y_Spline(X_)
ax.plot(X_, Y_, marker=".", markersize=4, label = "r = 20 мм")
X_Y_Spline = mis(r30, p30)
X_ = np.linspace(r30.min(), r30.max(), 500)
Y_ = X_Y_Spline(X_)
ax.plot(X_, Y_, marker=".", markersize=4, label = "r = 30 мм")
X_Y_Spline = mis(r40, p40)
X_ = np.linspace(r40.min(), r40.max(), 500)
Y_ = X_Y_Spline(X_)
ax.plot(X_, Y_, marker=".", markersize=4, label = "r = 40 мм")
X_Y_Spline = mis(r50, p50)
X_ = np.linspace(r50.min(), r50.max(), 500)
Y_ = X_Y_Spline(X_)
ax.plot(X_, Y_, marker=".", markersize=4, label = "r = 50 мм")
X_Y_Spline = mis(r60, p60)
X_ = np.linspace(r60.min(), r60.max(), 500)
Y_ = X_Y_Spline(X_)
ax.plot(X_, Y_, marker=".", markersize=4, label = "r = 60 мм")
X_Y_Spline = mis(r70, p70)
X_ = np.linspace(r70.min(), r70.max(), 500)
Y_ = X_Y_Spline(X_)
ax.plot(X_, Y_, marker=".", markersize=4, label = "r = 70 мм")
X_Y_Spline = mis(r80, p80)
X_ = np.linspace(r80.min(), r80.max(), 500)
Y_ = X_Y_Spline(X_)
ax.plot(X_, Y_, marker=".", markersize=4, label = "r = 80 мм")
X_Y_Spline = mis(r90, p90)
X_ = np.linspace(r90.min(), r90.max(), 500)
Y_ = X_Y_Spline(X_)
ax.plot(X_, Y_, marker=".", markersize=4, label = "r = 90 мм")
ax.set_xlim([-40, 40])
ax.set_ylim([100, 500])
ax.yaxis.set_minor_locator(tic.MultipleLocator(10)) #делаем сетку
ax.xaxis.set_minor_locator(tic.MultipleLocator(1))
ax.yaxis.set_major_locator(tic.MultipleLocator(50))
ax.xaxis.set_major_locator(tic.MultipleLocator(5))
ax.grid(axis= 'both', which = 'minor', linestyle='--', linewidth=0.5, alpha=0.4, color='lightgrey', zorder=0)
ax.grid(axis= 'both', which = 'major', linestyle='-', linewidth=1, alpha=0.4, color='lightgrey', zorder=0)
ax.set_title("График зависимости давления торможения от расстояния до трубки Пито")
ax.set_ylabel('Давление торможения, Па')
ax.set_xlabel('Расстояние, мм')
ax.legend(loc=0)
plt.show()
fig.savefig('pressure_smoothed.png')

del fig
del ax

fig, ax = plt.subplots()
ax.plot(r00, v00, marker=".", label = "Q (00 мм) = {:.3f} г/с".format(qall[0]))
ax.plot(r10, v10, marker=".", label = "Q (10 мм) = {:.3f} г/с".format(qall[1]))
ax.plot(r20, v20, marker=".", label = "Q (20 мм) = {:.3f} г/с".format(qall[2]))
ax.plot(r30, v30, marker=".", label = "Q (30 мм) = {:.3f} г/с".format(qall[3]))
ax.plot(r40, v40, marker=".", label = "Q (40 мм) = {:.3f} г/с".format(qall[4]))
ax.plot(r50, v50, marker=".", label = "Q (50 мм) = {:.3f} г/с".format(qall[5]))
ax.plot(r60, v60, marker=".", label = "Q (60 мм) = {:.3f} г/с".format(qall[6]))
ax.plot(r70, v70, marker=".", label = "Q (70 мм) = {:.3f} г/с".format(qall[7]))
ax.plot(r80, v80, marker=".", label = "Q (80 мм) = {:.3f} г/с".format(qall[8]))
ax.plot(r90, v90, marker=".", label = "Q (90 мм) = {:.3f} г/с".format(qall[9]))
ax.set_xlim([-40, 40])
ax.set_ylim([-0.5, 25])
ax.yaxis.set_minor_locator(tic.MultipleLocator(0.2)) #делаем сетку
ax.xaxis.set_minor_locator(tic.MultipleLocator(1))
ax.yaxis.set_major_locator(tic.MultipleLocator(1))
ax.xaxis.set_major_locator(tic.MultipleLocator(5))
ax.grid(axis= 'both', which = 'minor', linestyle='--', linewidth=0.5, alpha=0.4, color='lightgrey', zorder=0)
ax.grid(axis= 'both', which = 'major', linestyle='-', linewidth=1, alpha=0.4, color='lightgrey', zorder=0)
ax.set_title("График зависимости скорости потока от расстояния до трубки Пито")
ax.set_ylabel('Скорость, м/с')
ax.set_xlabel('Расстояние, мм')
ax.legend(loc=0)
plt.show()
fig.savefig('velocity.png')

del fig
del ax

fig, ax = plt.subplots()
X_Y_Spline = mis(r00, v00)
X_ = np.linspace(r00.min(), r00.max(), 500)
Y_ = X_Y_Spline(X_)
ax.plot(X_, Y_, marker=".", markersize=4, label = "Q (00 мм) = {:.3f} г/с".format(qall[0]))
X_Y_Spline = mis(r10, v10)
X_ = np.linspace(r10.min(), r10.max(), 500)
Y_ = X_Y_Spline(X_)
ax.plot(X_, Y_, marker=".", markersize=4, label = "Q (10 мм) = {:.3f} г/с".format(qall[1]))
X_Y_Spline = mis(r20, v20)
X_ = np.linspace(r20.min(), r20.max(), 500)
Y_ = X_Y_Spline(X_)
ax.plot(X_, Y_, marker=".", markersize=4, label = "Q (20 мм) = {:.3f} г/с".format(qall[2]))
X_Y_Spline = mis(r30, v30)
X_ = np.linspace(r30.min(), r30.max(), 500)
Y_ = X_Y_Spline(X_)
ax.plot(X_, Y_, marker=".", markersize=4, label = "Q (30 мм) = {:.3f} г/с".format(qall[3]))
X_Y_Spline = mis(r40, v40)
X_ = np.linspace(r40.min(), r40.max(), 500)
Y_ = X_Y_Spline(X_)
ax.plot(X_, Y_, marker=".", markersize=4, label = "Q (40 мм) = {:.3f} г/с".format(qall[4]))
X_Y_Spline = mis(r50, v50)
X_ = np.linspace(r50.min(), r50.max(), 500)
Y_ = X_Y_Spline(X_)
ax.plot(X_, Y_, marker=".", markersize=4, label = "Q (50 мм) = {:.3f} г/с".format(qall[5]))
X_Y_Spline = mis(r60, v60)
X_ = np.linspace(r60.min(), r60.max(), 500)
Y_ = X_Y_Spline(X_)
ax.plot(X_, Y_, marker=".", markersize=4, label = "Q (60 мм) = {:.3f} г/с".format(qall[6]))
X_Y_Spline = mis(r70, v70)
X_ = np.linspace(r70.min(), r70.max(), 500)
Y_ = X_Y_Spline(X_)
ax.plot(X_, Y_, marker=".", markersize=4, label = "Q (70 мм) = {:.3f} г/с".format(qall[7]))
X_Y_Spline = mis(r80, v80)
X_ = np.linspace(r80.min(), r80.max(), 500)
Y_ = X_Y_Spline(X_)
ax.plot(X_, Y_, marker=".", markersize=4, label = "Q (80 мм) = {:.3f} г/с".format(qall[8]))
X_Y_Spline = mis(r90, v90)
X_ = np.linspace(r90.min(), r90.max(), 500)
Y_ = X_Y_Spline(X_)
ax.plot(X_, Y_, marker=".", markersize=4, label = "Q (90 мм) = {:.3f} г/с".format(qall[9]))
ax.set_xlim([-40, 40])
ax.set_ylim([-0.5, 25])
ax.yaxis.set_minor_locator(tic.MultipleLocator(0.2)) #делаем сетку
ax.xaxis.set_minor_locator(tic.MultipleLocator(1))
ax.yaxis.set_major_locator(tic.MultipleLocator(1))
ax.xaxis.set_major_locator(tic.MultipleLocator(5))
ax.grid(axis= 'both', which = 'minor', linestyle='--', linewidth=0.5, alpha=0.4, color='lightgrey', zorder=0)
ax.grid(axis= 'both', which = 'major', linestyle='-', linewidth=1, alpha=0.4, color='lightgrey', zorder=0)
ax.set_title("График зависимости скорости потока от расстояния до трубки Пито")
ax.set_ylabel('Скорость, м/с')
ax.set_xlabel('Расстояние, мм')
ax.legend(loc=0)
plt.show()
fig.savefig('velocity_smoothed.png')

del fig
del ax

fig, ax = plt.subplots()
ax.plot([i * 10 for i in range(10)], qall, marker=".", label="Расход от расстояния")
ax.set_title("График зависимости расхода от расстояния до трубки Пито")
ax.set_ylabel('Расход')
ax.set_xlabel('Расстояние, мм')
ax.legend(loc=0)
ax.set_xlim([-2, 92])
ax.set_ylim([62, 70])
ax.yaxis.set_minor_locator(tic.MultipleLocator(0.1)) #делаем сетку
ax.yaxis.set_major_locator(tic.MultipleLocator(1))
ax.xaxis.set_major_locator(tic.MultipleLocator(10))
ax.grid(axis= 'y', which = 'minor', linestyle='--', linewidth=0.5, alpha=0.4, color='lightgrey', zorder=0)
ax.grid(axis= 'both', which = 'major', linestyle='-', linewidth=1, alpha=0.4, color='lightgrey', zorder=0)
plt.show() # - раскомментить, чтобы получить график
fig.savefig('q_plot.png')