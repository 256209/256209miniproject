from datetime import datetime
from bst_demo import BST, JOB

def get_job_input_details():
    Time = input("Time in hh:mm format, example 13:10 or 1:10-> ")
    while True:
        try:
            datetime.strptime(Time, '%H:%M')
        except ValueError:
            print("Incorrect time format, please follow hh:mm")
            Time = input("Time in hh:mm format, ex 13:10 or 1:10-> ")
        else:
            break
    Jobtime = input("Duration of the job in minutes, ex 60-> ")
    while True:
        try:
            int(Jobtime)
        except ValueError:
            print("Please enter minutes")
            Jobtime = input("Duration of the job in minutes, ex 60-> ")
        else:
            break
    name = input("job name *case sensitive*-> ")
    return Time, Jobtime, name

job_tree = BST()

with open("data.txt") as f:
    for line in f:
        job_tree.insert(line)

while True:
    print("Please choose an option from the list below:")
    print("Press 1 to view jobs")
    print("Press 2 to add a job")
    print("Press 3 to remove a job")
    print("Press 4 to exit")
    option = input("Press the choice you want-> ")
    try:
        entry = int(option)
    except ValueError:
        print("Please enter a choice from the given list")
        continue
    if int(option) == 1:
        job_tree.in_order()
    elif int(option) == 2:
        print("You want to add a job")
        Time, Jobtime, name = get_job_input_details()
        line = Time+","+Jobtime+","+name
        len = job_tree.length()
        job_tree.insert(line)
        if len == job_tree.length()-1:
            with open("data.txt", "a+") as wr:
                wr.write(line+"\n")
        input("any key to cont... ")
    elif int(option) == 3:
        print("You want to remove a job")
        Time, Jobtime, name = get_job_input_details()
        key_to_find = datetime.strptime(Time, '%H:%M').time()
        result = job_tree.find_val(key_to_find)
        if result:
            if result.name_of_job == name and result.duration == Jobtime:
                print("Removing job:")
                print(result)
                job_tree.delete_val(key_to_find)
                print("Job removed")
                with open("data.txt", "r") as f:
                    lines = f.readlines()
                with open("data.txt", "w") as f:
                    for line in lines:
                        if line.strip("\n") != Time+","+Jobtime+","+name:
                            f.write(line)
                input("any key to cont... ")
            else:
                print("The data of job couldnt be found, delete failed")
                input("any key to cont... ")
        else:
            print("Job absent")
            input("any key to cont... ")
    elif int(option) == 4:
        print("quiting...")
        break
    else:
        print("Please select from the given choices")