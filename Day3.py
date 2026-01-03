import math
age = 18
height = 179.1
imagionary = 1-3j
base = float(input('Enter base of triangle: '))
triangle_height = float(input('Enter height of triangle: '))
print(f'The area of triangle is {0.5 * base * triangle_height}')
side_a = float(input('Enter side a of triangle: '))
side_b = float(input('Enter side b of triangle: '))
side_c = float(input('Enter side c of triangle: '))
print(f'Perimeter of triangle is {side_a + side_b + side_c}')
rect_width = float(input('Enter width of rectangle: '))
rect_height = float(input('Enter height of rectangle: '))
print(f'Area of rectangle is {rect_width * rect_height}')
print(f'Perimeter of rectangle is {2*(rect_width + rect_height)}')
circle_radius = float(input('Enter radius of circle: '))
print(f'Area of circle is {round(math.pi * (circle_radius ** 2))}')
print(f'Circumference of circle is {round(2*math.pi*circle_radius)}')
x = 0
y = 0
Slope_one = 2
print(f'Y-intersect of(y=2x-2): {round(2*x-2)}')
print(f'X-intersect of(y=2x-2): {round((y+2)/2)}')
print(f'Slope = {Slope_one}')
x_one = 2
x_two = 6
y_one = 2
y_two = 10
Slope_two = (y_two - y_one) / (x_two - x_one)
print(f'The slope of (2, 2) and (6, 10) is {round(Slope_two)}')
Euclidian_distance = math.sqrt((x_two - x_one)**2 + (y_two - y_one)**2)
print(f'Euclidian_distance = {round(Euclidian_distance)}')
print(f'Slope one is bigger: {Slope_one > Slope_two}')
print(f'Slope two is bigger: {Slope_one < Slope_two}')
print(f'Slopes are equal: {Slope_one == Slope_two}')
x = -3
y = x**2 + 6*x + 9
print(f'Y is equal to {y}, when x = {x}')
print(f'Length of \'python\' is { len('python') }')
print(f'Length of \'dragon\' is { len('dragon') }')
print(f'python is longer than dragon {len('python')==len('dragon')}')
print(f'python is shorter than dragon {len('python')==len('dragon')}')
print(f'python is equal to dragon {len('python')!=len('dragon')}')
print(f'\'on\' is in \'python\' and \'dragon\': {"on" in "python" and "on" in "dragon"}')
print (f'I hope this course is not full of jargon: {'jargon' in 'I hope this course is not full of jargon'} ')
print(str(float(len('python'))))
print(5 % 2)
print(7 // 3 == int(2.7))
print(type('10') == type(10))
print(int(float('9.8')) == 10)
hours = input('Enter hours: ')
rate = input('Enter rate: ')
print(f'Your weekly salary is {round(float(hours) * float(rate))}')
years_lived = int(input('Enter number of years you have lived: '))
print(f'You lived for {round(31536000 * years_lived)} secs')
print(f'1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125')