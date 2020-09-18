"""
输出 9*9 乘法口诀表。
"""
for r in range(1,10):
    print()
    for c in range(1,r+1):
        print(f"{r}*{c}=",r*c,end=" ")
    # print("\n")