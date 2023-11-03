from flask import Flask, render_template,jsonify

app=Flask(__name__)
jobs=[
{
    'id':1,
    'title':'Data Analyst',
    'location':'Hyderabad',
    'salary':'Rs.10 LPA'
},
{
    'id':2,
    'title':'Data Scientist',
    'location':'Bangaluru',
    'salary':'Rs.12 LPA'
},
{
    'id':3,
    'title':'Software Engineer',
    'location':'Delhi',
    
},
{
    'id':4,
    'title':'Frontend Engineer',
    'location':'Chennai',
    'salary':'Rs.15 LPA'
}
]
@app.route('/')
def index():
    return render_template('index.html',jobs=jobs)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(jobs)

if __name__=='__main__':
    app.run(debug=True)