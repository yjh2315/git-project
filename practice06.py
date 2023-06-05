from grade_calculator.calculator import *

course = Course()

while True:
    print("작업을 선택하세요")
    print("    1. 입력")
    print("    2. 출력")
    print("    3. 조회")
    print("    4. 계산")
    print("    5. 파일 저장")
    print("    6. 파일 불러오기")
    print("    7. 종료")

    input_Case = input()

    # 입력값별 작업
    if input_Case == "1":
        try:
            course.inputCourse()
        except Exception:
            print("잘못된 입력입니다.")

    elif input_Case == "2":
        course.outputCourse()

    elif input_Case == "3":
        try:
            course.checkCourse()
        except Exception:
            print("잘못된 입력입니다.")

    elif input_Case == "4":
        course.calculateCourse()

    elif input_Case == "5":
        course.makeFile()

    elif input_Case == "6":
        course.setVal()

    elif input_Case == "7":
        break

    else:
        print("잘못된 입력입니다.")
        continue

print("프로그램을 종료합니다.")
