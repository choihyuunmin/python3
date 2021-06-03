# yield : 메인루틴 <-> 서브루틴 통신
# 서브루틴 : 메인루틴에서 리턴에 의해 호출 부분으로 돌아와 다시 프로세스
# 코루틴 : 루틴 실행 중 멈춤 가능 -> 특정 위치로 돌아갔다가 다시 원래 위치로 돌아와 수행 가능 ==> 동시성 프로그래밍 가능

def coroutine1():
    print('>>> coroutine started')
    i = yield
    print('>>> coroutine received : {}'.format(i))
    
    
# declare generator
c1 = coroutine1()

print(c1, type(c1))

next(c1)
# next(c1)


c1.send(100)