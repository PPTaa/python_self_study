import tensorflow as tf
a = tf.constant(1) #상수
b = tf.constant(2)
c = tf.add(a,b)
sess = tf.Session()
sess.run(c)

print(c)
#변수 실습
a1=tf.Variable(5)
b2=tf.Variable(3)
c2=tf.multiply(a1,b2)
init = tf.global_variables_initializer()
sess.run(init)
sess.run(c2)
a1 = tf.Variable(15)
c2 = tf.multiply(a1,b2)
init = tf.global_variables_initializer()
sess.run(init)
sess.run(c2)

##7강 - 프레이스 홀더 실습1
input = [1,2,3,4,5]
x = tf.placeholder(dtype = tf.float32)
y = x + 5
sess = tf.Session()
sess.run(y, feed_dict={x:input})

##7강 - 프레이스 홀더 실습2
mathscore = [85,99,84,97,92]
engscore = [59,60,80,65,94]
a=tf.placeholder(dtype=tf.float32)
b=tf.placeholder(dtype=tf.float32)
y=(a+b)/2
sess.run(y, feed_dict={a:mathscore, b:engscore})

#8강 - 주요함수 실습하기
a=tf.constant(16)
b=tf.constant(14)

##덧셈함수 사용하기
c=tf.add(a,b)
sess.run(c)
##뺄셈함수 사용하기
c=tf.subtract(a,b)
sess.run(c)
##곱셈함수 사용하기
c=tf.multiply(a,b)
sess.run(c)
##나눗셈 함수 사용하기
c=tf.truediv(a,b)
sess.run(c)
##나눗셈의 나머지 함수 사용하기
c=tf.mod(a,b)
sess.run(c)
##절대값 함수 사용
c=tf.abs(-a)
sess.run(c)

#a,b변수 다시 초기화
a=tf.constant(17.5)
b=tf.constant(5.0)
##음수함수사용
c=tf.negative(a)
sess.run(c)
#부호함수 사용
c=tf.sign(a)
sess.run(c)
#제곱함수 사용
c=tf.square(a)
sess.run(c)
#거듭제곱 함수 사용
c=tf.pow(a,2)
sess.run(c)
#최댓값 함수
c=tf.maximum(a,b)
sess.run(c)
#최소값 함수
c=tf.minimum(a,b)
sess.run(c)
#지수값 계산 함수
c=tf.exp(b)
sess.run(c)
#로그값 계산 함수
c=tf.log(b)
sess.run(c)