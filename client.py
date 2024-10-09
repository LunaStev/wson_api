import requests
import wson

def load_wson_from_file(filename):
    """Load WSON data from a file."""
    with open(filename, 'r') as file:
        wson_str = file.read()
    return wson.parse_wson(wson_str)

def main():
    # WSON 파일에서 데이터 로드
    filename = 'data.ws'  # 예시 파일 이름
    try:
        wson_data = load_wson_from_file(filename)
        print("Loaded Data:", "\n", wson_data, "\n")

        # Flask API에 POST 요청 보내기
        response = requests.post('http://127.0.0.1:5000/api/data', data=wson.serialize_wson(wson_data), headers={'Content-Type': 'application/wson'})

        # 서버 응답 출력
        if response.status_code == 200:
            print("Server Response:", "\n", response.text, "\n")
        else:
            print("Error:", response.status_code, response.text)

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
