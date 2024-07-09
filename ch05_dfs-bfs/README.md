## **✏️ Chapter 5 : DFS/BFS**
"이것이 취업을 위한 코딩 테스트다 with Python" 5장 DFS/BFS 내용을 정리하는 공간.  

### **5장 DFS/BFS**

- 이론
    - 꼭 필요한 자료구조 기초
    - 탐색 알고리즘 DFS/BFS
    - 스택 구현 예제: ([Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/1.py) / [C++ 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/1.cpp) / [Java 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/1.java))
    - 큐 구현 예제: ([Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/2.py) / [C++ 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/2.cpp) / [Java 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/2.java))
    - 무한히 반복되는 재귀함수 예제: ([Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/3.py) / [C++ 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/3.cpp) / [Java 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/3.java))
    - 재귀함수의 종료 조건 예제: ([Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/4.py) / [C++ 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/4.cpp) / [Java 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/4.java))
    - 2가지 방식으로 구현한 팩토리얼 예제: ([Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/5.py) / [C++ 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/5.cpp) / [Java 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/5.java))
    - 인접 행렬 예제: ([Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/6.py) / [C++ 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/6.cpp) / [Java 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/6.java))
    - 인접 리스트 예제: ([Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/7.py) / [C++ 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/7.cpp) / [Java 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/7.java))
    - DFS: ([Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/8.py) / [C++ 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/8.cpp) / [Java 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/8.java))
    - BFS: ([Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/9.py) / [C++ 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/9.cpp) / [Java 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/9.java))
- 실전
    - 음료수 얼려 먹기: ([Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/10.py) / [C++ 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/10.cpp) / [Java 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/10.java))
    - 미로 탈출: ([Python 3.7 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/11.py) / [C++ 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/11.cpp) / [Java 코드](https://github.com/ndb796/python-for-coding-test/blob/master/5/11.java))


-------------------------------------------------

1. 꼭 필요한 자료구조 기초

🌍탐색(Search)
 탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 의미함.
 프로그래밍에서는 그래프, 트리 등의 자료구조 안에서 탐색을 하는 문제를 자주 다룸. 
 대표적인 탐색 알고리즘: DFS(깊이 우선 탐색)과 BFS(너비 우선 탐색).이를 제대로 이해하기 위해서는 기본 자료구조인 스택, 큐, 재귀 함수에 대한 이해가 필요함.


🌍자료구조 (Data Structure)
  자료구조는 '데이터를 표현/관리/처리하기 위한 구조'를 의미함.
  그 중 스택과 큐는 자료구조의 기초 개념으로 다음의 두 핵심적인 함수로 구성됨:
    - 삽입(Push): 데이터를 삽입함.
    - 삭제(Pop): 데이터를 삭제함.

 실제로 스택, 큐를 이용할 때에는 오버플로(Overflow)와 언더플로(Underflow)를 고민해야 함.
  - Overflow: 데이터의 크기가 이미 가득 찬 상태에서 삽입 연산을 수행할 때 발생함.
  - Underflow: 데이터가 전혀 들어있지 않은 상태에서 삭제 연산을 수행할 때 발생함.


🏒 스택 (Stack)
    스택은 선입후출(FILO) or 후입선출(LIFO) 구조. (ex: 박스 쌓기)

    파이썬에서 스택을 사용할 때는 따로 라이브러리를 사용할 필요가 없음.
    기본 리스트에서 apend()와 pop() 메서드를 이용하면 스택 자료구조와 동일하게 동작함.:
        append() 메서드: 리스트의 가장 뒤쪽에 데이터를 삽입함. 
        pop() 메서드: 리스트의 가장 뒤쪽에서 데이터를 꺼냄.


🏒 큐 (Queue)
   큐는 선입선출(FIFO) 구조. (ex: 대기줄)

   파이썬에서 큐를 구현할 때는 collections 모듈에서 제공하는 deque 자료구조를 활용해야.
   deque는 스택, 큐의 장점을 모두 채택한 것임.
   데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적, queue 라이브러리를 이용하는 것보다 더 간단함.

🏒 재귀 함수 (Recursive Function)
    재귀 함수는 '자기 자신을 다시 호출하는 함수'를 의미.
    
    * 간단한 재귀 함수

    def recursive_function():
        print("재귀 함수를 호출합니다.")
        recursive_function()
    recursive_function()

    -> 위 코드를 실행하면 '재귀 함수를 호출합니다.' 라는 문자열을 무한히 출력함. 여기서 정의한 recursive_function()이 자기 자신을 계속해서 추가로 불러오기 때문. 물론 어느정도 출력하면 오류 메시지를 출력하고 멈출 것임.


📍 재귀 함수의 종료 조건
 재귀 함수는 종료 조건을 꼭 명시하지 않을 경우, 함수가 무한히 호출될 수 있기 때문에 재귀 함수가 언제 끝날지 종료 조건을 꼭 명시해야 함.


  * 재귀 함수를 100번 호출하는 코드

    def recursive_function(i):
        if i == 100:
            return
        print(i, '번째 재귀 함수에서', i+1 '번째 재귀 함수를 호출합니다.)
        recursive_function(i+1)
        print(i, '번째 재귀 함수를 종료합니다.)

    recursive_function(1)

재귀 함수는 내부적으로 스택 자료구조와 동일하기 때문에, 스택 자료구조를 활용해야 할 때 재귀 함수를 이용하여 구현될 수 있음. DFS(깊이 우선 탐색)이 대표적인 예임.

재귀 함수를 이용하는 대표적 예로 팩토리얼(Factorial) 문제가 있음. 반복적으로 구현한 n!과 재귀적으로 구현한 n!은 결과는 똑같지만, 재귀 함수를 사용했을 때 코드가 더 간결함. 그 이유는 수학의 점화식(재귀식)을 그대로 코드에 옮겼기 때문.


- 팩토리얼을 수학적 점화식으로 표현했을 때

    n이 0 혹은 1일 때: factorial(n) = 1
    n이 1보다 클 때: factoria(n) = n x factorial(n-1)

점화식에서 종료 조건을 찾을 수 있는데, 위 예시에서 종료 조건은 'n이 0 혹은 1일 때'임.
팩토리얼은 n이 양의 정수일 때만 유효하기 때문에 n이 1 이하인 경우 1을 반환할 수 있게 재귀함수를 작성해야 함. (n이 1 이하인 경우를 고려하지 않으면 재귀 함수가 무한히 반복되어 결과 출력이 불가능)

또한 n의 값으로 음수가 들어왔을 때는 입력 범위 오류로, 오류 메세지를 띄우도록 코드를 작성할 수도 있음.

따라서 재귀 함수 내에서 특정 조건일 때 더이상 재귀적으로 함수를 호출하지 않고 종료하도록 if문을 이용하여 꼭 종료 조건을 구현해주어야 함.