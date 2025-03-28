def get_score():
    score=input("PLEASE Enter your score\t")
    return score
def is_score_available(score:int)->bool:
    if score>100:
        print("Entered score is too high")
        return False
    elif score<0:
        print("Entered Score must be positive!")
        return False
    return True
def calc_grade(score:int)->str:
    if not is_score_available(score):
        print("[*] INVALID SCORE")
        exit()
    if score>90:
        return "A"
    if score>60:
        return "B"
    if score>40:
        return "C"
    else:
        return "D"
score=int(get_score())
print(calc_grade(score))