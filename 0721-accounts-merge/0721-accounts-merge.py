class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        # build graph
        graph = defaultdict(list)
        email_to_name = {}

        for account in accounts:
            name = account[0]
            first_account = account[1]

            for email in account[1:]:
                email_to_name[email] = name
                graph[first_account].append(email)
                graph[email].append(first_account)
                
        visited = set()
        res = []

        for email in graph:
            if email not in visited:
                emails = self.bfs(email, graph, visited)
                res.append([email_to_name[email]] + sorted(emails))
        return res

    def bfs(self, email, graph, visited):
        queue = deque([email])
        visited.add(email)
        emails = [email]

        while queue:
            node = queue.popleft()
            for n in graph[node]:
                if n not in visited:
                    visited.add(n)
                    queue.append(n)
                    emails.append(n)
        
        return emails

