# DataBase 만들기

from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

# DB 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class Hjgrace(db.Model):
    h_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    q_1 = db.Column(db.String(10000), nullable=False)
    q_2 = db.Column(db.String(10000), nullable=False)
    q_3 = db.Column(db.String(10000), nullable=False)
    q_4 = db.Column(db.String(10000), nullable=False)
    q_5 = db.Column(db.String(10000), nullable=False)
    label = db.Column(db.Integer, nullable=False)
    cosine = db.Column(db.Float, nullable=True)
    rank = db.Column(db.Integer, nullable=True)
    
    def __repr__(self):
        return "Hjgrace(name={}, label={})".format(self.name, self.label)

# DB 만들기
# 맨 처음에 만들고 지우기
#db.create_all()

text_put_args = reqparse.RequestParser()
text_put_args.add_argument('name', type=str, help='텍스트의 주인 이름', required=True)
text_put_args.add_argument('q_1', type=str, help='지원동기 및 입사 후 포부', required=True)
text_put_args.add_argument('q_2', type=str, help='히든그레이스는 어떤 회사인가', required=True)
text_put_args.add_argument('q_3', type=str, help='히든그레이스가 보완할 점', required=True)
text_put_args.add_argument('q_4', type=str, help='채용 된다면 일할 수 있는 기간, 오래 일하는 데 문제 되는 요소', required=True)
text_put_args.add_argument('q_5', type=str, help='고린도전서 읽은 후 기술', required=True)
text_put_args.add_argument('label', type=int, help='우수인재여부', required=True)
text_put_args.add_argument('cosine', type=float, help='코사인 유사도', required=False)
text_put_args.add_argument('rank', type=int, help='인재순위', required=False)

text_update_args = reqparse.RequestParser()
text_update_args.add_argument('name', type=str, help='텍스트의 주인 이름')
text_update_args.add_argument('q_1', type=str, help='지원동기 및 입사 후 포부')
text_update_args.add_argument('q_2', type=str, help='히든그레이스는 어떤 회사인가')
text_update_args.add_argument('q_3', type=str, help='히든그레이스가 보완할 점')
text_update_args.add_argument('q_4', type=str, help='채용 된다면 일할 수 있는 기간, 오래 일하는 데 문제 되는 요소')
text_update_args.add_argument('q_5', type=str, help='고린도전서 읽은 후 기술')
text_update_args.add_argument('label', type=int, help='우수인재여부')
text_update_args.add_argument('cosine', type=float, help='코사인 유사도')
text_update_args.add_argument('rank', type=int, help='인재순위')


resource_fields = {
    'h_id' : fields.Integer,
    'name' : fields.String,
    'q_1' : fields.String,
    'q_2' : fields.String,
    'q_3' : fields.String,
    'q_4' : fields.String,
    'q_5' : fields.String,
    'label' : fields.Integer,
    'cosine' : fields.Float,
    'rank' : fields.Integer
}

# class로 api 객체 생성
class TextAnanlysis(Resource):
    @marshal_with(resource_fields) # ==> 위 resource_fields 형식에 맞게 적용
    def get(self, text_id):
        result = Hjgrace.query.filter_by(h_id=text_id).first()
        
        # 만약 찾으려는 id 값이 없는 데이터라면
        if not result:
            abort(404, message='찾을 수 없는 id값입니다.')
        return result
    
    @marshal_with(resource_fields)
    def post(self, text_id):
        args = text_put_args.parse_args()
        
        # 이미 등록하려는 id가 있을 경우
        result = Hjgrace.query.filter_by(h_id=text_id).first()
        if result:
            abort(409, message='등록하려는 id 값이 이미 존재합니다.')
        
        text = Hjgrace(h_id=text_id, 
                       name=args['name'], 
                       q_1=args['q_1'],
                       q_2=args['q_2'],
                       q_3=args['q_3'],
                       q_4=args['q_4'],
                       q_5=args['q_5'],
                       label=args['label'],
                       cosine=args['cosine'],
                       rank=args['rank'])
        db.session.add(text)
        db.session.commit()
        return text, 201
    
    @marshal_with(resource_fields)
    def patch(self, text_id):
        args = text_update_args.parse_args()
        result = Hjgrace.query.filter_by(h_id=text_id).first()

        if not result:
            abort(404, message='등록하려는 id 값이 없기에 업데이트가 불가합니다.')

        if args['cosine'] :
            result.cosine = args['cosine']
        if args['rank'] :
            result.rank = args['rank']

        db.session.commit()

        return result

    
    @marshal_with(resource_fields)
    def put(self, text_id):
        args = text_put_args.parse_args()
        
        # 이미 등록하려는 id가 있을 경우
        result = Hjgrace.query.filter_by(h_id=text_id).first()
        if result:
            abort(409, message='등록하려는 id 값이 이미 존재합니다.')
        
        text = Hjgrace(h_id=text_id, 
                       name=args['name'], 
                       q_1=args['q_1'],
                       q_2=args['q_2'],
                       q_3=args['q_3'],
                       q_4=args['q_4'],
                       q_5=args['q_5'],
                       label=args['label'],
                       cosine=args['cosine'],
                       rank=args['rank'])
        db.session.add(text)
        db.session.commit()
        return text, 201
    '''
        
    def delete(self, text_id):
        abort_not_exist(text_id)
        del texts[text_id]
        return '', 204
    '''
        
api.add_resource(TextAnanlysis, '/text/<int:text_id>')

if __name__ == '__main__':
    app.run(debug=True)