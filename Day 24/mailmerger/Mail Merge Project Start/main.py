#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



PLACEHOLDER = "[name]"

with open(r"C:\Users\YBALASAH\OneDrive - Capgemini\Desktop\git repo\100-days-of-python\Day 24\mailmerger\Mail Merge Project Start\Input\Names\invited_names.txt") as data_f:
        names = data_f.readlines()


with open(r"100-days-of-python\Day 24\mailmerger\Mail Merge Project Start\Input\Letters\starting_letter.txt") as file:
    my_reader = file.read()
    for name in names:
          stripepd_name = name.strip()
          my_letter = my_reader.replace(PLACEHOLDER,stripepd_name)
          with open(fr"C:\Users\YBALASAH\OneDrive - Capgemini\Desktop\git repo\100-days-of-python\Day 24\mailmerger\Mail Merge Project Start\Output\ReadyToSend\letter_for_{stripepd_name}", mode="w") as completed:
                completed.write(my_letter)