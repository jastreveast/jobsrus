# index will only send html vue file 
from flask import Blueprint, current_app, render_template
from flask import current_app as app 
import csv
from application.database import db 
from application.models.job import Job

index_bp = Blueprint(
    'index_bp',
    __name__,
   
)

@index_bp.route('/')
def index():
    return current_app.send_static_file('index.html')

@app.cli.command('populateJobData')
def populateJobData():
    f = open('/Users/jasoneast/Desktop/jobsrus/api/application/index/data.csv', 'r')

    with f:

        reader = csv.reader(f)
        row_count = 0
        column_count = 0

        for row in reader:
            if row_count == 0:
                row_count += 1
                continue
            else:
                date = row[1]
                title = row[2]
                company = row[3]
                location = row[10]
                description = row[11]
                requirements = row[12]
                qualifications = row[13]
                salary = row[14]
                application = row[15]

                job = Job(
                    date=date,
                    title=title,
                    company=company,
                    location=location,
                    description=description,
                    requirements=requirements,
                    qualifications=qualifications,
                    salary=salary,
                    application=application
                )
                db.session.add(job)
                db.session.commit()
                
        
    print(f'complete')



