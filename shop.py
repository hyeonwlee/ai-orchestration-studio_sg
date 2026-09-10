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
    def __init(self, order_id, customer, items):
        self.order_id = order_id
        self.customer = customer
        self.items = items

    def total_price(self):
        sum_of_items = sum([item[1] for item in self.items])
        return int(sum_of_items * (1 - self.get_discount_rate()))

    def add_item(self, name, price):
        self.items += (name, price)

    def pay(self):
        self.customer.add_points(self.total_price())