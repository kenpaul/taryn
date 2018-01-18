# flask_wtf is the Flask extension to use WTForms
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Application', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class BizClassForm(FlaskForm):
    application = StringField('Application', validators=[DataRequired()])
    q0 = SelectField('Question goes here', choices = [('A', '1'), ('B', '2')])
    q1 = StringField('In the event of a serious or catastrophic failure, what is the Recovery Time Objective? (RTO)',validators=[DataRequired()])
    q2 = StringField('What is the financial loss to Dell of 4 hours of unplanned downtime?',validators=[DataRequired()])
    q3 = StringField('What is Dells regulatory, contractual, or ethical obligations relative to the data?',validators=[DataRequired()])
    q4 = StringField('What is the damage to Dell if the data is compromised, stolen or destroyed?',validators=[DataRequired()])
    q5 = StringField('What is the financial loss (most likely) to Dell if a days worth of data is lost or destroyed?',validators=[DataRequired()])
    q6 = StringField('What is the impact to Total Customer Experience (TCE) due to a failure?',validators=[DataRequired()])
    q7 = StringField('What is the user mix of Employees to Customers?',validators=[DataRequired()])
    q8 = StringField('What would be the cost of a business "work around" solution (manual or automated)?',validators=[DataRequired()])
    q9 = StringField('Approximately "when" is IT Support needed during the month or quarter?',validators=[DataRequired()])
    q10 = StringField('Approximately "when" is IT Support needed at end of month or quarter?',validators=[DataRequired()])
    q11 = StringField('Where is the user population located',validators=[DataRequired()])
    q12 = StringField('What is the quarterly pattern of usage, or flow of data?',validators=[DataRequired()])
    q13 = StringField('How would you describe the data?',validators=[DataRequired()])
    q14 = StringField('What is the Dell Data Classification of your data?',validators=[DataRequired()])
    q15 = StringField('What is the most critical or sensitive data stored?',validators=[DataRequired()])
    q16 = StringField('How many users will be using this application?',validators=[DataRequired()])
    remember_me = BooleanField('Remember Answers')
    submit = SubmitField('Model')
