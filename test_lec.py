print('===================')
print('회원가입')
print('===================')

register = False #회원가입 진행 한다/안한다

while not register:     #true가 되겠금
    print('회원가입을 진행하시겠습니까?\n y:진행     n:취소')
    register_input = input('>> ')
    register_input = register_input.lower()  #소문자만 input
    
    if register_input == 'y':
        register = True
        print('===================')
        print('회원가입 진행')
        print('===================')
    elif register_input == 'n':
        print('===================')
        print('회원가입 취소')
        print('===================')
        exit()
    else:
        print('입력 값을 확인해주세요.')
        
users = []  #user info 리스트 생성

while True:
    user = {}  #dictionary
    username = input('ID: ')
    while True:
        password = input('PW: ')
        password_confirm = input('PW 확인: ')
        if password == password_confirm:
            break
        else:
            print('패스워드가 일치하지 않습니다.')
    
    name = input('이름: ')
    while True:
        birth_date = input('생년월일(6자리): ')
        if len(birth_date) == 6:
            break
        else:
            print('생년월일 다시 입력')      
    
    email = input('이메일: ')
    
    user['username'] = username
    user['password'] = password
    user['name'] = name
    user['birth_date'] = birth_date
    user['email'] = email
    
    users.append(user)
    print(users)
    
    print('==================')
    print(f"{user['name']}님 가입을 환영합니다")
    print('==================')
    
    print('회원가입을 추가로 진행하시겠습니까?n y:진행     n:취소')
    register_another_input = input('>> ')
    register_another_input.lower()
    
    if register_another_input == 'y':
        pass
    elif register_another_input == 'n':
        exit()

    
    