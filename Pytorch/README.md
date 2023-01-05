### pytorch 배경

-   페이스북에서 `루아` 언어라는 언어로 개발한 torch 프레임 워크를 `python`으로 다시 개발해서 `pytorch`로 개발
-   초기에는 `numpy`와 같이 데이터 분석 프레임워크와 같은 느낌으로 기능 제공
-   추후 GPU를 사용해서 딥러닝 병렬처리가 가능하게끔 발전

### pytorch 구조

-   low-level : 하위 부분은 하드웨어 입장에서 GPU 접근 등 처리 계산을 빠르게 하기 위한 구조로 개발돼 있음, `C, CUDA`와 같은 저수준 언어 사용
-   middle-level : `C++` 활용하여 중간 레벨의 언어로 개발. 엔진 역할을 담당
-   top-level : `Python` 모듈 구조로 wrapping돼 있는 API 제공

### pytorch 구성 요소

-   `torch` : 텐서와 같은 수학 함수 기능 포함
-   `torch.autograd` : 자동 미분 기능 제공하는 라이브러리
-   `torch.nn` : 딥러닝 Neural Network 신경망 구성을 위한 라이브러리
-   `torch.multiprosessing` : 병렬처리 계산 기능 제공
-   `torch.optim` : 신경망 파라미터 최적화 알고리즘 제공
-   `torch.utils` : 데이터 조작 기능 제공
-   `torch.onnx` : **ONNX**(Open Neural Network Exchange) -> pytorch로 구현한 딥러닝 모델을 다른 프레임워크 형태의 모델로 공유할 수 있도록 도와주는 라이브러리

### Tensor

-   데이터 표현하는 하나의 구조로서 다차원 데이터를 효율적으로 표현 가능
-   수치형 데이터를 담는 컨테이너 구조로 이뤄져 있음
-   GPU 사용해서 tensor 계사할 때 연산 가속 기능 제공
-   `scalar` : 0D, 차원이 없는
-   `vector` : 1D, 1차원
-   `matrix` : 2D, 2차원
-   그 외 다차원 tensor 확장 가능

#### 참고 url : https://youtu.be/k60oT_8lyFw