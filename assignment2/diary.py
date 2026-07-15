import traceback

try:
    with open("diary.txt", "a") as file:
        first_prompt = True

        while True:
            # Asking the user for input
            if first_prompt:
                diary_input = input("What happened today? ")
                first_prompt = False
            # Asking the user after the first input
            else:
                diary_input = input("What else? ")
                

            # Finish the program when there is a specific input
            if diary_input == "done for now":
                file.write(diary_input + "\n")
                break
            else:
                file.write(diary_input + "\n")




except Exception as e:
   trace_back = traceback.extract_tb(e.__traceback__)
   stack_trace = list()
   for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
   print(f"Exception type: {type(e).__name__}")
   message = str(e)
   if message:
      print(f"Exception message: {message}")
   print(f"Stack trace: {stack_trace}")

