class MurderStatsManager:
    def __init__(self):
        self.data = {}

    def add_data(self, continent, country, city, count):
        if continent not in self.data:
            self.data[continent] = {}
        if country not in self.data[continent]:
            self.data[continent][country] = {}
        self.data[continent][country][city] = count

    def get_stats(self):
        return self.data
if __name__ == "__main__":
    manager = MurderStatsManager()
    manager.add_data("Europe", "Estonia", "Tallinn", 5)
    manager.add_data("Europe", "Finland", "Helsinki", 3)
    manager.add_data("Asia", "Japan", "Tokyo", 8)

    print(manager.get_stats())

 
