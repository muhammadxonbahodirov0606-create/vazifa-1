class Player:
    def __init__(self, ism):
        self.ism = ism
        self.energiya = 100

    def use_energy(self, amount):
        self.energiya = max(0, self.energiya - amount)

    def show_status(self):
        print("O'yinchi:", self.ism)
        print("Energiya:", self.energiya)

oyinchi = Player("Hero")
oyinchi.use_energy(35)
oyinchi.show_status()