class Athlete:
    def __init__(self, ism, sport, yosh):
        self.ism = ism
        self.sport = sport
        self.yosh = yosh

    def show_info(self):
        print("Ism:", self.ism)
        print("Sport turi:", self.sport)
        print("Yosh:", self.yosh)

athlete = Athlete("Ali", "Futbol", 20)
athlete.show_info()