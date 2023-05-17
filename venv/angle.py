from turtle import*

for angle in range(0, 360, 30):
    setheading(angle)
    forward(150)
    write(str(angle) + '°')
    backward(150)
done()
