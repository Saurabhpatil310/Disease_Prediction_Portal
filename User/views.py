from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib import messages


import pandas as pd

import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from .models import diabetesdata, lungcancerdata

from .models import breastcancerdata

#user is table name

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    if request.method=="POST":
        uname=request.POST['uname']
        pass1=request.POST['pass']
        user=authenticate(username=uname,password=pass1)
        if user is not None:
            auth.login(request,user)
            messages.info(request,"Logout Successful")
            return render (request,'index.html')
        else:
            messages.info(request,"Invalid Credentials")
            # return render(request,'login.html') 
    return render(request,'login.html') 

def register(request):
    if request.method=="POST":
        first=request.POST['fname']
        username=request.POST['uname']
        last=request.POST['lname']
        mail=request.POST['email']
        p1=request.POST['pass']
        p2=request.POST['pass1']
        if p1==p2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exits")
                return render(request,'register.html')
        elif User.objects.filter(email=mail).exists():
            messages.info(request,"Email already exits")
            return render(request,'register.html')
        #create database connection for that create obj for db table
        user=User.objects.create_user(first_name=first,last_name=last,
             email=mail,password=p1,username=username)
        user.save()
        return redirect('login')
    else:
        # messages.info(request,"Password not matching")
        return render(request,'register.html')
    
    
def lungcancer(request):
    return render(request,'lcancer.html')
def breastcancer(request):
    return render(request,'bcancer.html')
def diabetes(request):
    return render(request,'diabetes.html')
    
def Predictlung(request):
    if (request.method == 'POST'):
        age=request.POST['age']
        gender=request.POST['gender']
        airpollution=request.POST['airpollution']
        alcoholuse=request.POST['alcoholuse']
        dustallergy = request.POST['dustallergy']
        occupationalhazards=request.POST['occupationalhazards']
        geneticrisk= request.POST['geneticrisk']
        chroniclungdisease=request.POST['chroniclungdisease']
        balanceddiet=request.POST['balanceddiet']
        obesity= request.POST['obesity']
        smoking=request.POST['smoking']
        passivesmoker=request.POST['passivesmoker']
        chestpain=request.POST['chestpain']
        coughingofblood=request.POST['coughingofblood']
        fatigue=request.POST['fatigue']
        weightloss=request.POST['weightloss']
        shortnessofbreath=request.POST['shortnessofbreath']
        wheezing=request.POST['wheezing']
        swallowingdifficulty=request.POST['swallowingdifficulty']
        clubbingoffingernails = request.POST['clubbingoffingernails']
        frequentcold=request.POST['frequentcold']
        dry_cough = request.POST['drycough']
        snoring= request.POST['snoring']

        df = pd.read_csv(r"static/datasets/Lung_cancer.csv")
        df.dropna(inplace=True)
        df.isnull().sum()
        X_train = df[['Age','Gender','Air_Pollution','Alcohol_Use','Dust_Allergy','OccuPational_Hazards','Genetic_Risk','Chronic_Lung_Disease','Balanced_Diet','Obesity',
                      'Smoking','Passive_Smoker','Chest_Pain','Coughing_Of_Blood','Fatigue','Weight_Loss','Shortness_Of_Breath','Wheezing','Swallowing_Difficulty','Clubbing_Of_Finger_Nails',
                      'Frequent_Cold','Dry_Cough','Snoring']]
        y_train = df[['Level']]
        ran = RandomForestClassifier()
        ran.fit(X_train,y_train)
        prediction = ran.predict([[age,gender,airpollution,alcoholuse,dustallergy,occupationalhazards,geneticrisk,chroniclungdisease,balanceddiet,obesity,smoking,passivesmoker,chestpain,coughingofblood,fatigue,
                                   weightloss,shortnessofbreath,wheezing,swallowingdifficulty,clubbingoffingernails,frequentcold,dry_cough,snoring]])
        lungcancer=lungcancerdata.objects.create(Age=age,Gender=gender,Air_Pollution=airpollution,Alcohol_Use=alcoholuse,Dust_Allergy=dustallergy,OccuPational_Hazards=occupationalhazards,Genetic_Risk=geneticrisk,
                                                 Chronic_Lung_Disease=chroniclungdisease,Balanced_Diet=balanceddiet,Obesity=obesity,Smoking=smoking,Passive_Smoker=passivesmoker,Chest_Pain=chestpain,Coughing_Of_Blood=coughingofblood,
                                                 Fatigue=fatigue,Weight_Loss=weightloss,Shortness_Of_Breath=shortnessofbreath,Wheezing=wheezing,Swallowing_Difficulty=swallowingdifficulty,Clubbing_Of_Finger_Nails=clubbingoffingernails,
                                                 Frequent_Cold=frequentcold,Dry_Cough=dry_cough,Snoring=snoring)
        lungcancer.save()
        return render(request,'lungpredict.html',
                      {"lungcancer": prediction,'age':age,'gender':gender,'airpollution':airpollution,'alcoholuse':alcoholuse,'dustallergy':dustallergy,'occupationalhazards':occupationalhazards,'geneticrisk':geneticrisk,'chroniclungdisease':chroniclungdisease,'balanceddiet':balanceddiet,'obesity':obesity,'smoking':smoking,'passivesmoker':passivesmoker,'chestpain':chestpain,'coughingofblood':coughingofblood,'fatigue':fatigue,
                                   'weightloss':weightloss,'shortnessofbreath':shortnessofbreath,'wheezing':wheezing,'swallowingdifficulty':swallowingdifficulty,'clubbingoffingernails':clubbingoffingernails,'frequentcold':frequentcold,'dry_cough':dry_cough,'snoring':snoring })
    else:
        return render(request, 'lungpredict.html')

def predictbreast(request):
    if (request.method == 'POST'):
        meanradius=request.POST['meanradius']
        meantexture=request.POST['meantexture']
        meanperimeter = request.POST['meanperimeter']
        meanarea= request.POST['meanarea']
        meansmoothness= request.POST['meansmoothness']
        meancompactness= request.POST['meancompactness']
        meanconcavity= request.POST['meanconcavity']
        meanconcavepoints= request.POST['meanconcavepoints']
        meansymmetry = request.POST['meansymmetry']
        meanfractaldimension= request.POST['meanfractaldimension']
        radiuserror= request.POST['radiuserror']
        textureerror= request.POST['textureerror']
        perimetererror= request.POST['perimetererror']
        areaerror= request.POST['areaerror']
        smoothnesserror= request.POST['smoothnesserror']
        compactnesserror= request.POST['compactnesserror']
        concavityerror= request.POST['concavityerror']
        concavepointserror= request.POST['concavepointserror']
        symmetryerror= request.POST['symmetryerror']
        fractaldimensionerror= request.POST['fractaldimensionerror']
        worstradius= request.POST['worstradius']
        worsttexture= request.POST['worsttexture']
        worstperimeter= request.POST['worstperimeter']
        worstarea= request.POST['worstarea']
        worstsmoothness= request.POST['worstsmoothness']
        worstcompactness= request.POST['worstcompactness']
        worstconcavity= request.POST['worstconcavity']
        worstconcavepoints= request.POST['worstconcavepoints']
        worstsymmetry= request.POST['worstsymmetry']
        worstfractaldimension= request.POST['worstfractaldimension']

        df = pd.read_csv(r"static/datasets/Breast_cancer.csv")
        df.dropna(inplace=True)
        df.isnull().sum()
        df["Diagnosis"].replace({"M": "Affected", "B": "Not Affected"}, inplace=True)
        X_train=df[['Mean_Radius','Mean_Texture','Mean_Perimeter','Mean_Area','Mean_Smoothness','Mean_Compactness','Mean_Concavity','Mean_Concave_Points','Mean_Symmetry','Mean_Fractal_Dimension',
                    'Radius_Error','Texture_Error','Perimeter_Error','Area_Error','Smoothness_Error','Compactness_Error','Concavity_Error','Concave_Points_Error','Symmetry_Error','Fractal_Dimension_Error',
                    'Worst_Radius','Worst_Texture','Worst_Perimeter','Worst_Area','Worst_Smoothness','Worst_Compactness','Worst_Concavity','Worst_Concave_Points','Worst_Symmetry','Worst_Fractal_Dimension']]
        y_train = df[['Diagnosis']]
        ran = RandomForestClassifier()
        ran.fit(X_train, y_train)
        prediction = ran.predict([[meanradius,meantexture,meanperimeter,meanarea,meansmoothness,meancompactness,meanconcavity,meanconcavepoints,meansymmetry,
                                   meanfractaldimension,radiuserror,textureerror,perimetererror,areaerror,smoothnesserror,compactnesserror,concavityerror,concavepointserror,symmetryerror,
                                   fractaldimensionerror,worstradius,worsttexture,worstperimeter,worstarea,worstsmoothness,worstcompactness,worstconcavity,worstconcavepoints,worstsymmetry,
                                   worstfractaldimension]])

        breastcancer = breastcancerdata.objects.create(Mean_Radius=meanradius,Mean_Texture=meantexture,Mean_Perimeter=meanperimeter,Mean_Area=meanarea,Mean_Smoothness=meansmoothness,Mean_Compactness=meancompactness,Mean_Concavity=meanconcavity,Mean_Concave_Points=meanconcavepoints,Mean_Symmetry=meansymmetry,Mean_Fractal_Dimension=meanfractaldimension,
                                                     Radius_Error=radiuserror,Texture_Error=textureerror,Perimeter_Error=perimetererror,Area_Error=areaerror,Smoothness_Error=smoothnesserror,Compactness_Error=compactnesserror,Concavity_Error=concavityerror,Concave_Points_Error=concavepointserror,Symmetry_Error=symmetryerror,Fractal_Dimension_Error=fractaldimensionerror,
                                                     Worst_Radius=worstradius,Worst_Texture=worsttexture,Worst_Perimeter=worstperimeter,Worst_Area=worstarea,Worst_Smoothness=worstsmoothness,Worst_Compactness=worstcompactness,Worst_Concavity=worstconcavity,Worst_Concave_Points=worstconcavepoints,Worst_Symmetry=worstsymmetry,Worst_Fractal_Dimension=worstfractaldimension)
        breastcancer.save()
        return render(request,'breastpredict.html',
                      {"breastcancer": prediction,'meanradius':meanradius,'meantexture':meantexture,'meanperimeter':meanperimeter,'meanarea':meanarea,'meansmoothness':meansmoothness,'meancompactness':meancompactness,'meanconcavity':meanconcavity,'meanconcavepoints':meanconcavepoints,'meansymmetry':meansymmetry,
                                   'meanfractaldimension':meanfractaldimension,'radiuserror':radiuserror,'textureerror':textureerror,'perimetererror':perimetererror,'areaerror':areaerror,'smoothnesserror':smoothnesserror,'compactnesserror':compactnesserror,'concavityerror':concavityerror,'concavepointserror':concavepointserror,'symmetryerror':symmetryerror,
                                   'fractaldimensionerror':fractaldimensionerror,'worstradius':worstradius,'worsttexture':worsttexture,'worstperimeter':worstperimeter,'worstarea':worstarea,'worstsmoothness':worstsmoothness,'worstcompactness':worstcompactness,'worstconcavity':worstconcavity,'worstconcavepoints':worstconcavity,'worstsymmetry':worstsymmetry,
                                   'worstfractaldimension':worstfractaldimension})
    else:
        return render(request, 'breastpredict.html')



def Predictdiabetes(request):
    if (request.method == 'POST'):
        pregnancies=request.POST['pregnancies']
        glucose=request.POST['glucose']
        blood=request.POST['bp']
        skin=request.POST['skin']
        insulin = request.POST['insulin']
        bmi=request.POST['bmi']
        pedi= request.POST['pedigree']
        age=request.POST['age']
        
        df = pd.read_csv(r"static/datasets/diabetes.csv")
        df.dropna(inplace=True)
        df.isnull().sum()
        # plt.figure(figsize=(12,4))
        # plt.xlabel("Age")
        # plt.ylabel("Outcome")
        # plt.title("Age vs Outcome")
        # plt.plot(df['Age'],df['Outcome'])
        # plt.show()
        # import seaborn as sns
        
        # sns.countplot(df['Outcome'])

        #import seaborn as sns
        #sns.countplot(df['Age'],df['Outcome'])
        X_train = df[["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin",
        "BMI","DiabetesPedigreeFunction","Age"]]
        y_train = df[['Outcome']]
        ran = RandomForestClassifier()
        ran.fit(X_train,y_train)
        prediction = ran.predict([[pregnancies,glucose,blood,skin,
        insulin,bmi,pedi,age]])
        """lungcancer=lungcancerdata.objects.create(Age=age,Gender=gender,Air_Pollution=airpollution,Alcohol_Use=alcoholuse,Dust_Allergy=dustallergy,OccuPational_Hazards=occupationalhazards,Genetic_Risk=geneticrisk,
                                                 Chronic_Lung_Disease=chroniclungdisease,Balanced_Diet=balanceddiet,Obesity=obesity,Smoking=smoking,Passive_Smoker=passivesmoker,Chest_Pain=chestpain,Coughing_Of_Blood=coughingofblood,
                                                 Fatigue=fatigue,Weight_Loss=weightloss,Shortness_Of_Breath=shortnessofbreath,Wheezing=wheezing,Swallowing_Difficulty=swallowingdifficulty,Clubbing_Of_Finger_Nails=clubbingoffingernails,
                                                 Frequent_Cold=frequentcold,Dry_Cough=dry_cough,Snoring=snoring)
        lungcancer.save()"""

        diabetes= diabetesdata.objects.create(Pregnancies=pregnancies,Glucose=glucose,BloodPressure=blood,SkinThickness=skin,Insulin=insulin,
                                                 BMI=bmi,DiabetesPedigreeFunction=pedi,Age=age)
        diabetes.save()
        
        return render(request,'predictdiabetes.html',
                      {"diabetesdata": prediction,'pregnancies':pregnancies,
                      'glucose':glucose,"bp":blood,"skin":skin,"bmi":bmi,"pedigree":pedi,"insulin":insulin,"age":age})
    else:
        return render(request, 'diabetes.html')
