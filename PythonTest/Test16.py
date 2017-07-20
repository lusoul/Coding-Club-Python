import os
print os.getcwd()

import graphlab

sales = graphlab.SFrame("/Users/lusoul/Git-Hub/Coding-Club-Python/MachineLearning/CourseraClass/home_data.gl")
print sales

print sales[{"id":["7129300520", "6414100192", "5631500400"]}]