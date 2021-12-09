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
    
print(f'Part1\n  h = {hor_direction}\nx v = {ver_direction}\n{hor_direction*ver_direction}')
file1.close()

##########

file1 = open('input.txt','r')

hor_direction = 0
ver_direction = 0
aim = 0


for line in file1:
    token = line.split(" ")
    val = int(token[1])
    if token[0] == "forward":
        hor_direction +=val
        ver_direction += (val * aim)
       
    elif token[0] == 'down':     
        aim += val
        
    elif token[0] == 'up':       
        aim -= val
       
   
    
print(f'Part2\n  h = {hor_direction}\nx v = {ver_direction}\n{hor_direction*ver_direction}')
file1.close()