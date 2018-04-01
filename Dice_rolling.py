leaveprogram=0
while leaveprogram != "q":
    import random
    leaveprogram=raw_input("Press any key to roll the Dice or Enter q to exist \n")
    if leaveprogram == "q":
        break
    randnum=random.randint(1,6)
    if randnum==1:
          print"{-------------}"
          print"{             }"
          print"{      0      }"
          print"{             }"
          print"{-------------}"
          
    if randnum==2:
          print"{-------------}"
          print"{             }"
          print"{   0     0   }"
          print"{             }"
          print"{-------------}"
          
    if randnum==3:
          print"{-------------}"
          print"{      0      }"
          print"{             }"
          print"{    0   0    }"
          print"{-------------}"
          
    if randnum==4:
          print"{-------------}"
          print"{   0    0    }"
          print"{             }"
          print"{   0    0    }"
          print"{-------------}"

    if randnum==5:
          print"{-------------}"
          print"{   0     0   }"
          print"{      0      }"
          print"{   0     0   }"
          print"{-------------}"
          
    if randnum==6:
          print"{-------------}"
          print"{   0    0    }"
          print"{   0    0    }"
          print"{   0    0    }"
          print"{-------------}"
    
