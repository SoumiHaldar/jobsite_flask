from flask import Flask, render_template,jsonify,request

app=Flask(__name__)


# jobs=[
# {
#     'id':1,
#     'title':'Data Analyst',
#     'location':'Hyderabad',
#     'salary':'Rs.10 LPA'
# },
# {
#     'id':2,
#     'title':'Data Scientist',
#     'location':'Bangaluru',
#     'salary':'Rs.12 LPA'
# },
# {
#     'id':3,
#     'title':'Software Engineer',
#     'location':'Delhi',
    
# },
# {
#     'id':4,
#     'title':'Frontend Engineer',
#     'location':'Chennai',
#     'salary':'Rs.15 LPA'
# }
# ]

# To we get jobs from database instead of the list above:
from database import load_jobs_from_db,each_job_from_db,add_application_to_db

@app.route('/')
def index():
    jobs=load_jobs_from_db() # get jobs from database
    return render_template('index.html',jobs=jobs)

@app.route('/api/jobs')
def list_jobs():
    jobs=load_jobs_from_db()
    return jsonify(jobs)

# for dynamic page of jobs
@app.route('/job/<id>')
def show_job(id):
    job=each_job_from_db(id)
    if not job:
        return "Job Not Found", 404
    return render_template('jobpage.html',job=job)

@app.route('/job/<id>/apply', methods=['POST'])
def apply_to_job(id):
    data=request.form
    # to get the information about the job
    job=each_job_from_db(id)
    # store appication in db
    add_application_to_db(id,data)
    return render_template('application_submitted.html',application=data,job=job)




if __name__=='__main__':
    app.run(debug=True)