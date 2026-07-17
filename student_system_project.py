# student mangemment system
class invalidScoreError(Exception): # custom exception
    pass
class Students:
    def __init__(self, name, age, student_class, *args, **kwargs):
        self.name = name
        self.age = age
        self.student_class = student_class
        self.scores = args
        self.more_details = kwargs
        for score in self.scores:
            if score < 0 or score > 100:
                raise invalidScoreError(f"Invalid score: {score}. Score must be between 0 and 100.")

    def display_student_info(self): # method display
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Class: {self.student_class}")
        for score in self.scores:
            print(f"Score: {score}")
        total = sum(self.scores)
        average = total / len(self.scores)
        print(f"Total Score: {total}")
        print(f"Average Score: {average}")
        if average >= 50:
            print("Status: Pass")
        else:
            print("Status: Fail")
        for key, value in self.more_details.items():
            print(f"{key}: {value}")

try:
    student1 = Students("John Doe", 20, "10th Grade", 85, 90, 78, address="123 Main St", phone="555-1234")
    student1.display_student_info()
except invalidScoreError as e:
    print(e)
    
    
#