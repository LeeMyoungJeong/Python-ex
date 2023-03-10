# 세트
# : 집합의 개념
#   중복 없이 순서가 없는 여러 개의 데이터를 저장하는 컬렉션
#    - 중복된 값을 제거하거나, 교집합, 합집합 등의 개념이 필요한 경우 사용
#    - 기호 : {  }
#    - s = { 값1, 값2, ... }

s1 = {1,2,3,4,5}
print('s1 : ', s1 )


# 세트는 순서가 없어서, 인덱싱을 할 수 없다.

# 세트의 요소 추가 및 삭제
# 요소 추가 : add()
# 요소 삭제 : remove(), discard()

s1.add(6)
print(s1)

s1.add(7)
print(s1)

s1.add(8)
print(s1)

# 중복된 값을 추가하지 않는다.
print()
s1.add(5)
s1.add(5)
print(s1)
print()

# 세트에서는 값을 찾아서 삭제한다. (8번째 인덱스를 찾아 삭제가 아니라 8이라는 값을 삭제)
s1.remove(8)
print(s1)

s1.discard(7)
print(s1)

# remove 와 discard 함수의 차이
# s1.remove(10)
# remove 함수는 없는 값을 삭제할 때 에러 발생
# discard 함수는 없는 값을 삭제해도 에러발생 안 함

s1.discard(10)
print(s1)
