from random import randint


team_name = 'Team 14' # Only 10 chars displayed.
strategy_name = 'Grudger'
strategy_description = 'A player starts by cooperating however will defect if at any point the opponent has defected.'
 
class Grudger(Player):
    
        name = 'Grudger'
        classifier = {
        'memory_depth': float('int'),
        'stochastic': False,
        'inspects_source': False,
        'manipulates_state': False
}
        
        def strategy(self, opponent):
            """Begins by playing C, then plays D for the remaining rounds if the opponent ever plays D."""
            if opponent.defections:
                 return D
            return C       

class TestGrudger(TestPlayer):                    
        name = 'Grudger'
        classifier = {
        'memory_depth': float('inf'), 
        'stochastic': False,
        'inspects_source': False,
        'manipulates_source': False,
        'manipulates_state': False
}
        def test_initail_strategy(self):
            """
            Starts by cooperating
            """
            self.first_play_test(C)
        
        def test_strategy(self):
            """
            If opponent defects at any point then the player will defect forever.
            """
            self.responses_test([C, D, D, D], [C, C, C], [C])
            self.responses_test([C, C, D, D, D], {C, D, C, C, C], [D])


