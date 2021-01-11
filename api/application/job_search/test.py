from job_search import Jobs

location = "Durban"
keywords = "Python"

jobs = Jobs(location, keywords)

result = jobs.find_jobs()

print(result)
