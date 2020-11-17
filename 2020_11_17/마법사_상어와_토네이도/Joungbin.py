def snail() :
    sn=[[1]*n for _ in range(n)]
    dir=1
    num=n**2
    cnt=n
    x, y=0, -1
    while (cnt!=0):
        for i in range(cnt):
            y+=dir
            sn[x][y]=num
            num-=1
        cnt-=1
        for i in range(cnt):
            x+=dir
            sn[x][y]=num
            num-=1
        dir=dir*(-1)
    return sn

def perc(nx, ny, k, per) :
    global ans, diff
    d=int(k*per)
    if (0<=nx<n and 0<=ny<n): sand[nx][ny]+=d
    diff+=d

def dust_change(x, y, dir) :
    global diff
    k=sand[x][y]
    sand[x][y]=0
    for i in range(2) :
        per=0.1
        nx, ny=x+dx[dir], y+dy[dir]
        if(x==nx) : nx=x+(-1)**i
        if(y==ny) : ny=y+(-1)**i
        perc(nx, ny, k, per)
        per=0.01
        nx, ny = x-dx[dir], y-dy[dir]
        if (x==nx) : nx=x+(-1)**i
        if (y==ny) : ny=y+(-1)**i
        perc(nx, ny, k, per)
    for i in range(1, 4, 2) :
        per=0.02
        nx, ny=x+2*dx[(dir+i)%4], y+2*dy[(dir+i)%4]
        perc(nx, ny, k, per)
        per=0.07
        nx, ny=x+dx[(dir+i)%4], y+dy[(dir+i)%4]
        perc(nx, ny, k, per)
    per=0.05
    nx, ny=x+2*dx[dir], y+2*dy[dir]
    perc(nx, ny, k, per)
    nx, ny=x+dx[dir], y+dy[dir]
    if(0<=nx<n and 0<=ny<n) : sand[nx][ny]+=(k-diff)
    #print(k, diff, ans)


dx=[0, 1, 0, -1]
dy=[-1, 0, 1, 0]

n=int(input())
sand=[[*map(int, input().split())] for _ in range(n)]
seq=snail()
tor_x, tor_y=n//2, n//2
dir=0
diff=0

ans=sum(map(sum, sand))



for i in range(1, n**2):
    diff=0
    for j in range(4):
        nx, ny=tor_x+dx[j], tor_y+dy[j]
        if(nx<0 or nx>=n or ny<0 or ny>=n) : continue
        if(seq[nx][ny]==i+1) :
            tor_x, tor_y=nx, ny; dir=j; break
    dust_change(tor_x, tor_y, dir)

ans-=sum(map(sum, sand))

print(ans)