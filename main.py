from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)
screen.listen()
player = Player()
car = CarManager()
score = ScoreBoard()
screen.onkey(key="Up", fun=player.move_up)
screen.onkey(key="Down", fun=player.move_down)
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    #Detect collision with car
    """
    When the car collides with the turtle then the game should end
    """
    for each_car in car.all_cars:
        if each_car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    #Detect successful crossing
    """
    The rule of the game is whenever the turtle crosses the path without collision then it will go back to the starting
    position and the speed of the car increases.
    """
    if player.is_at_finish_line():
        player.goto_start()
        car.level_up()
        score.level_points()

screen.exitonclick()
