from time import sleep

from django.core.cache import cache


def x():
    key = f'lock user'
    retry = 10
    for i in range(retry):
        lock = cache.get(key)

        # 락 없음
        if not lock:
            # 락걸기
            cache.set(key, True, 3)
            print('logic 실행중', end='')

            # 비즈니스 로직
            for j in range(5):
                # 터치
                cache.touch(key, 2)
                print('.', end='')
                sleep(1)
            print()

            print('logic 완료! >ㅅ<')
            cache.delete(key)
            break

        # 락 있음
        else:
            # wait 후 재시도
            print('wait 후 재시도')
            sleep(1)
    else:
        print('락 획득 실패')
