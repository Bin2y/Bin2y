# 201802394 윤정빈 Design Pattern TermProject
"""
class employee: // 직원 클래스

class department: // prototype?이 될수도 있다. 여러 부서에 상속 가능

class 

composite
"""

from dis import Instruction
from unicodedata import name


class employee:
    def __init__(self, name, gender, empID):
        self.name = name
        self.gender = gender
        self.empID = empID

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def empId(self):
        return self.empID

    def getState(self):
        return self.name,self.gender,self.empID

class employeeBuilder: #builder pattern
    
    def __init__(self):
        self.name = None
        self.gender = None
        self.empID = None
    
    def setName(self,name):
        self.name = name
        return self
    def setGender(self, gender):
        self.gender = gender
        return self
    def setID(self, empID):
        self.empID = empID
        return self
    def build(self):
        emp = employee(self.name,self.gender,self.empID)
        return emp



class department: #component class
    def __init__(self):
        self.workers=[]
        
    def register(self, employee:employee):
        self.workers.append(employee)
    
    def remove(self, removeName):
        for index, value in enumerate(self.workers):
            if value.getName()==removeName:
                self.workers.pop(index)
                print("제거완료")
                return True
                
    def info(self):
        pass

class PersonalTeam(department): #concrete1
    def info(self):
        print("인사팀의 직원수는 : " + str(len(self.workers)) + "명 입니다.")
        for i in self.workers:
            print(i.getState())

class AccountingTeam(department): #concrete1
    def info(self):
        print("회계팀의 직원수는 : " + str(len(self.workers)) + "명 입니다.")
        for i in self.workers:
            print(i.getState())
class MarketingTeam(department): #concrete1
    def info(self):
        print("마케팅팀의 직원수는 : " + str(len(self.workers)) + "명 입니다.")
        for i in self.workers:
            print(i.getState())

class Group(department): #composite pattern
    def __init__(self):
        self.components=[]
    def add(self,department:department):
        self.components.append(department)
    def re(self,num):
        return self.components[num]
    def info(self):
        for i in self.components:
            i.info()

    
            

class client: #Facade Pattern
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
    def regist(self):
        name,gender,empID = input("이름 성별 ID를 차례대로 입력해주세요 : ").split()
        newEmp = self.emp.setName(name).setGender(gender).setID(empID).build()
        print("새로운 사원을 넣을 부서를 정하세요")
        print("0 : 인사팀, 1: 회계팀, 2: 마케팅팀")
        num = int(input("숫자를 입력하세요: "))
        team = self.group.re(num)
        team.register(newEmp)
    def remove(self):
        print("제거할 사원이름을 적어주세요")
        removeName = input("사원이름 : ")
        for i in self.group.components:
            isRemove = i.remove(removeName)
            if isRemove:
                break
    def moveDepartment(self):
        print("부서를 정하세요")
        print("0 : 인사팀, 1: 회계팀, 2: 마케팅팀")
        num = int(input("숫자를 입력하세요: "))
        team = self.group.re(num)
        print("옮길 사원이름을 적어주세요")
        moveName = input("사원이름 : ")
        if moveName not in team:
            print(moveName+" 이름을 가진 사원이 존재 하지 않습니다 다시 입력해 주세요")
            moveName = input("사원이름 : ")
        else:
            print("옮길 부서를 정하세요")
            print("0 : 인사팀, 1: 회계팀, 2: 마케팅팀")
    def main(self):
        self.makeGroup()
        print("인사관리 프로그램이 시작되었습니다")
        while(True):
            print("-----------------------------------")
            print("0.모든 정보 1.사원생성 2.사원제거 3.사원이동 10.종료")
            inputNum = int(input("숫자를 입력하세요: "))
            print("-----------------------------------")
            if(inputNum==0):
                self.group.info()
            elif(inputNum==1):
                self.regist()
            elif(inputNum==2):
                self.remove()
            elif(inputNum==3):
                self.moveDepartment()
            elif(inputNum==10):
                break
                

c = client()
c.main()
