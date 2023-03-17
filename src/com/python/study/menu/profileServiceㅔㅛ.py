class profileservice:
    from src.com.prthon.study.menu.UserEntity import UserEntity
    class profileService:

    @staticmethod
    def addUser():
        print("사용자 등록 시작")
        username = input("사용자이름을 입력하세요:")
        password = input("비닐번호를 입력하세요:")
        name = input("성명을 입력하세요: ")
        email = input("이메일을 입력하세요: ")
        userEntity = userEntity(username, password, name, email)
        profileRepository.insertUsr(userEntity)
        print(f"등록된 사용자 정보>>> {userEntity}")

        @staticmethod
        def showUserAll():
            print("[사용자 전제 조회]")
            userList = profileRepository.seLectAllUser()
            for user in userList:
                print(user)
                print("====<< 사용자")