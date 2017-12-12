class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):

        if A == 0 or A == 1:
            return A
        start = 2
        end = long(A)
        while start<end:
            mid = (start + end)/2
            mid_sq = long(mid * mid)
            if mid_sq == A:
                return mid
            if mid_sq < A and (mid+1)*(mid+1) > A:
                return mid

            if mid_sq > A:
                end = long(mid - 1)
            else:
                start = long(mid+1)

        return min(start, end)
            
