S = input()

sound = {1:"Do", 2:"Do", 3:"Re", 4:"Re", 5:"Mi", 6:"Fa", 
         7:"Fa", 8:"So", 9:"So", 10:"La", 11:"La", 12:"Si"}

Piano = ["W", "B", "W", "B", "W", "W", "B", "W", "B", "W", 
         "B", "W"]

for i in range(20):
    if list(S)[:12] == Piano:
        print(sound[i%12+1])
        exit()
    else:
        tmp = Piano[0]
        Piano =  Piano[1:]
        Piano.append(tmp)
