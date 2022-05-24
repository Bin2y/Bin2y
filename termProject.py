# 201802394 윤정빈 Design Pattern TermProject
# 게임? singleton(게임 액터의 생성), facade(전체적인 게임의 구동),
# 인사관리? factory(신입 생성, 재직자 관리 등, 사원 ID 등),composite pattern(부서 이동, 관리) , proxy? 고려해볼만하다
"""
class employee: // 직원 클래스

class department: // prototype?이 될수도 있다. 여러 부서에 상속 가능

class 

composite
"""

class employee:
    def __init__(self, name, gender, ID):
        self.name = name
        self.gender = gender
        self.ID = ID

    def getState(self):
        return self.name,self.gender,self.ID

class employeeBuilder: #builder pattern
    
    def __init__(self):
        self.name = None
        self.gender = None
        self.ID = None
    
    def setName(self,name):
        self.name = name
        return self
    def setGender(self, gender):
        self.gender = gender
    def setID(self, ID):
        self.ID = ID
    def build(self):
        emp = employee(self.name,self.gender,self.ID)
        return emp



class department:
    def __init__(self):
        self.workers=[]
        self.workersCount=0
        self.departmentName = ""  # 부서 이름

    def setDepartmentName(self,departmentName):
        self.departmentName = departmentName

    def register(self, employee:employee):
        self.workers.append(employee)
        self.workersCount+=1
    
    def sendOut(self,employee:employee):
        if employee in self.workers:
            self.workers.remove(employee)
            self.workersCount-=1
    
            



a = employeeFactory()
a.createEmployee("윤정빈", "male", 123)
myhome = department()
myhome.setDepartmentName("집")
myhome.register(a)


