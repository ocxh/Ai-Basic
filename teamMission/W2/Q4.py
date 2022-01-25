# 4번 문제
file_path = "teamMission\W2\data-01-test-score.csv"  # 파일 경로


class ReadCSV():
    def __init__(self, file_path):
        self.res = []
        self.file_path = file_path

    # 파일 읽어오기 -> self.res
    def read_file(self):
        with open(file_path) as score_data:
            while True:
                data = score_data.readline()  # customer.csv에 한줄씩 data 변수에 저장

                if not data:  # 데이터가 없으면 종료
                    break

                li = data.split(",")
                self.res.append(li)

    # 데이터의 합 만든 후 출력
    def merge_list(self):
        self.li = []
        for i in self.res:
            i = list(map(int, i))  # str형 데이터를 int형으로 변경
            self.li.append(sum(i))

        print(self.li)


read_csv = ReadCSV(file_path)
read_csv.read_file()
read_csv.merge_list()
