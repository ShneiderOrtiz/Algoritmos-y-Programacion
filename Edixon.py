import turtle


tortuga=turtle.Turtle()
tortuga.pensize(15)
tortuga.color("red")
tortuga.shape('turtle')
tortuga.left(180)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(60)
tortuga.left(90)
tortuga.forward(80)
tortuga.left(180)
tortuga.forward(80)
tortuga.left(90)
tortuga.forward(60)
tortuga.left(90)
tortuga.forward(100)

tortuga=turtle.Turtle()
tortuga.shape('turtle')
tortuga.pensize(15)
tortuga.color("orange")

# Establecer la velocidad (opcional, para animación)
tortuga.speed(0)  # 0 es la velocidad más rápida

# Dibujar una curva a la derecha
for i in range(180):  # Ajustar el rango para controlar la forma de la curva
    tortuga.forward(1.05)  # Distancia a avanzar (ajustar para la curva)
    tortuga.right(1)  # Ángulo de giro (ajustar para la curva)
tortuga.right(90)
tortuga.forward(105)


tortuga=turtle.Turtle()
tortuga.shape('turtle')
tortuga.pensize(15)
tortuga.color("green")
tortuga.penup()
tortuga.goto((50, 0))
tortuga.pendown()
tortuga.forward(120)
tortuga.right(180)
tortuga.forward(60)
tortuga.left(90)
tortuga.forward(120)
tortuga.right(90)
tortuga.forward(60)
tortuga.left(180)
tortuga.forward(120)

tortuga=turtle.Turtle()
tortuga.shape('turtle')
tortuga.pensize(15)
tortuga.color("blue")
tortuga.penup()
tortuga.goto((175, 0))
tortuga.pendown()
tortuga.right(45)
tortuga.forward(180)

