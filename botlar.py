# chizmalardan iborat kodlar jamlanmasi

from turtle import *

color('red', 'yellow')
begin_fill()

while True:
    forward(200)
    left(150)
    if abs(pos()) < 1:
        break

end_fill()
done()


print("hello world")