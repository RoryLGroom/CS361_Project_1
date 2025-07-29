from datetime import date, datetime
import json
import os
class Profile:
    def __init__(self, name, DOB, email, username):
        self.name = name
        self.DOB = DOB
        self.email = email
        self.user_id = username
        

class Journal: 
    def __init__(self):
        dateAndTime = datetime.now()
        
        year = dateAndTime.year
        day = dateAndTime.day
        month = dateAndTime.month
        if(month < 10 and day < 10):
            self.todaysDate = str(year) + "-0" + str(month) + "-0" + str(day)
        elif (month < 10):
            self.todaysDate = str(year) + "-0" + str(month) + "-" + str(day)
        elif(day < 10):
            self.todaysDate = str(year) + "-" + str(month) + "-0" + str(day)
        else:
            self.todaysDate = str(year) + "-" + str(month) + "-" + str(day)
        currentTime = dateAndTime.time()
        hour = currentTime.hour
        minutes = currentTime.minute
        seconds = currentTime.second
        self.time = str(hour) + ":" + str(minutes) + ":" + str(seconds)

    
    def createJournalLog(self,text, username):
            
        data = {
            
            "journals": [{
            "user_id": username,
            "date": self.todaysDate,
            "time": self.time,
            "journalEntry": text
            }
            ]
            
        }
        newJournal = {
            "user_id": username,
            "date": self.todaysDate,
            "time": self.time,
            "journalEntry": text
            }
        if os.path.getsize('user.json') != 0:
            with open('user.json', 'r') as json_file:
                addingJournal = json.load(json_file)
            
            addingJournal["journals"].append(newJournal)

            with open("user.json", "w") as json_file:
                json.dump(addingJournal, json_file, indent = 4, ensure_ascii=False)
            print("Journal logged successfully!")
        else:
            with open("user.json", "w") as json_file:
                json.dump(data, json_file, indent = 4, ensure_ascii=False)           
            print("Journal logged successfully!") 
    
    
    def readJournalLog(self, date, username):
        days_journals = []
        with open('user.json', 'r') as json_file:
            data = json.load(json_file)

        journals = data["journals"]

        for journal in journals:
            if(journal['user_id'] == username):
                if journal['date'] == date:
                    days_journals.append((journal['time'], journal['journalEntry']))

        print("Journals for: " + str(date) + "\n ")
        
        print(days_journals, sep = '\n')

    def updateJournal(self, date, username):
        days_journals = []

        self.readJournalLog(date, username)
        selectedTime = input("Which journal would you like to edit? Please enter the time corresponding to your desired journal: \n")
        updatedJournal = input("Please copy and paste the text you would like to edit \n")
        with open('user.json', 'r') as json_file:
            data = json.load(json_file)
        m = 0
        journals = data["journals"]
        for journal in journals:
            if journal['user_id'] == username:
                if journal["time"] == selectedTime:
                    data["journals"][m]["journalEntry"] = updatedJournal
                    with open("user.json", "w") as json_file:
                        json.dump(data, json_file, indent = 4, ensure_ascii=False)           
            
                    print("Journal logged successfully!") 
                    break
                else:
                    m += 1              
