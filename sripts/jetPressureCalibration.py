from matplotlib import pyplot as plt

x = [0, 800]
y = [0, 4.4]

plt.plot(x, y, marker = ".", label = "P = 0.119N - 116.749")

plt.minorticks_on()
plt.grid(b = True, which = "minor")
plt.grid(b = True)
plt.title("Калибровочный график зависимости показаний АЦП от давления")
plt.ylabel('Отсчёты АЦП')
plt.xlabel('Давление, Па')
plt.legend()
plt.show()

