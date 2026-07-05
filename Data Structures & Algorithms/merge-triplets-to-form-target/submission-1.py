class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(target)
        ta, tb, tc = target[0], target[1], target[2]
        isa, isb, isc = False, False, False
        for a, b, c in triplets:
            if a <= ta and b <= tb and c <= tc:
                if a == ta:
                    isa = True
                if b == tb:
                    isb = True
                if c == tc:
                    isc = True
            if isa and isb and isc:
                return True
        return False