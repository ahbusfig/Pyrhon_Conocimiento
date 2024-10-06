class Course:
    def __init__(self, name, duration, link):
        self.name = name
        self.duration = duration
        self.link = link

    def __repr__(self):
        return f"The course {self.name} has a duration of {self.duration} hours and his link is {self.link}"
    
    def __str__(self):
        return f"The course {self.name} has a duration of {self.duration} hours and his link is {self.link}"
    
#Crear lista de objetos course
courses = [
        Course("Introduccion a Linux", 15, "url1"),
        Course("Personalizacion de Linux", 3, "url2"),
        Course("Intoduccion al hacking", 53, "url3"),
        Course("Python defensivo", 90, "url4"),

    ] 

def list_of_courses():
        for course in courses:
            print(course)

