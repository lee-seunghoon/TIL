# flask_restful 을 사용
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

text_put_args = reqparse.RequestParser()
text_put_args.add_argument('name', type=str, help='텍스트의 주인 이름', required=True)
text_put_args.add_argument('rating', type=int, help='텍스트 분석 후 순위', required=True)
text_put_args.add_argument('contents', type=str, help='자소서 본문', required=True)

texts = {}

# 데이터가 없는 정보를 요청할 경우
def abort_not_exist(textId):
    if textId not in texts:
        # flask_restful의 abort 사용
        abort(404, message='해당하는 ID가 없습니다.')

# class로 api 객체 생성
class TextAnanlysis(Resource):
    def get(self, text_id):
        abort_not_exist(text_id)
        return texts[text_id]
    
    def post(self, text_id):
        args = text_put_args.parse_args()
        texts[text_id] = args
        return texts[text_id]
    
    def put(self, text_id):
        args = text_put_args.parse_args()
        texts[text_id] = args
        return texts[text_id]
        
        
api.add_resource(TextAnanlysis, '/text/<int:text_id>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)