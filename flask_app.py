from flask import Flask, render_template, request

from conncetion import get_response

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def ask():
    if request.method == "GET":
        return render_template('resume_input.html')
    elif request.method == "POST":
        full_name = request.form.get("full_name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        location = request.form.get("location")
        linkedin = request.form.get("linkedin")
        github = request.form.get("github")
        portfolio = request.form.get("portfolio")
        target_job_role = request.form.get("target_job_role")
        years_of_experience = request.form.get("years_of_experience")
        skills = request.form.get("skills")
        tools_technologies = request.form.get("tools_technologies")
        projects = request.form.get("projects")
        education = request.form.get("education")
        certifications = request.form.get("certifications")
        achievements = request.form.get("achievements")

        user_prompt = f'Generate an ATS-friendly resume using the following candidate details:"full_name": "{full_name}","email": "{email}","phone": "{phone}","location": "{location}","linkedin": "{linkedin}","github": "{github}","portfolio": "{portfolio}","target_job_role": "{target_job_role}","years_of_experience": "{years_of_experience}","skills": {skills},"tools_technologies": {tools_technologies},"projects": {projects},"education": {education},"certifications": {certifications},"achievements": {achievements},---### ADDITIONAL INSTRUCTIONS: Customize the resume specifically for the target job role, Emphasize achievements and measurable outcomes, Ensure ATS keyword optimization, Maintain a clean, professional structure,Return only the final resume. MANDATORILY RETURN THE RESPONSE IN HTML FORMAT WITH DOWNLOAD BUTTON'
        ai_resume=get_response(user_prompt)
        return render_template('resume_output.html',ai_response=ai_resume)

app.run(debug=True)
