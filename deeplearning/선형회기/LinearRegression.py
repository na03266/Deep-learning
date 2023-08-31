import numpy as np
import matplotlib.pyplot as plt

# 넘파이 배열 생성
x = np.array([2,4,6,8]) #공부한 시간
y = np.array([81,93,91,97]) # 성적

# 데이터의 분포를 그래프로 나타내기
plt.scatter(x,y)
plt.show

# 값 초기화
a = 0   # 기울기
b = 0   # 절편

# 학습률 설정
lr = 0.01

#반복 횟수 설정
epochs = 2001

# x 값이 총 몇개인지 세기
n = len(x)

# 경사하강법
for i in range(epochs):
    y_pred = a * x + b  # 예측 값을 구하는 식
    error = y - y_pred  # 실제 값과 비교한 오차를 error 로 세팅

    a_diff = (2/n) * sum(-x * (error))  # 오차 함수를 a로 편미분
    b_diff = (2/n) * sum(-(error))      # 오차 함수를 b로 편미분

    a = a - lr * a_diff     # 학습률을 곱해서 기존 a값 업데이트
    b = b - lr * b_diff     # 학습률을 곱해서 기존 b값 업데이트

    if i % 100 == 0:        # 100번마다 현재 값 출력
        print("epoch=%.f, 기울기=%.04f, 절편=%.04f" %(i,a,b))

# 최종 a 값과 b 값을 각각 대입해 그래프 생성
y_pred = a * x + b

# 그래프를 출력합니다.
plt.scatter(x, y)
plt.plot(x, y_pred, 'r')
plt.show() 