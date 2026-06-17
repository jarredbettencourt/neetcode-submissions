class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visit_set = set()
        visit_set.add((0,0))
        x, y = 0, 0
        for dir in path:
            if dir == 'N':
                y += 1
            elif dir == 'E':
                x += 1
            elif dir == 'S':
                y -= 1
            elif dir == 'W':
                x -= 1
            if (x, y) in visit_set:
                return True
            visit_set.add((x, y))
        return False