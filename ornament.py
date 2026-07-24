import turtle
from PIL import Image

# ---------- настройки ----------
#SIZE = 40        # размер одного элемента орнамента
#REPEATS = 10     # сколько повторов по горизонтали
#WIDTH = 800
#HEIGHT = 500
#
#BLUE = "#1976d2"
#GREEN = "#009900"
#WHITE = "white"
BLACK = #000000


# ---------- turtle setup ----------
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor(BLACK)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.color(WHITE)
t.fillcolor(WHITE)
t.pensize(2)


# ---------- зелёная нижняя полоса ----------


# ---------- функция элемента орнамента ----------
def ornament_unit(x, y, s):
    t.penup()
    t.goto(x, y)
    t.setheading(0)

    t.begin_fill()

    # центральный "крест"
    for _ in range(4):
        t.forward(s)
        t.left(90)
        t.forward(s / 3)
        t.right(90)
        t.forward(s / 3)
        t.right(90)
        t.forward(s / 3)
        t.left(90)

    t.end_fill()


# ---------- рисуем орнамент ----------
start_x = -WIDTH // 2 + SIZE
y = -HEIGHT//2 + HEIGHT*0.25

for i in range(REPEATS):
    ornament_unit(start_x + i * SIZE * 1.8, y, SIZE)


# ---------- экспорт в BMP ----------
canvas = screen.getcanvas()
canvas.postscript(file="ornament.ps")

img = Image.open("ornament.ps")
img.save("ornament.bmp", "bmp")

print("Готово: ornament.bmp")

turtle.done()

