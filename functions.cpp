#include <iostream>

#include "profile.h"

using namespace std;


bool newUserValidator(const Users& u, string email)
{
  for (int i = 0; i < u.existingUsers.size(); i++) {
    if (u.existingUsers[i].email == email) {
      return false;
    }
  }
  return true;
}

profile newUser(string& name, string& DOB, string& email, string& password)
{
}