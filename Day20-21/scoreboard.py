from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Comic Sans', 18, 'bold')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.get_high_score()
        self.update_scoreboard()

    def get_high_score(self):
        with open(".\Day20-21\high_score.txt", "r") as f:
            self.high_score = int(f.read())

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    def reset(self):
        if self.score > self.high_score:
            with open(".\Day20-21\high_score.txt", "w") as f:
                f.write(str(self.score))
        self.score = 0
        self.get_high_score()
        self.update_scoreboard()