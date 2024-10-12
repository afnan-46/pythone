def personal_info(First_name, Last_name):
    print("hello")
    print(f"{First_name} {Last_name}")

personal_info("Afnan", "Ahmed")


def get_greeting(name):
    return f"Hello {name}"

message = get_greeting("Ahmed")
file=open("hello.txt","w")
file.write(message)