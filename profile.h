#ifndef PROFILE_H
#define PROFILE_H

#include <string>
#include <vector>
using namespace std;

/**
 * @brief 
 * 
 */
struct Users{
    vector<profile> existingUsers;
};
/**
 * @brief storage type for user profile. 
 * @param
 * @return
 */
struct profile{
    string name;
    string email;
    string DOB;
    string password;
    vector<journalLog> journal;

};

/**
 * @brief structure for storing journal logs. Date will be automatically
 * retrived from system, and terminal will prompt user for meta data. If no 
 * meta data recieved, will store first sentance as meta data. 
 * 
 */
struct journalLog{
    string date;
    string metaData;
    vector<string> journalLog;
};

/**
 * @brief prints meta data and date for last three logs
 * 
 * @param userLogs 
 */
void popLastThreeLogs(const journalLog& userLogs);

/**
 * @brief takes string input from terminal and parses into a journalLog. Will
 * be stored in profile. 
 * @param string
 * @return journalLog 
 */
journalLog createLog(string logEntry);

/**
 * @brief 
 * 
 * @return profile 
 */
profile newUser(string userData);


/**
 * @brief ccompares email to known structs to check if there is already a profile. 
 * 
 */
void newUserValidator(string email);


#endif 