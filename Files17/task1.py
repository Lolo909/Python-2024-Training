try:
    with open('Files17\sample_text.txt', 'w') as file:
        i = 1
        while i <= 5:
           file.write("This is line " + str(i) + ".")
           i+=1
        
    with open('Files17\sample_text.txt', 'r') as file:
        text = file.read()
        file.seek(30)
        text2 = file.read()

        print(text2)
    
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")