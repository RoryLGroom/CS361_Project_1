from functionsCall import Profile, Journal

infoDecision = input("Thank you for using The Wellness Journal! Would you like to see the current and upcoming features? Please type YES or NO: \n")
if(infoDecision == "YES"):
    print("The Wellness journal aims to aid our users by giving them a private journal to record their thoughts and feelings, and recall them in an instant! We offer ")
existingUser = input("Do you have an account? Please answer with YES or NO: ")
if existingUser == "NO":
    name = input("What is your full name?: \n")
    DOB = input("What is your date of birth?: \n")
    email = input("What is your email?: \n")
    username = input("What would you like your username to be?: \n")
    newUser = Profile(name, DOB, email, username)
else:
    username = input("What is your username?: \n")

myJournal = Journal()
print("\n")
userOptions = input("Would you like to CREATE, READ, or UPDATE a journal entry?: \n")
if userOptions == "CREATE":
    todays_journal = input("How are you feeling?: \n")
    myJournal.createJournalLog(todays_journal, username)
elif userOptions == "READ": 
    
    journalDate = input("For what day would you like to view your journals? Please enter date in YYYY-MM-DD format: \n")
    myJournal.readJournalLog(journalDate, username)
elif userOptions == "UPDATE":
    chosenDate = input("What day do you want to update? Please enter in YYYY-MM-DD format \n")
    myJournal.updateJournal(chosenDate, username)