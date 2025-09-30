class Solution:
    def numOfUnplacedFruits(self, fruits, baskets) -> int:
        used = [False] * len(baskets)
        unplaced_count = 0

        for fruit_quantity in fruits:
            placed = False

            for j in range(len(baskets)):
                if not used[j] and baskets[j] >= fruit_quantity:
                    used[j] = True
                    placed = True
                    break

            if not placed:
                unplaced_count += 1

        return unplaced_count
