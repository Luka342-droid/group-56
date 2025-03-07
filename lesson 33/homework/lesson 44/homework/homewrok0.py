def hero(bullets, dragons):
    # ყოველ დრაკონს სჭირდება 2 ტყვია დასამარცხებლად
    # თუ ტყვიების რაოდენობა (bullets) მეტია ან ტოლია 
    # დრაკონების რაოდენობის ორმაგზე (dragons * 2) მაშინ გმირი გადარჩება
    return bullets >= dragons * 2

# 3
def reverse_seq(n):
    return list(range(n, 0, -1))
# 4
def rps(player1, player2):
    if player1 == player2:
        return "Draw!"
    
    wins = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    
    if wins[player1] == player2:
        return "Player 1 won!"
    else:
        return "Player 2 won!"

# 5

# 6
def count_sheep(n):
    return "".join(f"{i} sheep..." for i in range(1, n + 1))

# 7
def get_grade(s1, s2, s3):
    avg = (s1 + s2 + s3) / 3  # Calculate the average score
    
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'
