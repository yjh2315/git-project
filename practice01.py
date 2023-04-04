print("작업을 선택하세요.\n")
print("1. 입력\n2. 계산\n")
in1 = input()
in1 = int(in1)

sGrade, oGrade = 0,0
sGpa, oGpa = 0,0


while(in1 != 2):
    if(in1 == 1):
        print("\n학점을 입력하세요:")
        grade = input()
        grade = int(grade)
        print("평점을 입력하세요:")
        score = input()
        
        match(score):
            case "A+":
                sGrade += grade
                oGrade += grade
                sGpa += grade*4.5
                oGpa += grade*4.5    
            case "A":
                sGrade += grade
                oGrade += grade
                sGpa += grade*4.0
                oGpa += grade*4.0
            case "B+":
                sGrade += grade
                oGrade += grade
                sGpa += grade*3.5
                oGpa += grade*3.5
            case "B":
                sGrade += grade
                oGrade += grade
                sGpa += grade*3.0
                oGpa += grade*3.0
            case "C+":
                sGrade += grade
                oGrade += grade
                sGpa += grade*2.5
                oGpa += grade*2.5
            case "C":
                sGrade += grade
                oGrade += grade
                sGpa += grade*2.0
                oGpa += grade*2.0
            case "D+":
                sGrade += grade
                oGrade += grade
                sGpa += grade*1.5
                oGpa += grade*1.5
            case "D":
                sGrade += grade
                oGrade += grade
                sGpa += grade*1.0
                oGpa += grade*1.0
            case "F":
                oGrade += grade
                oGpa += grade*0.0
            
        print("입력되었습니다.\n")
        print("작업을 선택하세요.\n")
        print("1. 입력\n2. 계산")
        in1 = input()
        in1 = int(in1)

print("\n제출용: ",end='')
print(sGrade,end='')
print("학점 (GPA:",sGpa/sGrade,")")
print("제출용: ",oGrade,"학점 (GPA:",oGpa/oGrade,")")


print("\n프로그램을 종료합니다.")

    