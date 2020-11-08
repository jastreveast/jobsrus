# index will only send html vue file 
from flask import Blueprint, current_app, render_template, request, jsonify
from careerjet_api import CareerjetAPIClient

job_search_bp = Blueprint(
    'job_search_bp',
    __name__,
   
)

@job_search_bp.route('/job_search', methods=['POST'])
def job_search():
    what = request.args.get('what')
    where = request.args.get('where')

    jobs = Jobs(where, what)
    result = jobs.find_jobs()
    print(result)
    return jsonify(result)


class Jobs():
  def __init__(self, location, keywords):
    self.keywords = keywords
    self.location = location

  def find_jobs(self):

    cj  =  CareerjetAPIClient("en_ZA")

    result_json = cj.search({
                            'location'    : self.location,
                            'keywords'    : self.keywords,
                            'affid'       : '213e213hd12344552',
                            'user_ip'     : '11.22.33.44',
                            'url'         : 'http://www.example.com/jobsearch?q=python&l=london',
                            'user_agent'  : 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'
                          })

    return result_json


    
