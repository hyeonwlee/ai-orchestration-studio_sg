class Customer:
    def __init__(self, name, grade="basic"):
        self.name = name
        self.grade = grade
        self.points = 0

    def add_points(self, amount):
        self.points += int(amount * 0.05)

    def get_discount_rate(self):
        if self.grade == "vip": return 0.10
        elif self.grade == "basic": return 0.03

    def summary(self):
        return f"[{self.grade}] {self.name} (포인트: {self.points:,})"

class Order:
    def __init__(self, order_id, customer, items):
        self.order_id = order_id
        self.customer = customer
        self.items = items

    def total_price(self):
        sum_of_items = sum([item[1] for item in self.items])
        return int(sum_of_items * (1 - self.customer.get_discount_rate()))

    def add_item(self, name, price):
        self.items += (name, price)

    def pay(self):
        self.customer.add_points(self.total_price())

# 검증 코드
c1 = Customer("Jone", "vip")
c2 = Customer("Jane")

o1 = Order("A-1001", c1, [("라떼", 5500), ("크루아상", 4200)])
o1.pay()
print(f"[{o1.order_id}] \n주문 총액: {o1.total_price():,}\n고객 정보: {o1.customer.summary()}\n")

o2 = Order("A-1002", c1, [("아메리카노", 4000)])
o2.pay()
print(f"[{o2.order_id}] \n주문 총액: {o2.total_price():,}\n고객 정보: {o2.customer.summary()}\n")

o3 = Order("A-1003", c2, [("라떼", 5500), ("쿠키", 3500)])
o3.pay()
print(f"[{o3.order_id}] \n주문 총액: {o3.total_price():,}\n고객 정보: {o3.customer.summary()}\n")