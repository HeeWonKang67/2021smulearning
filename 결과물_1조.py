print("====================================")
print()
print(" C O D E  : 방 탈 출 ")
print("당신은 이 방을 탈출해야 합니다.")
print("이 방을 탈출하려면 _ _ _ _ 네 자리의 코드가 필요합니다.")
print("이 코드는 '상명대학교'와 관련이 깊습니다.")
print("하나의 방을 통과할 때마다 영어 스펠링이 하나씩 주어집니다.")
print("스펠링을 조합하여 코드를 맞추고 방을 탈출해보세요!")
print()
print("====================================")
print()
point = 1
print("[첫 번째 방] 상명 퀴즈")
print("상명대를 주제로 한 퀴즈가 나갑니다. 정답을 맞춰보세요.")
print("* 힌트를 원하시면 '힌트'라고 입력해주세요.")
print()

while point == 1:
    quiz = input("Q. 상명대학교의 설립자 이름은? A. ")
    
    if quiz == "배상명":
        print()
        print("정답입니다. ★ 얻은 코드 : E ★")
        print()
        print("====================================")
        point += 1
        print()
        print("[두 번째 방] 영어 명언 퀴즈")
        print("빈칸에 들어갈 알맞은 말을 알파벳 소문자로 작성하세요. (띄어쓰기 포함)")
        print("* 힌트를 원하시면 '힌트'라고 입력해주세요.")
        print()
                
    elif quiz == "힌트":
        print("힌트 : 배○○")
        
    else:
        print("오답입니다. 다시 한번 도전해보세요.")
        

while point == 2:
    blank = input("Q. \'To be , or ○○○ ○○ ○○, that is the question.\'  A. ")

    if blank == "not to be":
        print()
        print("정답입니다. ★ 얻은 코드 : D ★")
        print()
        print("====================================")
        point += 1
        print()
        print("[세 번째 방] 금액 계산하기")
        print("카페 직원과 상명이의 대화를 보고 상명이가 내야 하는 금액을 맞춰보세요.")
        print("입력하실 때에는 숫자만 입력해주세요.")
        print()
        print(" ↓  ↓  ↓  ↓  ↓ ")
        print()
        print("~~~~~~~~~~메뉴판~~~~~~~~~~~")
        print("아메리카노                      3,700")
        print("카페라떼                          4,200")
        print("바닐라라떼                      4,500")
        print("카라멜 마끼아또             5,600")
        print("카페모카                          5,500")
        print("(신메뉴!) 달고나라떼  6,000")
        print("딸기케이크                      6,100")
        print("치즈케이크                      5,400")
        print("초코케이크                      5,600")
        print("마카롱                              2,300")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()
        print("직원 : 어서오세요, 홈즈 카페에 오신 것을 환영합니다.")
        print("            주문 도와드릴까요?")
        print("상명이 : 네. 아메리카노 하나, 치즈케이크 하나 주세요.")
        print("직원 : 고객님, 저희 신메뉴 하나 나왔는데 추천해드려도 될까요?")
        print("상명이 : 네, 추천해주세요.")
        print("직원 : 오늘 새로 나온 신메뉴인 달고나라떼 입니다.")
        print("            원가는 6000원이지만 이번 달은 50% 할인 중입니다.")
        print("상명이 : 아, 그럼 추가로 달고나 라떼 두 잔 구매할게요!")
        print("                그리고 제가 10% 할인쿠폰이 있는데 사용 가능할까요?")
        print("직원 : 달고나라떼는 이미 할인을 하고 있어서, 10% 할인 적용이 되지 않습니다.")
        print("            그래도 괜찮으신가요?")
        print("상명이 : 네, 그렇게 해 주세요. 감사합니다.")
        print()
        
    elif blank == "힌트":
        print("힌트 : \'to be\'의 반대말")
        
    else:
        print("오답입니다. 다시 한번 도전해보세요.")


while point == 3:
    cafe = input("Q. 최종 금액은? 숫자만 입력해주세요.  A. ")
    
    if cafe == "14190":
        print()
        print("정답입니다. ★ 얻은 코드 : E ★")
        print()
        print("====================================")
        point += 1
        print()
        print("[네 번째 방] 파이썬 퀴즈")
        print("다음은 1부터 10까지의 합을 While문으로 나타낸 것입니다. For문으로 바꾼 코드의 빈칸을 채우세요.")
        print("* 정답에 콤마(,)와 띄어쓰기( )를 포함해주세요. ex. 4, 23, 5")
        print()
        print("sum = 0")
        print("count = 1")
        print()
        print("while 0 < count < 11 : ")
        print("          sum += count")
        print("          count += 1")
        print()
        print("print(sum)")
        print()
        print(" ↓  ↓  ↓  ↓  ↓ ")
        print()
        print("sum = 0")
        print()
        print("for i in range( ○, ○, ○ ): ")
        print("          sum += i")
        print()
        print("print(sum)")
        print()
        
    else:
        print("오답입니다. 다시 한번 도전해보세요.")


while point == 4:
    py = input("Q. 빈칸에 들어갈 숫자는?(ex. 4, 23, 5)   A. ")

    if py == "1, 11, 1":
        print()
        print("정답입니다. ★ 얻은 코드 : R ★")
        print()
        print("====================================")
        point += 1
        print("당신은 네 개의 방을 모두 통과하셨습니다.")
        print(" 획득한 코드는 E, D, E, R 입니다.")
        print("이 알파벳을 조합하여 _ _ _ _ 네 자리의 코드를 맞춰보세요!")
        print("정답이라면, 당신은 이 방탈출 게임을 클리어하실 수 있습니다.")
        print("* 기회는 한 번 뿐입니다.")
        print()

    else:
        print("오답입니다. 다시 한번 도전해보세요.")


while point == 5:
    final = input("Q. 상명대와 연관된 최종 코드는? _ _ _ _  A. ")

    if final == "DEER" or "deer" :
        print()
        print("정답입니다. 탈출을 축하드립니다!")
        print()
        print("지금까지 C O D E  : 방 탈 출 게임을 플레이해주셔서 감사합니다.")
        print()
        print("====================================")
        break

    else:
        print("오답입니다. 당신은 끝내 이 게임을 클리어하지 못하셨습니다.")
        print()
        print("지금까지 C O D E  : 방 탈 출 게임을 플레이해주셔서 감사합니다.")
        print()
        print("====================================")
        break
    
    


        


    
