a, b, c = (1, 2, 3)
# 주석처리, 여러 개의 변수를 한 번에 처리하려면 튜플 형태로.
"""
이러면 여러 줄 한 번에 주석 처리가 가능
"""
'''
하지만 이 외에도 문자열을 선언할 때 따옴표를 사용함
\n 파이썬도 줄 바꿈은 n으로 처리
'''
#string = "Life is too short You need Python"
string = '''
Life is too shrot
You need Python
'''
#줄 바꿈을 따옴표를 이용해서 처리하는 것도 가능하다
string2 = "good afternoon"

#print(string + string2) 
# +를 이용해서 concatenation이 가능, 
# * 연산자를 이용하면 문자열이 두 배가 된다
# len을 이용하면 string size 구할 수 있음

string3 = "I eat %d apples." % 3
print(string3) 
# % 3이 아닌 % "five" 를 넣어도 five가 출력된다.
# C언어처럼 변수 형태에 따라 s, d, f, o, x를 구분해서 넣어주자
# 하지만 %s 는 모든 변수를 string 형태로 
# 바꿔버리기 때문에 출력 자체에는 문제가 생기지 않음

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[-1][-1])
#-1은 마지막 인덱스를 의미함
a.insert(0, [4, 2])
print(a)