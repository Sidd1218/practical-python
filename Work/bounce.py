# bounce.py
#
# Exercise 1.5

height = 100
bounces = 11
for bounce in range(0,bounces):
    new_height = height * 0.6
    height = new_height
    print(round(new_height,4))
