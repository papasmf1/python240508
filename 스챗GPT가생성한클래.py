class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        print("ID:", self.id)
        print("Name:", self.name)


class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        super().printInfo()
        print("Title:", self.title)


class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        super().printInfo()
        print("Skill:", self.skill)


def run_tests():
    # Person 테스트
    print("---Person 테스트---")
    person1 = Person("001", "Alice")
    person1.printInfo()

    # Manager 테스트
    print("\n---Manager 테스트---")
    manager1 = Manager("101", "Bob", "Senior Manager")
    manager1.printInfo()

    # Employee 테스트
    print("\n---Employee 테스트---")
    employee1 = Employee("201", "Charlie", "Python Developer")
    employee1.printInfo()

    # 추가 테스트
    print("\n---추가 테스트 1---")
    person2 = Person("002", "Eve")
    person2.printInfo()

    print("\n---추가 테스트 2---")
    manager2 = Manager("102", "David", "Project Manager")
    manager2.printInfo()

    print("\n---추가 테스트 3---")
    employee2 = Employee("202", "Frank", "Java Developer")
    employee2.printInfo()

    print("\n---추가 테스트 4---")
    person3 = Person("003", "Grace")
    person3.printInfo()

    print("\n---추가 테스트 5---")
    manager3 = Manager("103", "Hannah", "Product Manager")
    manager3.printInfo()

    print("\n---추가 테스트 6---")
    employee3 = Employee("203", "Ivy", "Web Developer")
    employee3.printInfo()

    print("\n---추가 테스트 7---")
    person4 = Person("004", "Jack")
    person4.printInfo()

    print("\n---추가 테스트 8---")
    manager4 = Manager("104", "Kevin", "IT Manager")
    manager4.printInfo()

    print("\n---추가 테스트 9---")
    employee4 = Employee("204", "Lily", "Frontend Developer")
    employee4.printInfo()

    print("\n---추가 테스트 10---")
    person5 = Person("005", "Mike")
    person5.printInfo()


if __name__ == "__main__":
    run_tests()


#직접 모듈을 실행했는지 여부 
if __name__ == "__main__":
    run_tests()
