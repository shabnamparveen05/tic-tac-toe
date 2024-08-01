def sum(a,b,c):
    return a+b+c
def printScreen(xstate,ystate):
    zero=('x' if xstate[0] else ('O' if ystate[0] else 0))
    one=('x' if xstate [1] else ('O' if ystate[1] else 1))
    two=('x' if xstate[2] else ('O' if ystate[2] else 2))
    three=('x' if xstate[3] else ('O' if ystate[3] else 3))
    four = ('x' if xstate[4] else ('O' if ystate[4] else 4))
    five = ('x' if xstate[5] else ('O' if ystate[5] else 5))
    six= ('x' if xstate[6] else ('O' if ystate[6] else 6))
    seven= ('x' if xstate[7] else ('O' if ystate[7] else 7))
    eight= ('x' if xstate[8] else ('O' if ystate[8] else 8))

    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")
def checkwin (xstate, ystate):
    xwin=[[0,1,2], [3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[2,4,6],[0,4,8]]
    for win in xwin:
        if(sum(xstate[win[0]],xstate[win[1]],xstate[win[2]])==3):
            print("x's won the match. ")
            return 1
        if (sum(ystate[win[0]], ystate[win[1]], ystate[win[2]]) == 3):
            print("O's won the match. ")
            return 0
    return -1
if __name__ == '__main__':
    xstate = [0,0,0,0,0,0,0,0,0]
    ystate= [0,0,0,0,0,0,0,0,0]
    turn = 1 # 1 for x and 0 for O
    print('welcome to tic tac toe')
    while(True):
        printScreen(xstate,ystate)
        if(turn == 1):
            print("x's chance")
            value =int(input(" please enter a value: "))
            xstate[value]=1
        else:
            print("O's chance")
            value=int(input("please enter a value: "))
            ystate[value]=1
        cwin=checkwin(xstate,ystate)
        if(cwin!=-1):
            break
        turn=1-turn

