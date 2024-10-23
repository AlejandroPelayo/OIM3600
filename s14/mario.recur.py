def draw(n):
    print("#" * n)
    
def draw_recur(n):
    if n == 0:
        return
    draw_recur(n-1)
    print("#"*n)
    
# draw(4)
draw_recur(4)

