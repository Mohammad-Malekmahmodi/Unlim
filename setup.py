def add(students_list, student_id, student_name):
    students_list.append({
        "id": student_id,
        "name": student_name
    })


def remove(students_list, student_id):
    for index, student in enumerate(students_list):
        if student["id"] == student_id:
            students_list.pop(index)
            return False  # or any other result/message


def check(students_list, student_id):
    for student in students_list:
        if student["id"] == student_id:
            return True
    return False


def get_student_id(students_list, student_name):
    for student in students_list:
        if student["name"] == student_name:
            return student["id"]
    return None


def main():
    n = int(input())
    students_list = []
    for _ in range(n):
        command = input()
        if command == "add":
            student_id = int(input())
            student_name = input()
            add(students_list, student_id, student_name)
        elif command == "remove":
            input_command = input()
            if input_command.startswith("get_id "):
                student_id = int(input_command[7:])
            else:
                student_id = int(input_command)
            remove_result = remove(students_list, student_id)
            if remove_result is False:
                print("removed")
            else:
                print("not found")
        elif command == "check":
            student_id = int(input())
            if check(students_list, student_id):
                print("yes")
            else:
                print("no")
        elif command == "get_id":
            student_name = input()
            student_id = get_student_id(students_list, student_name)
            if student_id is not None:
                print(student_id)
            else:
                print("not found")


if __name__ == "__main__":
    main()
