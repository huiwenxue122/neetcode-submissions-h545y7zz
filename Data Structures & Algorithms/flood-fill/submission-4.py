class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]
        if orig == color:
            return image
        m = len(image)
        n = len(image[0])

        dirs = [(1,0), (-1,0),(0,1),(0,-1)]
        q = deque([(sr, sc)])
        image[sr][sc] = color

        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                newr = r + dr
                newc = c + dc
                if 0 <= newr < m and 0 <= newc < n and image[newr][newc] == orig:
                    image[newr][newc] = color
                    q.append((newr, newc))
        return image
