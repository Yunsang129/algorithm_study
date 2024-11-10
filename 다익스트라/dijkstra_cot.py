import sys
import heapq
input = sys.stdin.readline
INF = int(1e9) #무한을 의미하는 값으로 10억 설정

n,m = map(int, input().split()) #노드 개수, 간선 개수
start = int(input()) #시작 노드 번호
graph = [[] for i in range(n+1)] #노드에 대한 정보를 담음
visited = [False] * (n+1)   #방문한 적이 있는지 체크하는 목적의 리스트
distance = [INF] * (n+1) #최단거리 테이블 모두 무한으로 초기화


for _ in range(m): #모든 간선 정보 입력받기
    a,b,c = map(int,input().split())
    graph[a].append((b, c)) #a번 노드에서 b번 노드로 가는 비용이 C임
    

def dijkstra(start):
    q = 0
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
        
            
dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])