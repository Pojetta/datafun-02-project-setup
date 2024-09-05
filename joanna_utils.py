'''  ITERATION 5

Module: MindMetrics: Transforming Data into Strategic Clarity

This module provides a simple, reusable foundation for my analytics projects. 

Process:

In this fifth iteration I update the byline to show the min, max, mean and stdev of
client_satisfaction_scores and model_accuracy scores.

'''

#####################################
# Import Modules at the Top
#####################################

import statistics

#####################################
# Declare global variables
#####################################

has_international_clients: bool = True

years_in_operation: int = 10

skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]

client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

accepting_new_clients: bool = True

clients_served: int = 452

model_types: list = ["Predictive Analytics with Machine Learning", "Time Series Forecasting", "Natural Language Processing"]

model_accuracy: list = [92.5, 88.3, 94.7, 90.2, 93.8]

#####################################
# Calculate Basic Statistics 
#####################################

min_score: float = min(client_satisfaction_scores)  
max_score: float = max(client_satisfaction_scores)  
mean_score: float = statistics.mean(client_satisfaction_scores)  
stdev_score: float = statistics.stdev(client_satisfaction_scores)

min_accuracy: float = min(model_accuracy)  
max_accuracy: float = max(model_accuracy)  
mean_accuracy: float = statistics.mean(model_accuracy)  
stdev_accuracy: float = statistics.stdev(model_accuracy)

###################################
# Declare a global variable named byline. 
# Make it a multiline f-string to show our information.
#####################################

byline: str = f"""
---------------------------------------------------------
MindMetrics: Transforming Data into Strategic Clarity
---------------------------------------------------------
Years in Operation:                              {years_in_operation}
Clients Served:                                  {clients_served}
Has International Clients:                       {has_international_clients}
Accepting New Clients:                           {accepting_new_clients}
Skills Offered:                                  {skills_offered}
Model Types:                                     {model_types}

Model Accuracy:                                  {model_accuracy}
Minimum Model Accuracy                           {min_score}
Maximum Model Accuracy                           {max_score}
Mean Model Accuracy                              {mean_score}
Standard Deviation of Model Accuracy             {stdev_score}

Client Satisfaction Scores:                      {client_satisfaction_scores}
Minimum Client Satisfaction Score:               {min_score}
Maximum Client Satisfaction Score:               {max_score}
Average Client Satisfaction Score:               {mean_score}
Standard Deviation of Client Satisfaction Score: {stdev_score}
"""

#####################################
# Define the get_byline() function
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline

#####################################
# Define a main() function for this module
#####################################

# The main function now calls get_byline() to retrieve the byline.
def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional execution
#####################################

if __name__ == '__main__':
    main()
