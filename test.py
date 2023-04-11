import random as rand

def makeRandom():
    return int(9999*rand.random())

def functionIn():
    subject_Name = input("\n과목명을 입력하세요:\n")
    subject_Time = input("학점을 입력하세요:\n")
    subject_Score = input("평점을 입력하세요:\n")
    print("입력되었습니다.")
    return subject_Name,int(subject_Time),subject_Score

def checkKeys(inList):
    while True:
        keys = makeRandom()
        checker = 1
        if str(keys) in inList:
            checker = 0
        if checker == 1:
            return str(keys)

def getKey(inDict, in_value):
    for key, value in inDict.items():
        if in_value == value:
            return key
        
def numScore(score1):
    match score1:
        case 'A+':
            numScore1 = 4.5
        case 'A':
            numScore1 = 4
        case 'B+':
            numScore1 = 3.5
        case 'B':
            numScore1 = 3
        case 'C+':
            numScore1 = 2.5
        case 'D+':
            numScore1 = 2
        case 'F':
            numScore1 = 0
    return numScore1

print("작업을 선택하세요.")
print("1. 입력")
print("2. 출력")
print("3. 계산")
operation = int(input())

scoreList = []
codeDict = {}

while True:
    match operation:
        # 입력의 경우
        case 1:
            dataIn = (functionIn())
            # 재수강 데이터라면
            if dataIn[0] in list(codeDict.values()):
                # 값으로부터 키를 받고
                tmpKey = getKey(codeDict, dataIn[0])
                # scoreList의 값인 튜플을 꺼내 키를 비교하고 같다면 리스트에서 삭제
                for listF in scoreList:
                    if  tmpKey == listF[0]:
                        if numScore(dataIn[2])>numScore(listF[2]):
                        # 입력된 값이 평점이 더 높을 경우
                            scoreList.remove(listF)
                            scoreList.append(tuple((tmpKey,dataIn[1],dataIn[2])))
            else:    
                newkey = checkKeys(list(codeDict.keys()))
                codeDict[newkey] = dataIn[0]
                scoreList.append(tuple((newkey,dataIn[1],dataIn[2])))
        # 출력의 경우
        case 2:
            print()
            for i in scoreList:
                print("[%s] %d학점: %s" %(codeDict[i[0]], i[1], i[2]))
        case 3:
            submit_Score = 0
            submit_Time = 0
            open_Score = 0
            open_Time = 0
            
            for i in scoreList:
                temp_Score = numScore(i[2])
                if temp_Score==0:
                    open_Time += i[1]
                else:
                    open_Score += (temp_Score*i[1])
                    open_Time += i[1]
                    submit_Score += (temp_Score*i[1])
                    submit_Time += i[1]
            print("\n제출용: %d학점 (GPA:%.2f)" %(submit_Time, float(submit_Score)/submit_Time))
            print("열람용: %d학점 (GPA:%.2f)" %(open_Time, float(open_Score)/open_Time))

            print("\n프로그램을 종료합니다.")
            break

        case default:
            print("잘못 입력하셨습니다.")


    print("\n작업을 선택하세요.")
    print("1. 입력")
    print("2. 출력")
    print("3. 계산")
    operation = int(input())