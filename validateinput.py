def validateInput(value):
    while True:
        try:
            data = value
        except ValueError:
            print("Try another value..")
            continue
        else:
            break

prompt = int(input("give me an integer"))
validateInput(prompt)