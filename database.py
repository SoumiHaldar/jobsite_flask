import sqlalchemy
from sqlalchemy import create_engine,text
import os
from dotenv import load_dotenv
load_dotenv()
db_connection_info=os.getenv('db_connection')
engine = create_engine(db_connection_info)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        # print('type of result:',type(result))
        # result_all=result.all()
        # print('type of all result:',type(result_all))
        # print(result_all)
        # result_dict=dict(result_all)
        # first_result_dict=dict(result_all[0])
        jobs=[]
        for row in result.all():
            jobs.append(dict(row))
        print(jobs)
        return jobs
def each_job_from_db(id):
    with engine.connect() as conn:
        result =conn.execute(text('select * from jobs where id=:val'),val=id)  # using sqlalchemy
        rows=result.all()
        if len(rows)==0:
            return None
        else:
            return dict(rows[0])
        
def add_application_to_db(job_id, data):
  with engine.connect() as conn:
      query=text("Insert INTO Applications (job_id,full_name,email,linkedin_url,education,work_experience,resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")  
      conn.execute(query,
          job_id=job_id,
          full_name=data['full_name'],
          email=data['email'],
          linkedin_url=data['linkedin'],
          education=data['education'],
          work_experience=data['work_exp'],
          resume_url=data['resume_url']

      )
