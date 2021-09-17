class Player():
    player_list = []
    
    def __init__(self, user_name, coins, wins, losses, ties):
        self.user_name = user_name
        self.coins = coins
        self.wins = wins
        self.losses = losses
        self.ties = ties
        self.make_list()

    def make_list(self):
        Player.player_list.append(self)

    @classmethod
    def switch_dealer(cls, player_list):
        player_list.insert(0, player_list.pop())

    def __repr__(self):
        return f"{self.user_name} - Coins:{self.coins} - W:{self.wins} - L:{self.losses} - T:{self.ties}"

class CPU(Player):
    def __init__(self, user_name, coins, wins, losses, ties,  difficulty):
        super().__init__(user_name, coins, wins, losses, ties)
        self.difficulty = difficulty

    def __str__(self):
        return f"{self.user_name} - Coins:{self.coins}- Level:{self.difficulty}"

    def difficulty_easy(self):
        pass
    
    def difficulty_medium(self):
        pass

    def difficulty_hard(self):
        pass