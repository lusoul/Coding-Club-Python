import graphlab
import pandas

# sf = graphlab.SFrame("/Users/lusoul/Desktop/Git-Hub/Coding-Club-Python/MachineLearning/CourseraClass/home_data.gl")
# sf.save("./home_data.csv", format="csv")
df = pandas.read_csv("./home_data.csv")
print type(df)