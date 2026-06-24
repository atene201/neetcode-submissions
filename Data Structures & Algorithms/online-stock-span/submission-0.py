class StockSpanner:

    def __init__(self):
        self.stock = []

    def next(self, price: int) -> int:
        # find an algo that will count the number of consecutive 
        # days before that price was either <= to the price
        self.stock.append(price)
        res = 1
        if len(self.stock) > 0:
            for i in range(len(self.stock)-2,-1,-1):
                if self.stock[i] <= price:
                    res += 1
                else:
                    return res
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)