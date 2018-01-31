####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'RubyItsAPython' # Only 10 chars displayed.
strategy_name = 'Tempermental Bot'
strategy_description = 'The first round it betrays then it becomes nice..only if youre nice too'
    
def move(my_history, their_history, my_score, their_score): 
    if len(their_history)<100:
        return 'b'
    elif their_history[-1] == 'c':
        return 'c'
