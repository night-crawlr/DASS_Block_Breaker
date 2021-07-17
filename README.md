# BRICK BREAKER

## Style:
+ Code is writern in python3 using OOPS concepts
+ Main OOPS concepts are
  - ###  Encapsulation
    - Using OOP in Python, we can restrict access to methods and variables. This prevents data from direct modification which is called encapsulation. In Python, we denote private attributes using underscore as the prefix i.e single _ or double __.
    - In Bricks.py
    ```python
    def __init__(this):
        this.__is_broken = 0
        this.__row = 0
        this.__col = 0
        this.__type = 0
        this.__points = 0
        def ret_is_broken(this):
        return this.__is_broken

    def upd_is_broken(this, x):
        this.__is_broken = x

    def ret_row(this):
        return this.__row

    def upd_row(this, x):
        this.__row = x

    def upd_col(this, x):
        this.__col = x

    def ret_col(this):
        return this.__col

    def ret_type(this):
        return this.__type

    def dec_type(this):
        this.__type -= 1

    def upd_type(this, x):
        this.__type = x

    def ret_points(this):
        return this.__points

    def upd_points(this, x):
        this.__points = x
    ```
  - ### Polymorphism
    - Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).
Suppose, we need to color a shape, there are multiple shape options (rectangle, square, circle). However we could use the same method to color any shape. This concept is called Polymorphism.
    - In scree.py,Bricks.py,paddle.py
  - ### Inhereitance
    - Inheritance is a way of creating a new class for using details of an existing class without modifying it. The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).
    - In Bricks.py,Powers.py,screeen.py
___
## Libraries
+ [python3](https://www.python.org/downloads/)
+ [coloroma](https://pypi.org/project/colorama/)
## Execution
+ After installing the above libraries, Execute the main.py file using below command in the directory folder
```
python3 ./main.py
```
___
## Information
Brick Breaker is an Terminal game inspired from [the old brick breaker](https://www.youtube.com/watch?v=BXEk0IHzHOM)
+ ### Elements
  - Ball
  - Paddle
  - Bricks - There are 4 types of bricks
    - Red brick - Need a hit to break :pointup:
    - Blue brick - Need 2 hits to break :v:
    - Yellow brick - Need 3 hits to break :ok_hand:
    - White brick - Unbreakable :muscle:
    - Rainbow brick - Changes color untill it got hit 
  - Power ups - There are 5 types of powerups each stands for some time
    -  EP - Expand paddle
    -  SP - Shrink paddle
    -  FB - Fast ball
    -  TB - Thru-Ball (breaks any brick at a time)
    -  PG - Paddle Grab (Paddle can grab the ball and released on its will)
    -  SP - Shooting Paddle 
  - Score
    - Red brick gives 5 Points
    - Blue brick gives 10 Points
    - Yellow brick gives 15 Points
    - White brick gives 0 Points (even by TB :pensive: )
  - Lives
  - Time
  - Sound
  - BOSS :imp:
    - UFO which follows the paddle
    - Drops bombs on regular time interval
    - UFO health decreases on hit by a ball
    - Spawns 2 layers of defensive bricks around it
+ ### Features
    - MultiLevel Game
    - Elastic Collision with bricks, paddle, and boundaries.
    - Brick streanth decreases by 1 when hit (except the unbreakable ones)
    - Gravity fall simulation for powerups fall.
+ ### Controls
  - 'a' - To move the paddle left
  - 'd' - To move the paddle right
  - 'q' - To quit the game
  - '[SPACE]' - To release the ball from paddle
  - 'p' - To pause/resume the game
  - 'f' - To move the game one-step ahead when PAUSED (Note: when paused, the other controls wont work, except 'f')

+ ### Files
  - background.py - Python file that contains the Background and Boundaries code
  - ball.py - Python file that contains the ball code
  - Bricks.py - Python file that contains bricks, bricks_handler(Bricks) code
  - constants.py - Python file that conatins the Configuration constants like screen size, paddle length etc
  - input.py - Python file that contains the input taking code
  - main.py - Python file that simulates the choosen game and its environment
  - paddle.py Python file that contains about the paddle info and its code
  - power.py - Python file that contains about the powerups, its handler code
  - screen.py - Python file that contains about screen,headers info and its code


    
