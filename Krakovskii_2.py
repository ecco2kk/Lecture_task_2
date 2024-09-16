import numpy as np
import matplotlib.pyplot as plt

# Функция для расчета координат движения тела
def calculate_trajectory(h, v0, angle_deg):
    g = 9.81  # Ускорение свободного падения, м/с^2
    angle_rad = np.radians(angle_deg)  # Переводим угол в радианы

    # Разложение начальной скорости на горизонтальную и вертикальную составляющие
    v0x = v0 * np.cos(angle_rad)
    v0y = v0 * np.sin(angle_rad)

    # Время подъема до максимальной высоты
    t_max = (v0y + np.sqrt(v0y**2 + 2 * g * h)) / g

    # Время падения от максимальной высоты до земли
    t_fall = 2 * v0y / g

    # Общее время полета (учитывая высоту)
    total_time = t_max + t_fall

    # Создаем массив времени от 0 до total_time с шагом 0.01
    t = np.linspace(0, total_time, num=1000)

    # Координаты x(t) и y(t)
    x = v0x * t
    y = h + v0y * t - 0.5 * g * t**2

    return t, x, y

# Функция для расчета скорости тела в каждый момент времени
def calculate_velocity(t, v0, angle_deg):
    g = 9.81  # Ускорение свободного падения, м/с^2
    angle_rad = np.radians(angle_deg)  # Угол в радианах

    # Начальные скорости по осям
    v0x = v0 * np.cos(angle_rad)
    v0y = v0 * np.sin(angle_rad)

    # Горизонтальная составляющая скорости постоянна
    vx = v0x

    # Вертикальная составляющая скорости меняется со временем
    vy = v0y - g * t

    # Полная скорость
    v = np.sqrt(vx**2 + vy**2)

    return v

# Функция для визуализации
def plot_trajectory_and_velocity(h, v0, angle_deg):
    # Рассчитываем траекторию
    t, x, y = calculate_trajectory(h, v0, angle_deg)

    # Рассчитываем скорость в каждый момент времени
    v = calculate_velocity(t, v0, angle_deg)

    # Создаем графики
    fig, axs = plt.subplots(3, 1, figsize=(10, 15))

    # График траектории
    axs[0].plot(x, y, label='Траектория', color='blue')
    axs[0].set_title('Траектория движения тела')
    axs[0].set_xlabel('Координата X (м)')
    axs[0].set_ylabel('Координата Y (м)')
    axs[0].grid(True)
    axs[0].legend()

    # График зависимости X(t)
    axs[1].plot(t, x, label='X(t)', color='green')
    axs[1].set_title('Зависимость X от времени')
    axs[1].set_xlabel('Время (с)')
    axs[1].set_ylabel('Координата X (м)')
    axs[1].grid(True)
    axs[1].legend()

    # График зависимости скорости от времени
    axs[2].plot(t, v, label='Скорость', color='red')
    axs[2].set_title('Зависимость скорости от времени')
    axs[2].set_xlabel('Время (с)')
    axs[2].set_ylabel('Скорость (м/с)')
    axs[2].grid(True)
    axs[2].legend()

    # Показываем графики
    plt.tight_layout()
    plt.show()

# Ввод исходных данных
h = float(input("Введите высоту броска (м): "))
v0 = float(input("Введите начальную скорость (м/с): "))
angle_deg = float(input("Введите угол броска (градусы): "))

# Визуализируем траекторию и графики
plot_trajectory_and_velocity(h, v0, angle_deg)