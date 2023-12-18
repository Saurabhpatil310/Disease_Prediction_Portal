from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class Register(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.EmailField(max_length=67)
    password=models.CharField(max_length=67)
    username=models.CharField(max_length=89)

class lungcancerdata(models.Model):
    Age=models.IntegerField()
    Gender=models.IntegerField()
    Air_Pollution=models.IntegerField()
    Alcohol_Use=models.IntegerField()
    Dust_Allergy=models.IntegerField()
    OccuPational_Hazards=models.IntegerField()
    Genetic_Risk=models.IntegerField()
    Chronic_Lung_Disease=models.IntegerField()
    Balanced_Diet=models.IntegerField()
    Obesity=models.IntegerField()
    Smoking=models.IntegerField()
    Passive_Smoker=models.IntegerField()
    Chest_Pain=models.IntegerField()
    Coughing_Of_Blood=models.IntegerField()
    Fatigue=models.IntegerField()
    Weight_Loss=models.IntegerField()
    Shortness_Of_Breath=models.IntegerField()
    Wheezing=models.IntegerField()
    Swallowing_Difficulty=models.IntegerField()
    Clubbing_Of_Finger_Nails=models.IntegerField()
    Frequent_Cold=models.IntegerField()
    Dry_Cough=models.IntegerField()
    Snoring=models.IntegerField()

class breastcancerdata(models.Model):
    Mean_Radius=models.IntegerField()
    Mean_Texture=models.IntegerField()
    Mean_Perimeter=models.IntegerField()
    Mean_Area=models.IntegerField()
    Mean_Smoothness=models.IntegerField()
    Mean_Compactness=models.IntegerField()
    Mean_Concavity=models.IntegerField()
    Mean_Concave_Points=models.IntegerField()
    Mean_Symmetry=models.IntegerField()
    Mean_Fractal_Dimension=models.IntegerField()
    Radius_Error=models.IntegerField()
    Texture_Error=models.IntegerField()
    Perimeter_Error=models.IntegerField()
    Area_Error=models.IntegerField()
    Smoothness_Error=models.IntegerField()
    Compactness_Error=models.IntegerField()
    Concavity_Error=models.IntegerField()
    Concave_Points_Error=models.IntegerField()
    Symmetry_Error=models.IntegerField()
    Fractal_Dimension_Error=models.IntegerField()
    Worst_Radius=models.IntegerField()
    Worst_Texture=models.IntegerField()
    Worst_Perimeter=models.IntegerField()
    Worst_Area=models.IntegerField()
    Worst_Smoothness=models.IntegerField()
    Worst_Compactness=models.IntegerField()
    Worst_Concavity=models.IntegerField()
    Worst_Concave_Points=models.IntegerField()
    Worst_Symmetry=models.IntegerField()
    Worst_Fractal_Dimension=models.IntegerField()

class diabetesdata(models.Model):
    Pregnancies=models.IntegerField()
    Glucose=models.IntegerField()
    BloodPressure=models.IntegerField()
    SkinThickness=models.ImageField()
    Insulin=models.IntegerField()
    BMI=models.IntegerField()
    DiabetesPedigreeFunction=models.IntegerField()
    Age=models.IntegerField()



