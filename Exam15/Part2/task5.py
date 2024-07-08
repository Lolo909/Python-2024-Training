# Task 5: You are given a dictionary representing a person's contact information. The keys are "name," "email," and "phone."
# Create a new dictionary by transforming the keys as follows:
# Replace "name" with "full_name."
# Replace "email" with "email_address."
# Replace "phone" with "contact_number."
# Print the original and transformed dictionaries to compare the key changes.

person_info = {
    "name": "Pesho",
    "email": "pesho@abv.bg",
    "phone":"08812123312"
}

print(person_info)

person_info["full_name"] = person_info.pop("name")
person_info["email_address"] = person_info.pop("email")
person_info["contact_number"] = person_info.pop("phone")

print(person_info)
