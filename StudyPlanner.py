planner= {}

a = int(input("enter the number of courses: "))
for i in range(a):
     name = input("enter the name of the course: ")
     hour = int(input("enter how many minutes you've been studying: "))
     date = input("enter the date: ")
     p = input("enter priority level: ")

     planner[name] = {
         "hour" : hour,
         "date" : date,
         "priority" : p
     }

change = input("do you want to change anything?(yes/ no): ")

if change == "yes":
    while True:
        course = input("which course are you willing to change? ")
        if course in planner:
            break
        else:
            print("course not found")

    what = input("what do you want to change?(name/hour/date/priority): ")

    if what == "name":
        planner[course]["name"] = input("enter the new course name: ")
    elif what == "hour":
        planner[course]["hour"] = int(input("enter the new time: "))
    elif what == "date":
        planner[course]["date"] = input("enter the new date: ")
    elif what == "priority":
        planner[course]["priority"] = input("enter the new priority level: ")
    else:
        print("invalid choice")

delete = input("do you want to delete something? (yes/ no)")
if delete == "yes":
    choice = input("what do you want to delete?(course/ info): ")
    if choice == "course":
        while True:
            course = input("enter the name of the course that you want to delete: ")
            if course in planner:
                del planner[course]
                print("course deleted")
                break
            else:
                print("course not found")
    elif choice == "info":
        while True:
            course = input("which course do you want to change? ")
            if course in planner:
                what = input("what do you want to delete?(hour/ date/ priority): ")
                if what in planner[course]:
                    del planner[course][what]
                    print("information deleted")
                    break
            else:
                print("this information doesn't exist")
    else:
        print("invalid choice")

print(planner)


