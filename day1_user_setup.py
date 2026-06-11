#!/usr/bin/env python3
print("=== CORPORATE USER ONBOARDING SYSTEM ===\n")
# 1. Gathering input from the Admin
username = input("Enter the new employee's username: ")
department = input("Enter their department (e.g., IT, HR, Finance): ")

#2. String Concatention in action
# We are gluing the raw text, the variables, and your \n newline tricks together
summary_report = "\n[SUCCESS] Account created for: " + username + "\n[INFO] Assigned Department: " + department + "\n[SECURITY] Default permissions granted: Domain_User"

# 3. Printing the final concatenated string
print(summary_report)
print("\n========================================")
