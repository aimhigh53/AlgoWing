import sys
sys.stdin=open("sample_input.txt",'r')
def dijkstra():
    for now in range(city_num):
        for each in road:
            if each[0][0]==now:
                next=each[0][1]
                if ans[next]>each[1]+ans[now]:
                    ans[next]=each[1]+ans[now]

T=int(input())

for test_case in range(1,T+1):

    city_num,road_num=map(int,input().split())
    road=[]
    for _ in range(road_num):
        a,b,c=map(int,input().split())
        road.append([(a,b),c])
    ans=[float('inf')]*(city_num+1)
    ans[0]=0
    dijkstra()
    print("#{} {}".format(test_case,ans[-1]))
