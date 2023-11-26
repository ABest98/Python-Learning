#######################################################################
# Diagnose a user's state of dehydration based on a short questionnaire
## Yes or No type questions
## Previous answers determine next questions
## Severe/Some/None

# Retrieve and add dehydration diagnoses
## Display a list of patients and diagnoses
## Store new diagnoses to the list
#######################################################################
### Program doesn't persist ###

# Prompts For the questions and selections
welcome_prompt = "Welcome doctor, what would you like to do today ?\n - To list all patients, press 1\n - To run a new diagnosis, press 2\n - To quit, press q\n"

name_prompt = "What is the patient's name ?\n"

appearance_prompt = "How is the patient's general appearance ?\n - 1: Normal\n - 2: Irritable or Lethargic\n"

eye_prompt = "How are the patient's eyes ?\n - 1: Eyes are Normal or Slightly Sunken\n - 2: Eyes are very sunken\n"

skin_prompt = "How is the patient's skin when you pinch it ?\n - 1: Normal Skin Pinch\n - 2: Slow Skin Pinch\n"

error_message = "Could not save patient and diagnosis due to invalid input\n"

sever_dehydration = "Sever Dehydration"
some_dehydration = "Some Dehydration"
no_dehydration = "No Dehydration"

#Creating a patient and diagnosis list
patients_and_diagnosis = [
  "Mike - Severe Dehydration",
  "Ben - No Dehydration",
  "Kevin - Some Dehydration"
]

# Worker functions
def list_patients() :
  for patient in patients_and_diagnosis :
    print(patient)

def assess_skin(skin) :
  if skin == "1" :
    return some_dehydration
  elif skin == "2" :
    return sever_dehydration
  else :
    return ""

def assess_eyes(eyes) :
  if eyes == "1" :
    return no_dehydration
  elif eyes == "2" :
    return sever_dehydration
  else :
    return ""
  
def save_new_diagnosis(name, diagnosis) :
  if name == "" or diagnosis == "" :
    print(error_message)
    return
  final_diagnosis = name + " - " + diagnosis
  patients_and_diagnosis.append(final_diagnosis)
  print("Final Diagnosis: " + final_diagnosis, "\n")

# Main functions
def assess_appearance() :
  appearance = input(appearance_prompt)
  if appearance == "1" :
    eyes = input(eye_prompt)
    return assess_eyes(eyes)
  elif appearance == "2" :
    skin = input(skin_prompt)
    return assess_skin(skin)
  else :
    return ""

def start_new_diagnosis() :
  name = input(name_prompt)
  diagnosis = assess_appearance()
  save_new_diagnosis(name, diagnosis)

def start() :
  # Will rerun prompts till q is pressed then it'll end
  while(True) :
    selection = input(welcome_prompt)
    if selection == "1" :
      list_patients()
    elif selection == "2" :
      start_new_diagnosis()
    elif selection == "q" :
      return

start()