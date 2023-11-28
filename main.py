import pyautogui
import time
import itertools
from itertools import product
import signal

original=[]

for i in range (97,123) :
    if(chr(i) in "fxzq") :
        continue
    original.append(chr(i))

for i in range (0,10) :
    original.append(str(i))

original.append('!')
original.append('@')
#print (original)

ans=['' for i in range(10)]

limit=5
con=[]
f=open('t1.txt','w')
def backtracking(cnt, prev, check) :
    if(cnt==limit) :
        f.write(''.join(ans))
        f.write(' ')
        return
    for i in original :
        if prev == '': #첫 시작이면
            ans[cnt]=i
            backtracking(cnt+1, i, False)
        else :
            if(cnt<=2 and i in "!@") :
                    return
            if(prev == i) :
                if(check) :
                    return
                else :
                    ans[cnt]=i
                    backtracking(cnt+1, i, True)
            else :
                ans[cnt]=i
                backtracking(cnt+1, i, False)
backtracking(0,'',False)

'''
for i in range (5, 11) :
    no_consecutive = []
    for perm in product(original, repeat=i):
        valid = True
        for i in range(len(perm) - 2):
            if perm[i] == perm[i + 1] == perm[i + 2]:
                valid = False
                break
        if valid:
            no_consecutive.append(perm)
    for j in (no_consecutive) :
           pyautogui.moveTo(1054,588)
           pyautogui.click(1054,588)
           pyautogui.typewrite(j)
           pyautogui.typewrite(['enter'])
           time.sleep(0.3)
           pyautogui.doubleClick(351,204)
           pyautogui.hotkey('delete')

'''
