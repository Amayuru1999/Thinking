if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
i_values=[]
j_values=[]
k_values=[]
final_values = []
for i in range(x+1):
    i_values.append(i)

for j in range(y+1):
    j_values.append(j)

for k in range(z+1):
    k_values.append(k)

for i in i_values:
    for j in j_values:
        for k in k_values:
            if(i+j+k != n):
                final_values.append(i)
                final_values.append(j)
                final_values.append(k)



chunk_size = 3
chunks = [final_values[i:i + chunk_size] for i in range(0, len(final_values), chunk_size)]
print(chunks)