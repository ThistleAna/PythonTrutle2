from turtle import*
color = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
for x in range(360):
    pencolor(color[x % 6])
    width(x / 100 + 1)
    forward(x)
    left(59)
done()
