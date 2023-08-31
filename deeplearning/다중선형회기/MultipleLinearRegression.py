import numpy as np
import matplotlib.pyplot as plt

# 넘파이 배열 생성
x1 = np.array([2,4,6,8]) # 공부한 시간
x2 = np.array([0,4,2,3]) # 과외 시간
y = np.array([81,93,91,97]) # 성적

# 데이터의 분포를 그래프로 나타내기
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(x1,x2, y);
plt.show

# 값 초기화
a1 = 0   # 기울기
a2 = 0   # 기울기
b = 0   # 절편

# 학습률 설정
lr = 0.01

#반복 횟수 설정
epochs = 2001

# x 값이 총 몇개인지 세기
n = len(x1)     # 변수의 총 개수

# 경사하강법
for i in range(epochs):
    y_pred = a1 * x1 + a2 * x2 + b  # 예측 값을 구하는 식
    error = y - y_pred  # 실제 값과 비교한 오차를 error 로 세팅

    a1_diff = (2/n) * sum(-x1 * (error))  # 오차 함수를 a1로 편미분
    a2_diff = (2/n) * sum(-x2 * (error))  # 오차 함수를 a2로 편미분
    b_diff = (2/n) * sum(-(error))      # 오차 함수를 b로 편미분

    a1 = a1 - lr * a1_diff     # 학습률을 곱해서 기존 a1값 업데이트
    a2 = a2 - lr * a2_diff     # 학습률을 곱해서 기존 a2값 업데이트
    b = b - lr * b_diff     # 학습률을 곱해서 기존 b값 업데이트

    if i % 100 == 0:        # 100번마다 현재 값 출력
        print("epoch=%.f, 기울기1=%.04f, 기울기2=%.04f, 절편=%.04f" %(i, a1, a2, b))

# 실제 점수와 예측된 점수 출력
print("실제 점수: ", y)
print("예측 점수: ", y_pred)
