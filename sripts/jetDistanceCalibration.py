from matplotlib import pyplot as plt

x = [0, 800]
y = [0, 4.4]

plt.plot(x, y, marker = ".", label = "X = 0.0055 cm/step")

plt.minorticks_on()
plt.grid(b = True, which = "minor")
plt.grid(b = True)
plt.title("Калибровочный график зависимости перемещения трубки Пито от шага двигателя")
plt.ylabel('Перемещение трубки Пито, см')
plt.xlabel('Количество шагов')
plt.legend()
plt.show()

