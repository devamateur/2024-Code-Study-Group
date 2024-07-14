## **✏️ Chapter 6 : Sorting**
"이것이 취업을 위한 코딩 테스트다 with Python" 6장 정렬 내용을 정리하는 공간.  

### **6장 정렬**

- 이론
    - 기준에 따라서 데이터를 정렬
    - 선택 정렬: ([Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/1.py) / [C++ 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/1.cpp) / [Java 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/1.java))
    - 스와프(Swap): ([Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/2.py) / [C++ 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/2.cpp) / [Java 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/2.java))
    - 삽입 정렬: ([Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/3.py) / [C++ 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/3.cpp) / [Java 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/3.java))
    - 퀵 정렬: ([Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/4.py) / [C++ 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/4.cpp) / [Java 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/4.java))
    - 파이썬의 장점을 살린 퀵 정렬: [Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/5.py)
    - 계수 정렬: ([Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/6.py) / [C++ 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/6.cpp) / [Java 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/6.java))
    - 정렬 라이브러리 기본 예제: ([Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/7.py) / [C++ 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/7.cpp) / [Java 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/7.java))
    - 정렬 라이브러리 키(Key) 기준 정렬 예제: ([Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/9.py) / [C++ 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/9.cpp) / [Java 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/9.java))
- 실전
    - 위에서 아래로: ([Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/10.py) / [C++ 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/10.cpp) / [Java 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/10.java))
    - 성적이 낮은 순서대로 학생 출력하기: ([Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/11.py) / [C++ 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/11.cpp) / [Java 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/11.java))
    - 두 배열의 원소 교체: ([Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/12.py) / [C++ 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/12.cpp) / [Java 코드](https://github.com/ndb796/python-for-coding-test/blob/master/6/12.java))




    ---------


CHAPTER 06: 정렬. 연속된 데이터를 기준에 따라서 정렬하기 위한 알고리즘

🌍 기준에 따라 데이터를 정렬

- 정렬 알고리즘 개요
 정렬Sorting: 데이터를 특정한 기준에 따라서 순서대로 나열하는 것. 프로그램에서 데이터를 가공할 때 오름차순/내림차순 등 정렬해서 사용하는 경우가 많음. 정렬 알고리즘 = 가장 많이 사용되는 알고리즘 중 하나, 이진 탐색의 전처리 과정.

 			정렬 알고리즘을 사용하면 이진 탐색Binary Search이 가능해짐.

 정렬 알고리즘의 종류: 아주 다양함. 이 책에서는 선택 정렬, 삽입 정렬, 퀵 정렬, 계수 정렬에 대해 다룰 예정.
 					+ 파이썬에서 제공하는 기본 정렬 라이브러리를 적용하여 좀 더 효과적인 정렬 수행 방법도 다룰 예정.


 🧭 이 책에서 다루는 예제는 모두 오름차순 정렬을 수행한다고 가정함. 내림차순 정렬은 오름차순 정렬을 수행하는 알고리즘에서 크기 비교를 반대로 수행하면 됨. 리스트를 뒤집는 연산은 O(N)의 복잡도로 간단히 수행할 수 있으므로 이 책에서는 오름차순을 위한 소스코드만 다루기로 함.


🐲 선택 정렬

	선택 정렬 알고리즘Selection Sort: 무작위의 데이터가 여러 개 있을 때, 이 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복하는 것. = 가장 원시적인 방법, 매번 가장 작은 것을 선택함.

🧭 정렬 알고리즘은 흔히 데이터의 개수를 N이라고 표현함.

	N = 10이라고 가정했을 때, 선택 정렬을 하게 되면 가장 작은 데이터를 앞으로 보내는 과정은 N-1번 반복하면 정렬이 완료된다. (🧭책 158-159p 그림 참조)


	//
		array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

		for i in range(len(array)):
			min_index = i # 가장 작은 원소의 인덱스
			for j in range(i + 1, len(array)):
				if array[min_index] > array[j]:
					min_index = j
			array[i], array[min_index] = array[min_index], array[i] # 스와프

		print(array)

		= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

	//

🧭 스와프Swap: 특정한 리스트가 주어졌을 때 두 변수의 위치를 변경하는 작업을 의미함. 다른 프로그래밍 언어에서는 명시적으로 임시 저장용 변수를 만들어 두 원소의 값을 변경해야 한다.

	💚 선택 정렬의 시간 복잡도: O(N²). 소스코드 상으로 간단한 형태의 2중 반복문이 사용되었기 때문. 다른 알고리즘과 비교했을 때 매우 비효율적이지만, 특정한 리스트에서 가장 작은 데이터를 찾아야 할 때 사용할 일이 잦음.



🐲 삽입 정렬

	삽입 정렬 알고리즘Insertion Sort: 데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입하는 방법. 삽입 정렬은 필요할 때만 위치를 바꾼다. 또, 특정한 데이터가 적절한 위치에 들어가기 이전에 그 앞까지의 데이터는 이미 정렬되어 있다고 가정함.

	//
	array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

	for i in range(1, len(array)):
		for j in range (i, 0, -1): # 인덱스 i부터 1까지 감소하며 반복하는 문법
			if array[j] < array[j - 1]: #한 칸씩 왼쪽으로 이동
				array[j], array[j - 1] = array[j - 1], array[j]
			else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
				braek

	print(array)
	//

🧭 range의 매개 변수는 3개(start, end, step)이다. 세 번째 매개 변수인 step에 -1이 들어가면 start 인덱스부터 시작해서 end + 1 인덱스까지 1씩 감소한다. 앞의 코드에서는 j 변수가 i부터 1까지 1씩 감소한다.

	💚 삽입 정렬의 시간 복잡도: O(N²). 반복문이 중첩되어 사용됨. 그러나 리스트의 데이터가 거의 정렬되어 있는 상태라면, O(N)의 시간 복잡도를 가짐. 거의 정렬이 되어 있는 상태로 입력이 주어지는 문제라면 퀵 정렬보다 삽입 정렬을 이용하는 것이 정답 확률을 높일 수 있음.



🐲 퀵 정렬

	'병합 정렬' 알고리즘과 함께 가장 많이 사용되는 정렬 알고리즘. 기준을 설정함 -> 큰 수-작은 수를 교환 -> 리스트를 반으로 나누는 방식으로 동작함. 퀵 정렬을 수행하기 전에는 피벗을 어떻게 설정할 것인지 미리 명시해야 함.

	정리하자면, 퀵 정렬은 특정 리스트에서 pivot을 설정하여 정렬을 수행한 이후에, pivot을 기준으로 왼쪽, 오른쪽 리스트에서 각각 다시 정렬을 수행한다. '재귀 함수'와 동작 원리가 같다. (🧭5장 참조) 즉 종료 조건이 있어야 한다는 것임.
	퀵 정렬이 끝나는 조건: 현재 리스트의 데이터 개수가 1개인 경우.


	피벗Pivot: 큰 숫자와 작은 숫자를 교환할 때, 교환하기 위한 '기준'
	호어 분할Hoare Partition: 가장 대표적인 분할 방식. 리스트에서 첫 번째 데이터를 피벗으로 정함 -> 왼쪽에서 피벗보다 큰 데이터를 찾고, 오른쪽에서 피벗보다 작은 데이터를 찾음 -> 큰 데이터와 작은 데이터의 위치를 서로 교환해 줌 -> for(반복이라는 뜻) -> '피벗'에 대한 정렬이 수행됨.
	분할 = Divide (or) Partition

* 가장 직관적인 형태의 퀵 소스코드
	//
	array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

	def quick_sort(array, start, end):
		if start >= end: # 원소가 1개인 경우 종료
			return
		pivot = start #피벗은 첫 번째 원소
		left = start + 1
		right = end
		while left <= right:
			# 피벗보다 큰 데이터를 찾을 때까지 반복
			while left <= end and array[right] >= array[pivot]:
				left += 1
			# 피벗보다 작은 데이터를 찾을 때까지 반복
			while right > start and array[right] >= array[pivot]:
				right -= 1
			if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
				array[right], array[pivot] = array[right], array[left]
			else: #엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
				array[left], array[right] = array[right], array[left]
		# 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
		quick_sort(array, start, right -1)
		quick_sort(array, right + 1, end)

	quick_sort(array, 0, len(array) - 1)
	print(array)
	//

= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


* 파이썬의 장점을 살린 퀵 소스코드

	//
	array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

	def quick_sort(array):
		# 리스트가 하나 이하의 원소만을 담고 있다면 종료
		if len(array) <= 1:
			return array

		pivot = array[0] #피벗은 첫 번째 원소
		tail = array[1:] # 피벗을 제외한 리스트

		left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
		right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

		# 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
		return quick_sort(left_side)

	print(quick_sort(array))
	//


= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

	💚 퀵 정렬의 시간복잡도: 평균 O(NlogN). 최악의 경우는 O(N²)으로 작동함. #문제는 솔비가 로그를 모름! >_<
	삽입 정렬과 대조되게, 퀵 정렬은 이미 데이터가 정렬되어 있는 경우는 매우 느리게 작동함.



🐲 계수 정렬

	계수 정렬(Count Sort): 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘.