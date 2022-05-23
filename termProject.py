# 201802394 윤정빈 Design Pattern TermProject
# 게임? singleton(게임 액터의 생성), facade(전체적인 게임의 구동),
# 인사관리? factory(신입 생성, 재직자 관리 등, 사원 ID 등),composite pattern(부서 이동, 관리) , proxy? 고려해볼만하다
"""
class employee: // 직원 클래스

class department: // prototype?이 될수도 있다. 여러 부서에 상속 가능

class 

"""


class employee:
    def __init__(self, name, gender, ID):
        self.name = name
        self.gender = gender
        self.ID = ID

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setGender(self, gender):
        self.gender = gender

    def getGender(self):
        return self.gender

    def setID(self, ID):
        self.ID = ID

    def getID(self):
        return self.ID

    def info(self):
        print("이름 : ", self.name, "성별 : ", self.gender, "ID :", self.ID)

class employeeFactory: #factory pattern
    def __inti__(self):
        self.employee_count=0
    def createEmployee(self,name,gender,ID): #사용할때 인스턴스를 저장할 변수를 선언하면서 사용
        self.employee_count+=1
        return employee(name,gender,ID)
    def employeeCount(self):
        return self.employee_count


class department:
    def __init__(self):
        self.headCount = None  # 부서 인원수
        self.departmentName = None  # 부서 이름

    def setDepartmentName(self, departmentName):
        self.departmentName = departmentName

    def register(self, employee)


a = employee("윤정빈", "male", 123)
