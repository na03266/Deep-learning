import numpy as np
import matplotlib.pyplot as plt

# 텐서플로의 케ㅔ라스 API에서 필요한 함수 호출
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

x = np.array([2,4,6,8])
y = np.array([81,93,91,97])

model = Sequential()

# 출력 값, 입력변수, 분석 방법에 맞게끔 모델 설정
model.add(Dense(1, input_dim=1, activation='linear'))

# 오차 수정을 위해 경사 하강법(sgd), 오차의 정도 판단을 위해 평균제곱오차 사용
model.compile(optimizer='sgd', loss='mse')

#오차를 최소화하는 과정 2000번 반복
model.fit(x,y,epochs=2000)

plt.scatter(x,y)
plt.plot(x, model.predict(x), 'r')
plt.show()

#임의의 시간을 집어넣어 점수를 예측하는 모델 테스트
hour = 7
prediction = model.predict([hour])
print("%.f시간을 공부할 경우 예상 점수는 %.02f점입니다." % (hour, prediction))
