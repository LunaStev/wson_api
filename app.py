from flask import Flask, request, render_template
import wson

app = Flask(__name__)

# 기본 라우트: HTML 페이지 표시
@app.route('/')
def index():
    return render_template('index.html')

# WSON 데이터 수신 및 응답
@app.route('/api/data', methods=['POST'])
def handle_wson_data():
    # 요청 데이터 가져오기
    wson_file = request.files.get('file')
    
    if not wson_file:
        return wson.dumps({'error': 'No file uploaded'}), 400, {'Content-Type': 'application/wson'}
    
    try:
        # WSON 파일 내용 읽기
        wson_data = wson_file.read().decode('utf-8')
        
        # WSON 데이터를 파싱
        parsed_data = wson.loads(wson_data)

        # 클라이언트에게 전송할 응답 데이터 구성
        response_data = {
            'status': 'success',
            'code': 200,
            'message': 'Data retrieved successfully',
            'data': parsed_data,
        }

        # WSON 형식으로 직렬화하여 응답
        wson_output = wson.dumps(response_data)

        return wson_output, 200, {'Content-Type': 'application/wson'}

    except Exception as e:
        # 오류가 발생한 경우
        error_message = {'error': str(e)}
        return wson.dumps(error_message), 400, {'Content-Type': 'application/wson'}

if __name__ == '__main__':
    app.run(debug=True)
