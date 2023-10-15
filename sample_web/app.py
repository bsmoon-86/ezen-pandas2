# flask 라이브러리 로드 
from flask import Flask, render_template
import pandas as pd

# Flask class 생성 
# 해당 class에는 생성자함수 존재 
# 입력값으로 파일의 이름
# __name__ : 현재 파일의 이름
app = Flask(__name__)

# 포트번호 설정
_port = 3000

# api 생성
# localhost:3000

# 네비게이터 함수
# localhost:3000/ 요청시 바로 아래의 함수를 호출
@app.route("/")
def index():
    return render_template('index.html')

# localhost:3000/second 요청시 
@app.route("/second")
def second():
    return render_template('second.html')

@app.route("/corona")
def corona():
    # corona.csv 파일 로드 
    df = pd.read_csv('../csv/corona.csv')
    # 컬럼의 이름을 변경
    df.columns = ['인덱스', '등록일시', '총사망자', '총확진자', '게시글번호', 
                  '기준일', '기준시간', '수정일시', '누적의심자', '누적확진율']
    df.sort_values('등록일시', inplace=True)
    df['일일사망자'] = (df['총사망자'].diff()).fillna(0)

    data = df.tail(30)
    data2 = data.to_dict('records')
    print(data2)
    cnt = len(data2)
    columns = data.columns
    return render_template('corona.html', data = data2, cnt = cnt, col = columns)



app.run(port = _port, debug=True)