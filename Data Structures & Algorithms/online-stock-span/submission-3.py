class StockSpanner:

    def __init__(self):
        self.stock = [] # will hold (price, span)

    def next(self, price: int) -> int:
        # [(100, 1), (85,1), (65, 3)]
        res = 1
        while self.stock and self.stock[-1][0] <= price:
            res += self.stock[-1][1]
            self.stock.pop()
        self.stock.append((price,res))
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)