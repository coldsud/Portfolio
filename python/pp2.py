import random


class Student(object):
    def __init__(self,name,number):
    
        self.name=name #instance Variable
        self.courses=[] #Instance Variable
        for i in range(number):
            self.courses.append(0) #initialization which puts the grades at 0

    def __lt__(p,q):
        if p.name<q.name:
            return True
        else:
            return False
    def __ge__(p,q):
        if p.name>=q.name:
            return True
        else:
            return False
    def __eq__(p,q):
        if p.name==q.name:
            return True
        else:
            return False

    def __str__(self):
        courses_str=" ".join(map(str,self.courses))
        return f"{self.name} {courses_str}"   


def main():
    lyst = [
    Student("Berry",10),
    
    Student("Dawn",10),
    
    Student("Gale",10),
    
    Student("Chan",10),
    
    Student("April",10)
    ]
    for count in range(5):
        s=Student("Name" + str(count+1),10)
        
    #shuffle and print the lyst(list)

    random.shuffle(lyst)
    print("Unsorted list of students: ")

    for Student in lyst:
        print("Name: "(lyst))
    lyst.sort
    print("\nSorted list of students: ")
    for Student in lyst:
        print(Student)

    

if __name__ == "__main__":
    main()