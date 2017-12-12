class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):

        if A is None:
            return 0

        if len(A)==1:
            if A[0] >= B:
                return 0
            if A[0] < B :
                return 1

        start = 0
        end   = len(A)-1
        while start <= end:
            mid = (start+end)/2
            if A[mid] == B:
                return mid

            if A[mid] > B:
                end = mid - 1
            else:
                start = mid + 1

        return start
