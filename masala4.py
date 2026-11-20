class Ticket:
    def __init__(self, film, narx, son):
        self.film = film
        self.narx = narx
        self.son = son

    def total_cost(self):
        return self.narx * self.son

    def show_info(self):
        print("Film:", self.film)
        print("Umumiy narx:", self.total_cost())

chipta = Ticket("Labirint", 40000, 3)
print(chipta.total_cost())
chipta.show_info()