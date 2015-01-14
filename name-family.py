#CMPUT 410 Lab1 by Chongyang Ye
#This program allows add courses and 
#corresponding marks for a student
#and count the average score
class Student:
    courseMarks={}
    name= ""    
    def __init__(self,name,family):
        self.name = name
        self.family = family
       
    def addCourseMark(self, course, mark):
        self.courseMarks[course] = mark
    
    def average(self):
        grade= []
        grade= self.courseMarks.values()
        averageGrade= sum(grade)/float(len(grade))
        print("The course average for %s is %.2f" %(self.name, averageGrade))
    
    
    
    
if __name__ == "__main__":
    student = Student("Jeff", "Hub")
    student.addCourseMark("CMPUT410", 90)
    student.addCourseMark("CMPUT379", 95)
    student.addCourseMark("CMPUT466", 80)
    student.average()
    
    
    
    

