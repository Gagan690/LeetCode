class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        from itertools import permutations
        result = set()
        for i in range(1, len(tiles) + 1):
            for perm in permutations(tiles, i):
                result.add("".join(perm))
        return len(result)
