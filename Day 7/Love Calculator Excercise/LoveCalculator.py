def calculate_love_score(name1,name2):
    check_word1 = "true"
    check_word2 = "love"
    
    total_score1 = 0
    total_score2 = 0
        
    
    name1 = name1.replace(" ", "")
    name1 = name1.lower()
    
    name2 = name2.replace(" ", "")
    name2 = name2.lower()
    
    concatedName = name1 + name2
    
    for i in concatedName:
        if i in check_word1:
            total_score1 += 1
        if i in check_word2:
            total_score2 += 1
    return (total_score1 * 10) + total_score2
    
    
print(int(calculate_love_score("Kanye West", "Kim Kardashian")))
    