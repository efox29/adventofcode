file1 = open('input.txt','r')

hor_direction = 0
ver_direction = 0

for line in file1:
    token = line.split(" ")
    val = int(token[1])
    if token[0] == "forward":
        hor_direction +=val
    elif token[0] == 'down':
        ver_direction += val
    elif token[0] == 'up':
        ver_direction -= val
    
print(f'  h = {hor_direction}\nx v = {ver_direction}\n{hor_direction*ver_direction}')
file1.close()