def place():
    roomDict = {"CS101": '3004', "CS102": '4501', "CS103": '6755', "NT110": '1244', "CM241": '1411'}
    return (roomDict)
def instructor():
    instructorDict = {"CS101": 'Haynes', "CS102": 'Alvarado', "CS103": 'Rich', "NT110": 'Burke', "CM241": 'Lee'}
    return (instructorDict)
def time():
    timeDict = {"CS101": '8:00 a.m.', "CS102": '9:00 a.m.', "CS103": '10:00 a.m.', "NT110": '11:00 a.m.', "CM241": '1:00 p.m.'}
    return(timeDict)
def main():
    placedict=place()
    instructordict= instructor()
    timedict= time()
    course = input("Enter a course number: ")
    where = placedict[course]
    who = instructordict[course]
    when = timedict[course]
    print ("you will meet in room ",where," with ",who," at ", when)
main()