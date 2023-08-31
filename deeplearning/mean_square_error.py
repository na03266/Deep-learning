import numpy as np

# 가상의 기울기, 절편 결정
fake_a = 3
fake_b = 76

# 시간x 와 성적 y의 넘파이 배열 생성
x = np.array([2,4,6,8])
y = np.array([81,93,91,97])

# y = ax +b에 가상 값을 대입한 결과를 출력하는 함수
def predict(x):
    return fake_a * x + fake_b

# 예측 값이 들어갈 빈 리스트를 만듦
predict_result = []

# 모든 x 값을 한번씩 대입해 predict_result 리스트 완성
for i in range(len(x)):
    predict_result.append(predict(x[i]))
    print("공부한 시간 = %.f, 실제 점수 = %.f, 예측 점수 = %.f" 
          % (x[i], y[i], predict(x[i])))
    
# 평균 제곱 오차 함수를 각 y 값에 대입해 최종 값을 구하기
n = len(x)

def mse(y, y_pred):
    return (1/n) * sum((y-y_pred)**2)

# 평균 제곱 오차 값을 출력
print("평균 제곱 오차 : " + str(mse(y, predict_result)))