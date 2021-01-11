# index will only send html vue file 
from flask import Blueprint, current_app, render_template, request, jsonify, url_for
from application.database import db
from application.models.job import Job

job_search_bp = Blueprint(
    'job_search_bp',
    __name__,
   
)

@job_search_bp.route('/job_search', methods=['POST'])
def job_search():
    json = request.get_json()
    page = request.args.get('job_page', 1, type=int)
    what = json.get('what')
    where = json.get('where')

    if page == None:
      page = 1

    # TODO only searching on the what term in development
    search_query = '%{}%'.format(what)
    jobs = db.session.query(Job).filter(Job.title.like(search_query)).paginate(page, 10, False)
    # /job_search?job_page=2
    next_jobs_url = url_for('job_search_bp.job_search', job_page=jobs.next_num) if jobs.has_next else None
    prev_jobs_url = url_for('job_search_bp.job_search', job_page=jobs.prev_num) if jobs.has_prev else None

    obj = {
    'page'              : jobs.page,
    'pages'             : jobs.pages,
    'next_records_url'  : next_jobs_url,
    'prev_records_url'  : prev_jobs_url,
    'what'              : what,
    'where'             : where,
    'jobs'              : []
    }

    for job in jobs.items:
      obj['jobs'].append(
        {
          'id': job.id,
          'date': job.date,
          'title': job.title,
          'company': job.company,
          'location': job.location,
          'description': job.description
        }
      )

    return jsonify(obj)


# class Jobs():
#   def __init__(self, location, keywords):
#     self.keywords = keywords
#     self.location = location

#   def find_jobs(self):

#     cj  =  CareerjetAPIClient("en_ZA")

#     result_json = cj.search({
#                             'location'    : self.location,
#                             'keywords'    : self.keywords,
#                             'affid'       : '7949a2105cac900afaa60a62d35af2b9',
#                             'user_ip'     : '11.22.33.44',
#                             'url'         : 'http://www.jobnet.co.za/',
#                             'user_agent'  : 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'
#                           })

#     return result_json


    
