import  unittest
import  medical_diagnosis

sever_dehydration = "Sever Dehydration"
some_dehydration = "Some Dehydration"
no_dehydration = "No Dehydration"
empty_string = ""
patients_and_diagnosis = [
  "Mike - Severe Dehydration",
  "Ben - No Dehydration",
  "Kevin - Some Dehydration"
]

class TestMedicalDiagnosis(unittest.TestCase) :

  ## Tests for the assess_skin function ##

  def test_assess_skin_1(self) :
    result = medical_diagnosis.assess_skin("1")
    self.assertEqual(result, some_dehydration)

  def test_assess_skin_2(self) :
    result = medical_diagnosis.assess_skin("2")
    self.assertEqual(result, sever_dehydration)

  def test_assess_skin(self) :
    result = medical_diagnosis.assess_skin("")
    self.assertEqual(result, empty_string)

  ## Tests for the assess_eyes function ##

  def test_assess_eyes_1(self) :
    result = medical_diagnosis.assess_eyes("1")
    self.assertEqual(result, no_dehydration)

  def test_assess_eyes_2(self) :
    result = medical_diagnosis.assess_eyes("2")
    self.assertEqual(result, sever_dehydration)

  def test_assess_eyes(self) :
    result = medical_diagnosis.assess_eyes("")
    self.assertEqual(result, empty_string)

  ## Test for the save_new_diagnosis ##

  def test_save_new_diagnosis(self) :
    new_patient = "Alex - Sever Dehydration"
    old_length = len(patients_and_diagnosis)
    patients_and_diagnosis.append(new_patient)
    self.assertEqual(old_length + 1, len(patients_and_diagnosis))
