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