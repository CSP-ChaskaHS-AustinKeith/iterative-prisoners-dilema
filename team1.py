from random import randint

team_name = 'The name the team gives to itself' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
    
    if len(their_history) >= 3 and their_history[-3:] == 'ccc':
        return 'b'
    if len(their_history) >= 4:
        if their_history[-4:] == 'cbcb' or their_history[-4:] == 'bcbc':
            return 'b'
    return their_history[-1:] if randint(0,5) < 5 and their_history else 'b'
    
    
def testing(my_history, their_history, count):
    x = []
    for i in range(count):
        x += move(my_history, their_history, 0, 0)
    print 'Amount of iterations: %s \n * Amount Betrayed: %s \n * Amount Colluded: %s' % (count, len([i for i in x if i == 'b']), len([i for i in x if i == 'c']))
    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             