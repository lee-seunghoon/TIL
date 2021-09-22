# msg='별일 없죠?'
# => 매개변수에 설정된 값을 디폴트 값(기본값)이라고 함
# => 디폴트 값을 가진 변수를 디폴트 매개변수라고함
# => 디폴트 매개변수에 전달된 값이 없으면, 디폴트 값이 저장된다. 

def greet(name, msg='별일 없죠?') :
    print(name +', '+msg)
    

greet('Sherlock', 'Good morning')

greet('승훈')

greet(msg='KIN',name='zico') #유연하게 순서 바꿔서 변수에 내용 입력해줘도 된다.

