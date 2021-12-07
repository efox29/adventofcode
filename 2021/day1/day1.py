
file1 = open('input.txt','r')
prev_depth = -1
count = 0
for line in file1:
    depth = int(line.strip())
    if(depth > prev_depth and prev_depth != -1):
        count = count + 1
    prev_depth = depth

print(count)
file1.close()





file1 = open('input.txt','r')

while



file1.close()