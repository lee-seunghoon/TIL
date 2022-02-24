class Article :
    def __init__(self) :
        self.num = 0 #글번호
        self.title = 0 # 제목
    
class FileArticle(Article):
    def __init__(self):
        self.fileName = 0
        
    def __str__(self):
        return '자료실 [번호=%s, 제목=%s, 첨부파일=%s]' \
            %(self.num, self.title, self.fileName)
            
class QNAArticle(Article):
    def __init__(self):
        self.answer = 0
        
    def __str__(self):
        return '질문/답변 [번호=%s, 제목=%s, 답변=%s]' \
            %(self.num, self.title, self.answer)
            
# 파일
fileArticle = FileArticle()
fileArticle.num = 1
fileArticle.title = '첫 번째 자료입니다.'
fileArticle.fileName = 'python.ppt'

print(fileArticle)
print()

# 질문/답변
qna = QNAArticle()
qna.num = 2
qna.title = '두 번째 질문입니다.'
qna.answer = '두 번째 답변입니다.'
print(qna)

