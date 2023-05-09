import random as rand

class Course:
    def __init__(self):
        self.history = []
        self.course_id = {}
        self.submit_score = {}
        self.open_score = {}

    @classmethod
    def numScore(cls,score1):
        outVal = 0
        match score1:
            case 'A+':
                outVal = 4.5
            case 'A':
                outVal = 4
            case 'B+':
                outVal = 3.5
            case 'B':
                outVal = 3
            case 'C+':
                outVal = 2.5
            case 'C':
                outVal = 2
            case 'D+':
                outVal = 1.5
            case 'D':
                outVal = 1
            case 'F':
                outVal = 0
        return outVal

    def strScore(cls,score1):
        match score1:
            case 4.5:
                return 'A+'
            case 4:
                return 'A'
            case 3.5:
                return 'B+'
            case 3:
                return 'B'
            case 2.5:
                return 'C+'
            case 2:
                return 'C'
            case 1.5:
                return 'D+'
            case 1:
                return 'D'
            case 0:
                return 'F'

    def makeKeys(self, course_Name):
        if course_Name not in self.course_id:
            while True:
                keys = int(9999*rand.random())
                checker = 1
                if str(keys) in self.course_id.keys():
                    checker = 0
                if checker == 1:
                    self.course_id[course_Name] = str(keys)
                    return str(keys)
        else:
            print("여기옴")
            return str(self.course_id[course_Name])

        
    def getKey(self, in_value):
        for key, value in self.course_id.items():
            if str(in_value) == value:
                return key

            
    def inputCourse(self):
        subject_Name = input("과목명을 입력하세요:")
        subject_Time = int(input("학점을 입력하세요:"))
        subject_Strscore = input("평점을 입력하세요:")
        print("입력되었습니다.")

        subject_Score = self.numScore(subject_Strscore)
        course_id=self.makeKeys(subject_Name)

        #openScore 등록
        if subject_Score>0:
            if course_id in self.open_score:
                #재수강처리
                if subject_Score>self.open_score[course_id][1]:
                    self.open_score[course_id] = (subject_Time,subject_Score)
            else:
                self.open_score[course_id] = (subject_Time,subject_Score)

        #submitScore 등록
        if course_id in self.submit_score:
            #재수강처리
            if subject_Score>self.submit_score[course_id][1]:
                self.submit_score[course_id] = (subject_Time,subject_Score)
                #기록 정리(기존값 삭제, 새 값 추가)
                for history_Check in self.history:
                    if history_Check[0] == course_id:
                        
                        self.history.remove(history_Check)
                        self.history.append((course_id,subject_Time,subject_Score))
                        break
        else:
            self.submit_score[course_id] = (subject_Time,subject_Score)
            self.history.append((course_id,subject_Time,subject_Score))

    def outputCourse(self):
        for temp_History in self.history:
            print("[",end='')
            print(self.getKey(temp_History[0]),end='')
            print("] "+str(temp_History[1])+"학점:"+self.strScore(temp_History[2]))

    def checkCourse(self):
        course_name = input('과목명을 입력하세요: ')

        for course in (self.history):
            if course_name == self.getKey(course[0]):
                print('[' + self.getKey(course[0]) + '] ', end='')
                print(str(course[1]) + '학점: ' + self.strScore(course[2]))
                break
        else:
            print('해당하는 과목이 없습니다.')


    def calculateCourse(self):
        submit_Score, submit_Time = 0.0,0
        open_Score, open_Time = 0.0,0

        for temp_Course in self.submit_score:
            submit_Time += self.submit_score[temp_Course][0]
            submit_Score += self.submit_score[temp_Course][1]*self.submit_score[temp_Course][0]

        for temp_Course in self.open_score:
            open_Time += self.open_score[temp_Course][0]
            open_Score += self.open_score[temp_Course][1]*self.open_score[temp_Course][0]

        submit_Score /= submit_Time
        open_Score /= open_Time

        print('제출용: ' + str(submit_Time) + '학점' + '(GPA: ' + str(submit_Score) + ')')
        print('열람용: ' + str(open_Time) + '학점' + '(GPA: ' + str(open_Score) + ')')


course = Course()

while True:
    print('작업을 선택하세요')
    print('    1. 입력')
    print('    2. 출력')
    print('    3. 조회')
    print('    4. 계산')
    print('    5. 종료')

    input_Case = input()
    
    # 입력값별 작업
    if input_Case == '1':
        course.inputCourse()
        
    elif input_Case == '2':
        course.outputCourse()
        
    elif input_Case == '3':
        course.checkCourse()

    elif input_Case == '4':
        course.calculateCourse()
        
    elif input_Case == '5':
        break

    else:
        continue
        
print('프로그램을 종료합니다.')