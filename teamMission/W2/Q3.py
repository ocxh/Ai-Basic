# 3번 문제
res = []  # 최종 결과 리스트

file_path = "teamMission\W2\data-01-test-score.csv"


def read_file(file_path):
    with open(file_path) as score_data:
        while True:
            data = score_data.readline()  # customer.csv에 한줄씩 data 변수에 저장

            if not data:  # 데이터가 없으면 종료
                break

            li = data.split(",")
            res.append(li)


read_file(file_path)
print(res)
