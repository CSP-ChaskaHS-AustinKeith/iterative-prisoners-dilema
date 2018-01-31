####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'JavaCantC#' # Only 10 chars displayed.
strategy_name = 'TheNicePython'
strategy_description = 'Based on previous rounds bot score'

#this looks at thier_history and my_score and if conditions are met it colludes, if not with a simple else statement it betrays
def move(my_history, their_history, my_score, their_score):

    if 'c' in their_history[-1:] and my_score >= -500:   
        return 'c'
        
    else:
        return 'b'      