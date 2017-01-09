import pprint

def matchup(hand1,hand2):
    gen = -1
    wins = 0
    ties = 0
    loses = 0
    for gen in generate_small(0,216):
        pool = gen
        if winner(pool,hand1,hand2) == None:
            ties = ties+1
            # print "tie"
        elif winner(pool,hand1,hand2) == True:
            wins = wins+1
            # print "win"
        elif winner(pool,hand1,hand2) == False:
            loses = loses+1
            # print "loss"
    print hand1
    print hand2
    print "wins/loses/ties: "+str(wins)+"/"+str(loses)+"/"+str(ties)
    return [wins,loses,ties]

def analyze():
    # pool = [4,5,2]
    # hand1 = [6,3]
    # hand2 = [1,3]

    # print pool + hand1
    # print pool + hand2
    # print winner(pool,hand1,hand2)
    # print straight(pool,hand1)
    # print straight(pool,hand2)
    # print six_high(pool,hand1)
    # print six_high(pool,hand2)
    # print four_kind(pool,hand1)
    # print four_kind(pool,hand2)
    gen = -1
    record = generate_record()
    wins = 0
    losses = 0
    ties = 0            
    # while sum(gen) <= sum([6,6,6,6,6,6,6]):
    for gen in generate(0,279936): #6^7 = 279936
        temp = gen
        pool = temp[0:3]
        hand2 = temp[3:5]
        hand1 = temp [5:7]
        # pool = temp [4:7]
        # hand2 = temp [2:4]
        # hand1 = temp [0:2]
        key = hand1[0]*10 + hand1[1]
        # print pool
        # print hand1
        # print hand2
        if winner(pool,hand1,hand2) == None:
            record[key]["ties:"] = record[key]["ties:"]+1
            ties += 1
            # print "tie"
        elif winner(pool,hand1,hand2) == True:
            record[key]["wins:"] = record[key]["wins:"]+1
            wins += 1
            # print "win"
        elif winner(pool,hand1,hand2) == False:
            record[key]["loses:"] = record[key]["loses:"]+1
            losses += 1
            # print "loss"
    
    pp = pprint.PrettyPrinter()
    pp.pprint(record)
    print str(wins)+" "+str(losses)+" "+str(ties)
    best_responses(record)

def best_responses(record):
    winners = []
    for key in record:
        if record[key]["wins:"] > record[key]["loses:"]:
            winners.append(key)
    # print winners
    
    copy = winners
    results = {}
    for winner in winners:
        results[winner] = {}
        results[winner]["wins:"] = 0
        results[winner]["loses:"] = 0
        results[winner]["ties:"] = 0
        for other in copy:
            win = [winner/10,winner%10]
            oth = [other/10,other%10]
            r = matchup(win,oth)
            results[winner]["wins:"] += r[0]
            results[winner]["loses:"] += r[1]
            results[winner]["ties:"] += r[2]

    pp = pprint.PrettyPrinter()
    pp.pprint(results)

def generate_record():
    dic = {}
    for i in range(0,6):
        for k in range(0,6):
            key = (i+1)*10 + k+1
            dic[key] = {}
            dic[key]["ties:"] = 0
            dic[key]["wins:"] = 0
            dic[key]["loses:"] = 0
    return dic

def generate_small(start,end):
    current = start
    while current < end:
        lst = []
        temp = current
        for i in range (0,4):
            lst.append((temp%6)+1)
            temp = temp/6
        # print lst
        current += 1
        yield lst

def generate(start,end):
    current = start
    while current < end:
        lst = []
        temp = current
        for i in range (0,7):
            lst.append((temp%6)+1)
            temp = temp/6
        # print lst
        current += 1
        yield lst

def winner(pool,hand1,hand2):
    if straight(pool,hand1) > straight(pool,hand2):
        return True
    if straight(pool,hand1) < straight(pool,hand2):
        return False
    if (straight(pool,hand1) == straight(pool,hand2)) and (straight(pool,hand1) != -1):
        return None
    if six_high(pool,hand1) > six_high(pool,hand2):
        return True
    if six_high(pool,hand1) < six_high(pool,hand2):
        return False
    if six_high(pool,hand1) == six_high(pool,hand2) and six_high(pool,hand1) != -1:
        return None
    if four_kind(pool,hand1) > four_kind(pool,hand2):
        return True
    if four_kind(pool,hand1) < four_kind(pool,hand2):
        return False
    return None

def straight(pool,hand):
    total = pool + hand
    num = -1
    for i in range(6,3,-1):
        if i in total:
            num = i
            for x in range(1,4):
                if i-x not in total:
                    num = -1
                    break
            if num != -1:
                return num
    return -1


def six_high(pool,hand):
    total = pool + hand
    if 6 in total:
        return sum(total)-min(total) #5 dice, top 4 count
    return -1

def four_kind(pool,hand):
    total = pool + hand
    for i in range (5,0,-1):
        if total.count(i) >= 4:
            return i
    return -1

# analyze()
matchup([4,5],[3,4])
