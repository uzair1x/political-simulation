# Political Simulation Game - Core Framework

class GameStats:
    def __init__(self):
        self.stats = {
            "Approval Rating": 38,  # Starts at 38%
            "Party Unity": 70,  # Out of 100
            "International Standing": 50,  # Out of 100
            "Public Order": 80,  # Out of 100
            "Treasury Balance": 100.0,  # In £ billions
            "Media Relations": 60,  # Out of 100
            "Muslim Community Support": 50,  # Out of 100
            "Youth Approval": 45,  # Out of 100
            "GDP Growth": 2.5,  # Percent
            "Inflation": 3.2,  # Percent
            "Unemployment": 6.0,  # Percent
            "Pound Sterling Value": 1.3,  # Relative to USD
            "FTSE 100 Index": 7000,  # Stock market index
        }

    def update_stat(self, stat_name, change):
        if stat_name in self.stats:
            self.stats[stat_name] += change
            self.stats[stat_name] = max(0, self.stats[stat_name])  # Prevent negatives
            print(f"{stat_name} updated to {self.stats[stat_name]}.
")

    def display_stats(self):
        print("📊 Current Stats:")
        for stat, value in self.stats.items():
            print(f"- {stat}: {value}")

# Example Usage
game = GameStats()
game.display_stats()  # Show all stats
game.update_stat("Approval Rating", 5)  # Increase Approval Rating by 5%
game.update_stat("Treasury Balance", -10)  # Decrease Treasury Balance by £10 billion