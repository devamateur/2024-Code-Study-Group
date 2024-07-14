## **✏️ Chapter 7 : Binary Search**
"이것이 취업을 위한 코딩 테스트다 with Python" 7장 이진 탐색 내용을 정리하는 공간.  

### **7장 이진 탐색**

- 이론
    - 범위를 반씩 좁혀가는 탐색
    - 순차 탐색: ([Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/7/1.py) / [C++ 코드](https://github.com/ndb796/python-for-coding-test/blob/master/7/1.cpp) / [Java 코드](https://github.com/ndb796/python-for-coding-test/blob/master/7/1.java))
    - 재귀 함수를 이용한 이진 탐색: ([Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/7/2.py) / [C++ 코드](https://github.com/ndb796/python-for-coding-test/blob/master/7/2.cpp) / [Java 코드](https://github.com/ndb796/python-for-coding-test/blob/master/7/2.java))
    - 반복문을 이용한 이진 탐색: ([Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/7/3.py) / [C++ 코드](https://github.com/ndb796/python-for-coding-test/blob/master/7/3.cpp) / [Java 코드](https://github.com/ndb796/python-for-coding-test/blob/master/7/3.java))
    - 파이썬에서 빠르게 입력 받기: [Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/7/4.py)
- 실전
    - 부품 찾기
        - 이진 탐색으로 해결: ([Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/7/5.py) / [C++ 코드](https://github.com/ndb796/python-for-coding-test/blob/master/7/5.cpp) / [Java 코드](https://github.com/ndb796/python-for-coding-test/blob/master/7/5.java))
        - 계수 정렬로 해결: ([Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/7/6.py) / [C++ 코드](https://github.com/ndb796/python-for-coding-test/blob/master/7/6.cpp) / [Java 코드](https://github.com/ndb796/python-for-coding-test/blob/master/7/6.java))
        - 집합(Set) 자료형으로 해결: ([Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/7/7.py) / [C++ 코드](https://github.com/ndb796/python-for-coding-test/blob/master/7/7.cpp) / [Java 코드](https://github.com/ndb796/python-for-coding-test/blob/master/7/7.java))
    - 떡볶이 떡 만들기: ([Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/7/8.py) / [C++ 코드](https://github.com/ndb796/python-for-coding-test/blob/master/7/8.cpp) / [Java 코드](https://github.com/ndb796/python-for-coding-test/blob/master/7/8.java))


---


CHAPTER 07. 이진 탐색: 탐색 범위를 반으로 좁혀가며 빠르게 탐색하는 알고리즘




🥪 순차 탐색Sequential Search

- 가장 기본적인 탐색 방법. 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로(순차적으로) 확인하는 방법.
- 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 사용함.
- 리스트 내에 데이터가 아무리 많아도 시간만 충분하다면 항상 원하는 원소(데이터)를 찾을 수 있다는 장점이 있음.
- 아주 빈번하게 사용되는 방법. ex: 리스트에 특정 값의 원소가 있는지 체크할 때, 리스트 자료형에서 특정한 값을 가지는 원소의 개수를 세는 count() 메서드를 이용할 때


🎂 7-1.py 순차 탐색 소스코드

	# 순차 탐색 소스코드 구현
	def sequential_search(n, target, array):
		# 각 원소를 하나씩 확인하며
		for i in range(n):
			# 현재의 원소가 찾고자 하는 원소와 동일한 경우
			if array[i] == target:
				return i + 1 # 현재의 위치 반환(인덱스는 0부터 시작하므로 1 더하기)

	print("생성할 원소 개수를 입력한 다음 한 칸 띄우고 찾을 문자열을 입력하세요.")
	input_data = input().split()
	n = int(input_data[0]) # 원소의 개수
	target = input_data[1] # 찾고자 하는 문자열
	
	print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
	array = input().split()
	# 순차 탐색 수행 결과 출력
	print(sequentail_search(n, target, array))



	-> 생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.
	5 Dongbin
	-> 앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.
	Hanul Danik Solbi Mijeong Dongbin
	5

- 데이터 정렬 여부와 상관없이 가장 앞에 있는 원소부터 하나씩 확인하는 것이 특징.
- 시간 복잡도: O(N). (데이터의 개수가 N개일 때 최대 N번의 비교 연산이 필요하므로)




🥪 이진 탐색Binary Search

- 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘.
- 데이터가 무작위일 때는 사용할 수 없지만, 이미 정렬되어 있다면 매우 빠르게 데이터를 찾을 수 있다는 특징이 있음.
- 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 특징이 있음.

- 위치를 나타내는 변수 3개를 사용하여 탐색하고자 하는 범위의 '중간점, 시작점, 끝점'을 탐색함.
- 찾으려는 데이터와 중간점Middle 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 것.
- 절반씩 데이터를 줄어들도록 만든다는 점은 앞서 다룬 퀵 정렬과 공통점이 있음.
- 시간 복잡도: O(logN)
- 연산 횟수: log₂N에 비례한다. (한 단계를 거칠 때마다 확인하는 원소가 평균적으로 절반으로 줄어듬. = 단계마다 2로 나누는 것과 같음.)


🎂 7-2.py 재귀 함수로 구현한 이진 탐색 소스코드

	# 이진 탐색 소스코드 구현(재귀 함수)
	def binary_search(array, target, start, end):
	    if start > end:
	        return None
	    mid = (start + end) // 2
	    # 찾은 경우 중간점 인덱스 반환
	    if array[mid] == target:
	        return mid
	    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
	    elif array[mid] > target:
	        return binary_search(array, target, start, mid -1)
	    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
	    else:
	        return binary_search(array, target, start, mid + 1, end)

    # n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
    n, target = list(map(int, input().split))

    # 전체 원소 입력받기
    array = list(map(int, input(). split))

    # 이진 탐색 수행 결과 출력
    result = binary_search(array, target, 0, n, -1)
    if result == None:
            print("원소가 존재하지 않습니다.")
    else:
            print(result + 1)



		10 7
		1 3 5 7 9 11 13 15 17 19
		4

		10 7
		1 3 5 6 9 11 13 15 17 19
		원소가 존재하지 않습니다.


- mid = (start + end) // 2는 중간점을 의미함. 2로 나눈 몫만 구하기 위해 몫 연산자(//)를 사용한 것.
- 같은 기능이라고 하더라도 다양한 방법으로 구현이 가능함. (그리디의 '큰 수의 법칙'에서는 나눈 뒤에 몫을 구하기 위해 int() 함수를 사용함. 기능 면에서는 두 코드 모두 나눈 몫을 구하는 코드임.)


🎂 7-3.py 반복문으로 구현한 이진 탐색 소스코드

	# 이진 탐색 소스코드 (반복문)
	def binary_search(array, target, start, end):
		while start <= end:
			mid = (start + end) // 2
			# 찾은 경우 중간점 인덱스 반환
	if array[mid] == target:
	        return mid
	    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
	elif array[mid] > target:
	    end = mid -1
	    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
	else:
	    start = mid + 1
	    return None

	# n (원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
	n, target = list(map(int, input().split()))
	# 전체 원소 입력받기
	array = list(map(int, input().split()))

	# 이진 탐색 수행 결과 출력
	result = binary_search(array, target, 0, n - 1)
	if result == None:
	    print("원소가 존재하지 않습니다.")
	else:
	    print(result + 1)



🥪 코딩 테스트에서의 이진 탐색

- 참고할 소스코드가 없는 상황에서 이진 탐색 소스코드를 구현하는 것은 상당히 어려운 작업임.
- 이진 탐색은 코테에서 단골로 나오는 문제이기 때문에 가급적 외워야 함.
- 원리는 다른 알고리즘에서도 폭넓게 적용되는 원리와 유사하기 때문에 매우 중요함. 높은 난이도의 문제에서는 다른 알고리즘과 함께 사용되기도.
- 코테에서는 탐색 범위가 큰 상황에서의 탐색으 가정하는 문제가 많음. 처리해야 할 데이터의 개수나 값이 1,000만 단위 이상으로 넘어가면 이진 탐색과 같이 O(logN)의 속도를 내야 하는 알고리즘을 사용해야 함.




🎄 트리 자료구조

- 이진 탐색의 전제 조건: 데이터 정렬.
- 데이터베이스(DB): 내부적으로 대용량 데이터 처리에 적합한 트리Tree 구조를 이용하여 항상 데이터가 정렬되어 있음. 따라서 DB에서의 탐색은 이진 탐색과 유사한 방법을 사용해 탐색을 항상 빠르게 수행하도록 설계되어 있음.
- 노드Node: 정보의 단위로서 어떠한 정보를 가지고 있는 개체. 최단 경로에서는 '도시'와 같은 정점의 의미를 가짐.

- 트리는 부모 노드와 자식 노드의 관계로 표현된다.
- 트리의 최상단 노드를 '루트root 노드', 최하단 노드를 '단말element 노드'라고 한다.
- 트리에서 일부를 떼어내도 트리 구조이며, 이를 서브 트리라 한다.
- 트리는 파일 시스템과 같이 계층적이고 정렬된 데이터를 다루기에 적합하다.




🥪🎄 이진 탐색 트리

- 이진 탐색 트리: 트리 자료구조 중에서 가장 간단한 형태. 이진 탐색이 동작할 수 있도록 고안된, 효율적인 탐색이 가능한 자료구조.

- 부모 노드보다 왼쪽 자식 노드가 작다.
- 부모 노드보다 오른쪽 자식 노드가 크다.
	= 왼쪽 자식child 노드 < 부모parent 노드 < 오른쪽 자식child 노드
+ 특정 계층을 포함한 상단의 모든 노드를 조상ancesotr 노드, 하단의 모든 노드를 자손descendant 노드라고 한다.

- 이진 탐색 트리에 데이터를 넣고 빼는 방법은 알고리즘보다는 자료 구조에 가까움
- 이진 탐색 트리를 구현하는 문제는 출제 빈도가 낮은 편

이진 탐색 트리에서 데이터를 조회하는 과정

(1) 루트 노드를 방문하여 찾는 값에 따라 왼쪽(작은 값)/오른쪽(큰 값)으로 이동
(2) 단말 노드의 값을 확인 후 찾는 값에 따라 왼쪽(작은 값)/오른쪽(큰 값)으로 이동
(3) 현재 방문한 노드의 값과 동일한 원소값을 찾음. SEARCH END

- 위의 과정을 반복함.
- 만약 자식 노드가 없을 때까지 원소를 찾지 못했다면, 이진 탐색 트리에 찾는 값(원소)이 없는 것.






🎂 빠르게 입력받기

- 이진 탐색 문제는 입력 데이터가 많거나 탐색 범위가 매우 넓은 편임. (ex: 데이터의 개수가 1,000만 개를 넘어가거나 탐색 범위의 크기가 1,000억 이상인 경우)
- 그런데 이 경우 input() 함수를 사용하면 동작 속도가 느려 시간 초과로 오답 판정을 받을 수 있음.
- 입력 데이터가 많은 문제는 sys 라이브러리의 readline() 함수를 이용하면 시간 초과를 피할 수 있음.

7-4.py 한 줄 입력받아 출력하는 소스코드

import sys
# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()

#입력받은 문자열 그대로 출력
print(input_data)

-> Hello, NC friends!
Hello, NC friends!

- sys 라이브러리를 사용할 때는 한 줄 입력 -> rstrip() 함수를 꼭 호출해야 함. (!)
- 소스코드에 readling()으로 입력하면 입력 후 엔터가 줄 바꿈 기호/n으로 입력되는데, 이 공백 문자를 제거하려면 rstrip() 함수를 사용해야 함. (💚외우기)
- realind() 함수를 더 간결하게 사용하는 팁은 부록에서 추가로 다루고 있음. (444~448p)