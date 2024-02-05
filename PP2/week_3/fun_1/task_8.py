def spy_game(x):
    zero=0
    seven=False
    for i in x:
        if(i==0 and zero==0):
            zero+=1
        elif(i==0 and zero==1):
            zero+=1
        elif(i==7 and zero==2):
            seven=True
            break
    return seven                    
print(spy_game([1,2,4,0,0,7,5]) )
print(spy_game([1,0,2,4,0,5,7]) )
print(spy_game([1,7,2,0,4,5,0])) 