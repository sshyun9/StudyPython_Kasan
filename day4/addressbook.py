'''
주소록 프로그램 v1.0
작성일 2022-05-26 09:14
작성자 빵빵
설명 주소록 프로그램 테스트
'''

# 주소록 클래스
from audioop import add


class Contact:
    name = ''; phone_number = ''; e_mail = ''; addr = ''

    # 생성자 (contructor)
    def __init__(self, name, phone_number, e_mail, addr) -> None:    # init 합수는 return 없음. 그래서 None, class 함수에만 (self) 존재
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def __str__(self) -> str:      # str 함수는 return 있음. 문자열로 return
        res_str = f'이  름 : {self.name}\n' \
                  f'폰번호 : {self.phone_number}\n' \
                  f'이메일 : {self.e_mail}\n'  \
                  f'주  소 : {self.addr}\n'
        return res_str

def run():  # 클래스X 일반함수 -> (self) 없음
    member = Contact('홍길동', '010-0000-1111', 'hgd76@namver.com', '서울특별시')
    print(member)

if __name__ =='__main__':          # EntryPoint (프로그램 시작점)
    print('\n프로그램 시작\n')   
    run() 


