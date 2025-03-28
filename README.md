Predicting obesity level-  Machine Learning Project

The goal of this project is to predict a person's obesity level ( Insufficient Weight, Normal Weight, Overweight Level I, Overweight Level II, Obesity Type I, Obesity Type II, Obesity Type III ) based on various factors such as diet, physical activity, smoking habits, etc.

Dataset Structure

The dataset is structured as per below:
Gender – Male or Female.
Age – The person’s age in years.
Height – Height in meters.
Weight – Weight in kilograms.
family_history_with_overweight – Whether the person has a family history of being overweight (yes/no).
FAVC – If the person frequently consumes high-calorie foods (yes/no).
FCVC – Frequency of vegetable consumption (scale from 1 to 3).
NCP – Number of main meals per day.
CAEC – Frequency of consuming food between meals (Never, Sometimes, Frequently, Always).
SMOKE – Whether the person smokes (yes/no).
CH2O – Daily water intake (scale from 1 to 3).
SCC – If the person monitors their calorie intake (yes/no).
FAF – Physical activity frequency (scale from 0 to 3).
TUE – Time spent using technology (scale from 0 to 3).
CALC – Frequency of alcohol consumption (Never, Sometimes, Frequently, Always).
MTRANS – Main mode of transportation (Automobile, Bike, Motorbike, Public Transportation, Walking).

Target ->:NObeyesdad – Obesity level (Insufficient Weight, Normal Weight, Overweight Level I, Overweight Level II, Obesity Type I, Obesity Type II, Obesity Type III). Primary focus is to understand which features most significantly impact NObeyesdad. 


At the beginning, the data was cleaned and after acomplishing the EDA process the data was encoded into numerical feautures. 
Then the type of supervised learning was chosen: Classyfication. 

The 3 baseline models were chosen: Logistic Regression, Random Forest and XGB.



Baseline Model Accuracy:
Logistic Regression: 0.7328605200945626
Random Forest: 0.9550827423167849
XGB: 0.9574468085106383


From baselines models, the XGB model was chosen for further exploration. 

In the next steps, the baseline model accuracy was tried to be improved.
Next steps that were taken - Dropping the features from feature importance based on 'gain' under the threshold equal to 1:
'family_history_with_overweight'
'SCC'
'SMOKE'
'MTRANS'
'TUE'
'FAF'
'Age'

New column was created - BMI, as a formula coming from weight and height column.
After it was created, the 'weight' and 'height' were dropped.
The model at that point improved in its accuracy: 

XGB accuracy after improvements: 
0.9739952718676123

At the end from feature importance only 2 features were chosen for the model to run 'BMI' and 'Gender' as they had the biggest importance compared to the other features. 

The final model accuracy dropped a bit and it lowered to 0.9598108747044918 however the accuracy drop was okay considering that the model was based only on 2 feautures.

Streamlit app was created to show user friendly interface and to be able to interact with the model. 
