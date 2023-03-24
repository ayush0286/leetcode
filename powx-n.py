class Solution:
    # O(log n) Time | O(log n) Space
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n *= -1
        return self.pow(x, n, {})

    def pow(self, x, n, memo):
        if (x, n) in memo:
            return memo[(x, n)]

        if n <= 0:
            return 1
        if n == 1:
            return x

        if n % 2 == 0:
            memo[(x, n)] = self.pow(x, n // 2, memo) * self.pow(x, n // 2, memo)
            
        else:
            memo[(x, n)] =  x * self.pow(x, n - 1, memo)
        
        return memo[(x, n)] 
