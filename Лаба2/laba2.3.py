# Реализовать иерархию классов, описывающих разные виды объектов одного типа (например, сервоприводов (синхронный/асинхронный/линейный и т.п.). Реализовать минимум 3 уровня иерархии. Реализовать возможность задания характеристик (например, для двигателя это угол поворота, скорость вращения, ускорение и т.п.)
# Базовый класс для всех видов сервоприводов
class ServoDrive:
    def __init__(self):
        self.rotation_angle = 0  # угол поворота
        self.rotation_speed = 0  # скорость вращения

    def set_rotation_angle(self, angle):
        self.rotation_angle = angle

    def set_rotation_speed(self, speed):
        self.rotation_speed = speed


# Класс для синхронного сервопривода
class SynchronousServoDrive(ServoDrive):
    def __init__(self):
        super().__init__()
        self.acceleration = 0  # ускорение

    def set_acceleration(self, acceleration):
        self.acceleration = acceleration


# Класс для асинхронного сервопривода
class AsynchronousServoDrive(ServoDrive):
    def __init__(self):
        super().__init__()
        self.deceleration = 0  # замедление

    def set_deceleration(self, deceleration):
        self.deceleration = deceleration


# Класс для линейного сервопривода
class LinearServoDrive(ServoDrive):
    def __init__(self):
        super().__init__()
        self.position = 0  # позиция

    def set_position(self, position):
        self.position = position