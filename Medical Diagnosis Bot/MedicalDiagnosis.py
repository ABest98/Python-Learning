#######################################################################
# Diagnose a user's state of dehydration based on a short questionnaire
## Yes or No type questions
## Previous answers determine next questions
## Severe/Some/None

# Retrieve and add dehydration diagnoses
## Display a list of patients and diagnoses
## Store new diagnoses to the list
#######################################################################

welcome_prompt = "Welcome doctor, what would you like to do today ?\n - To list all patients, press 1\n - To run a new diagnosis, press 2\n - To quit, press q\n"

name_prompt = "What is the patients name ?\n"

appearance_prompt = "How is the patients general appearance ?\n - 1: Normal\n - 2: Irritable or Lethargic\n"

eye_prompt = "How are the patients eyes ?\n - 1: Eyes are Normal or Slightly Sunken\n - 2: Eyes are very sunken\n"

sever_dehydration = "Sever Dehydration"
some_dehydration = "Some Dehydration"
no_dehydration = "No Dehydration"

def list_patients() :
  print("Listing patients and diagnoses")

def access_skin() :
  print("accessing skin")

def access_eyes(eyes) :
  if eyes == "1" :
    return no_dehydration
  elif eyes == "2" :
    return sever_dehydration

def diagnosis_appearance() :
  appearance = input(appearance_prompt)
  if appearance == "1" :
    eyes = input(eye_prompt)
    diagnosis =  access_eyes(eyes)
  elif appearance == "2" :
    access_skin()

def start_new_diagnosis() :
  name = input(name_prompt)
  diagnosis_appearance()

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