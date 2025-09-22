class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n_count = Counter(str(n))
        for i in range(31):
            power_of_2 = 1 << i
            power_of_2_counts = Counter(str(power_of_2))
            if n_count == power_of_2_counts:
                return True
        return False
