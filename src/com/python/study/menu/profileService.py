class profileRepository:

    userList = List()

    @classmethod
    def addUser(cls,userEntity):
        cls.userList.append(userEntity)

        @classmethod
        def seLectAllUser(cls):
