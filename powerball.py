import random

stop_on_jackpot = False
print_every = 1000000
prizes = {(0, False):0,
          (1, False):0,
          (2, False):0,
          (3, False):7,
          (4, False):100,
          (5, False):1000000,
          (0, True):4,
          (1, True):4,
          (2, True):7,
          (3, True):100,
          (4, True):50000,
          (5, True):1300000000}


ticket_numbers = set(range(5))
ticket_powerball = 0

balls = tuple(range(69))
powerballs = tuple(range(26))

winnings = 0
spent = 0
max_prize = 0
jackpot = False
while not jackpot or not stop_on_jackpot:
    chosen_balls = random.sample(balls, 5)
    chosen_powerball = random.choice(powerballs)
    
    numbers_hit = sum(1 for x in chosen_balls if x in ticket_numbers)
    powerball_hit = chosen_powerball == ticket_powerball
    matches = (numbers_hit, powerball_hit)
    jackpot = matches == (5, True)
    
    prize = prizes[matches]
    winnings += prize	
    max_prize = max(prize, max_prize)	
    spent += 2
    
    if spent % print_every == 0 or jackpot:			
    	stats = 'spent:{:,}, winnings:{:,}, net:{:,} max_win:{:,}'.format(
    		spent, winnings, winnings-spent, max_prize
    	)
    	print(stats)
