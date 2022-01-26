
class play_game:
    """Starts with score, loops till loss, calcs score.
    """

    def __init__(self): 
        """loops till lost or out of cards. NEEDS DECK
    """
        player_score = 300
        while self.player_score > 0 or deck != 0:  
            guess = input("What is your guess? (+/-) ")
            self.guess = guess
            guess = input("What is your guess? (+/-) ")

    def calc_score(self, cards):
        """start with 300. corrtect earn 100. incorrect lose 75. 
        player reach <=0 game over. NEEDS CARDS
    """
        answer = None
        for card_drawn in cards:
            if new_card_drawn > card_drawn and self.guess == "+":
                correct = answer
                self.player_score += 100
            elif new_card_drawn < card_drawn and self.guess == "-":
                incorrect = answer
                self.player_score -= 75
            elif new_card_drawn < card_drawn and self.guess == "-":
                correct = answer
                self.player_score += 100
            elif new_card_drawn > card_drawn and self.guess == "+":
                incorrect = answer
                self.player_score -= 75

    

    

        