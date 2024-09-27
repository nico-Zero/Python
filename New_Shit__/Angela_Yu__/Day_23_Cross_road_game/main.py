from display import Display
from players import Player
from car import Cars

monitor = Display()

player_1 = Player()
vehicle = Cars()


while 1:
    player_1.control(monitor)
    monitor.speed()
    vehicle.create_car()
    vehicle.move()

    if vehicle.check_collision(player_1):
        break

    if player_1.is_level_up():
        monitor.level_up()
        vehicle.increase_density()
        vehicle.speed_up(2)
        player_1.reset()

    monitor.screen.update()

monitor.game_over()

monitor.screen.exitonclick()
