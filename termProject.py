# 201802394 윤정빈 Design Pattern TermProject
# 게임? singleton(게임 액터의 생성), facade(전체적인 게임의 구동),
# 인사관리? builder(신입 생성, 재직자 관리 등, 사원 ID 등),composite pattern(부서 이동, 관리) , proxy? 고려해볼만하다
"""
class employee: // 직원 클래스

class department: // prototype?이 될수도 있다. 여러 부서에 상속 가능

class 

composite
"""

from dis import Instruction


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
        return self
    def setID(self, ID):
        self.ID = ID
        return self
    def build(self):
        emp = employee(self.name,self.gender,self.ID)
        return emp



class department: #component class
    def __init__(self):
        self.workers=[]
        self.workersCount=0
        
    def register(self, employee:employee):
        self.workers.append(employee)
        self.workersCount+=1
    
    def sendOut(self,employee:employee):
        if employee in self.workers:
            self.workers.remove(employee)
            self.workersCount-=1
    
    def info(self):
        pass

class PersonalTeam(department): #concrete1
    def info(self):
        print("인사팀의 직원수는 : " + self.workersCount + "명 입니다.")

class AccountingTeam(department): #concrete1
    def info(self):
        print("회계팀의 직원수는 : " + self.workersCount + "명 입니다.")

class MarketingTeam(department): #concrete1
    def info(self):
        print("마케팅팀의 직원수는 : " + self.workersCount + "명 입니다.")
    
class Group(department): #composite pattern
    def __init__(self):
        self.components=[]
    def add(self,department:department):
        self.components.append(department)
    def info(self):
        for i in len(self.components):
            self.components[i].info()

    
            

class client:
    def __init__(self):
        self.P = PersonalTeam()
        self.A = AccountingTeam()
        self.M = MarketingTeam()
        self.group = Group()
        self.emp = employeeBuilder()
    def makeGroup(self):
        self.group.add(self.P)
        self.group.add(self.A)
        self.group.add(self.M)
    def start(self):
        print("인사관리 프로그램이 시작되었습니다")
        while(True):
            print("1.사원생성 2.사원제거 3.회사원수 10.종료")
            inputNum = input("숫자를 입력하세요: ")
            if(inputNum==0):
                break
            elif(inputNum==1):
                print("이름 성별 나이를 차례대로 입력해주세요.")
                newEmp = self.emp.build(name,gender,ID)
                print("새로운 사원을 넣을 부서를 정하세요")
            elif(inputNum==2):
                print("제거할 사원이름을 적어주세요")
                

c = client()
c.start()
