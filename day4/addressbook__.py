'''
주소록 프로그램 v1.01
작성일 2022-05-26 10:00
작성자 빵빵
설명 주소록 프로그램 테스트
'''
from operator import truediv
import os   # 운영체제 명령용 모듈

# 주소록 클래스
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
                  f'주  소 : {self.addr}\n' \
                      '=============================='
        return res_str
    
    def isNameExist(self, name) -> bool:
        if (self.name == name):
            return True
        else:
            return False

# 화면 클리어 함수
def clearConsole():
    command = 'clear'   # UNIX, LINUX, MACOS
    if os.name in ('nt','dos'):   #Windows
        command = 'cls'
    
    os.system(command)

# 사용자 정보 입력
def getContact():
    memeber = None  # 로컬변수 초기화
    try:
        (name, phone_number, e_mail, addr) = \
            input('정보입력(이름, 폰번호, 이메일, 주소)[구분자:/]\n >').split('/')
        member = Contact(name, phone_number, e_mail, addr)
    except Exception as ex:
        # print(f'예외발생 : {ex}')
        print('정확하게 이름/전화번호/이메일/주소 순으로 입력해주세요.')
    # print(name, phone_number, e_mail, addr)
    return member

# 연락처 리스트 출력
def printContacts(contacts):
    for item in contacts:  # 리스트 원소(Contact 객체)
        print (item)

# 연락처 삭제 함수
def delContact(contacts, name):
    for i, item in enumerate(contacts):
        if item.isNameExist(name) == True:
            del contacts[i]

# 메뉴출력
def getMenu():
    str_menu = ('\n주소록 프로그램 v1.0\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 프로그램 종료\n')
    print(str_menu)
    menu = input('메뉴선택 > ')
    try :                      # 예외처리: 1-4까지 숫자 제외 다른게 나오면 0으로 바뀜
        menu = int(menu)
    except:
        menu = 0
    return int(menu)

# 기본 실행 함수
def run():  # 클래스X 일반함수 -> (self) 없음
    contacts = []   # 빈 리스트 변수 초기화
    clearConsole()

    while True:
        sel_menu = getMenu()
        if sel_menu == 1:  # 연락처 추가
            clearConsole()
            member = getContact()
            if (member != None):
                contacts.append(member)   # 연락처리스트에 새로운 연락처 추가

            input('계속하려면 아무키나 누르세요.')
            clearConsole()
        elif sel_menu ==2:     # 연락처 출력
            clearConsole()
            print(f'총 {len(contacts)}건입니다.')
            print('--------------------')
            printContacts(contacts)
            input('계속하려면 아무키나 누르세요.')
            clearConsole()
        elif sel_menu ==3:     # 연락처 삭제
            clearConsole()
            name = input('삭제할 이름 입력 >')
            delContact(contacts, name)
            input('계속하려면 아무키나 누르세요.')
            clearConsole()
        elif sel_menu == 4:   #프로그램 종료
            break
        else:
            clearConsole()

if __name__ =='__main__':          # EntryPoint (프로그램 시작점)
    print('\n프로그램 시작\n')   
    try:
        run() 
    except KeyboardInterrupt as ex:
        print('비정상 종료!')