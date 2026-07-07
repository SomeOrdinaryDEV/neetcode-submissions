class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        adj = defaultdict(list)

        for src, dest in sorted(tickets)[::-1]:
            adj[src].append(dest)

        res = []
        def search(node):
            while adj[node]:
                dst = adj[node].pop()
                search(dst)
            res.append(node)

        search("JFK")
        return res[::-1]

