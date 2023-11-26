import  unittest
import  medical_diagnosis

sever_dehydration = "Sever Dehydration"
some_dehydration = "Some Dehydration"
no_dehydration = "No Dehydration"
empty_string = ""

class TestMedicalDiagnosis(unittest.TestCase) :

  def test_assess_skin_1(self) :
    global some_dehydration
    result = medical_diagnosis.assess_skin("1")
    self.assertEqual(result, some_dehydration)

  def test_assess_skin_2(self) :
    global some_dehydration
    result = medical_diagnosis.assess_skin("2")
    self.assertEqual(result, sever_dehydration)

  def test_assess_skin(self) :
    global some_dehydration
    result = medical_diagnosis.assess_skin("")
    self.assertEqual(result, empty_string)