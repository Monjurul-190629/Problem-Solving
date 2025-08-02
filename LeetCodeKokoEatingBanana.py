
    def minEatingSpeed( piles, h):
        low = 1
        high = max(piles)
        while low < high:
            mid = (low + high) // 2
            th = sum((pile + mid -1) // mid for pile in piles)
            if(th <= h):
                high = mid
            else:
                low = mid + 1
        return low