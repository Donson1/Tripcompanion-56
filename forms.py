from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, SelectField, IntegerField,PasswordField, SearchField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError


#admin form
class RegistrationForm(FlaskForm):
    id = IntegerField('id', validators=[(DataRequired())])
    name = StringField('name', validators=[(DataRequired())])
    yearCompleted= SelectField('yearCompleted', choices=[(2021,2021)])
    nationality = StringField('nationality',validators=[DataRequired()] )
    contact= StringField('contact',validators=[ DataRequired(), Length(min=10, max=10, message="Your number shouldn't be less than 10")])
    email = StringField('email',validators=[(DataRequired() )])
    faculty = SelectField('faculty',  choices=[('Campus','Campus'),('CU', 'CU'), ('Legon','Legon'), ('KNUST','KNUST'), ('UPSA', 'UPSA')], default=None )
    hallofresidence = SelectField('hallofresidence',  choices=[('Halls','Halls'),('Joy Otabil', 'Joy Otabil'), ('Faith','Faith'), ('Freedom','Freedom'), ('Kathryl Kuhlman ', 'Kathryl Kuhlman '), ('Justice','Justice'), ('Billy Graham','Billy Graham'),('Billy Graham','Billy Graham'),  ('Chancellor', 'Chancellor'),('Integerity','Integerity'), ], default=None )
    password = PasswordField('password')
    submit = SubmitField('Register')
    program=StringField('program', validators=[(DataRequired())])
    indexnumber =StringField('name', validators=[(DataRequired())])
    gender =StringField('gender', validators=[(DataRequired())])
    school =StringField('school', validators=[(DataRequired())])
    department =StringField('department', validators=[(DataRequired())])
    yearCompleted =StringField('yearCompleted', validators=[(DataRequired())])
    admitted =  StringField('admitted', validators=[(DataRequired())])
    telephone =  StringField('telephone', validators=[(DataRequired())])
    address =  StringField('address', validators=[(DataRequired())])
    work =  StringField('work', validators=[(DataRequired())])
    guardian =  StringField('guardian', validators=[(DataRequired())])
    marital =StringField('marital', validators=[(DataRequired())])
    extra =    StringField('extra', validators=[(DataRequired())])
    image_file =  StringField('image', validators=[(DataRequired())])
    
#admin login              
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
 
class Registration(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    indexnumber = StringField('indexnumber')
    name = StringField('Name', validators=[DataRequired()])
    phone= StringField('phone')
    password = PasswordField('password')
    faculty = SelectField('faculty',  choices=[('Campus','Campus'),('CU', 'CU'), ('Legon','Legon'), ('KNUST','KNUST'), ('UPSA', 'UPSA')], default=None )
   
    submit = SubmitField('SignUp')  
    # el4 = SelectField('el4', default='None', choices=[(user.lastname, user.lastname) for user in Person.query.all()])  
  

#forms
class Adduser(FlaskForm):
    schools = SelectField('Booking',choices=[('Booking','Booking'),
                        ('1 - 5 ', '1 - 5'),
                        ('5 - 10', '5 - 10'),
                ('More', 'More'),
                
                
             
                

                ], default=None )
    year= SelectField('Level', choices=[
    ('Centers', 'Centers'),
    ('Hotel', 'Hotel'),
    ('Restaurant', 'Restaurant'),
    ('Appartment', 'Appartment'),
    ('Resort', 'Resort'),
    ('Super Market', 'Super Market'),
  
    
    
    
], default=None)
    guardian= StringField('guardian')
    fees= StringField('fees')
    link= StringField('link')
    desc= StringField('desc')
   
    index= StringField('index')
    arrears= StringField('arrears')
    image_file = StringField('image_file')
    image_file1 = StringField('image_file1')
    image_file2 = StringField('image_file2')
    submit = SubmitField('submit') 
    
class Story(FlaskForm):
    fullname = StringField('fullname')
    work= StringField('work')
    guardian= StringField('guardian')
    image_file = StringField('image_file')
    submit = SubmitField('submit') 
    
    
class Formtripfrom(FlaskForm):
    name = StringField('name')
    email= StringField('email')
    message= StringField('message')
    submit = SubmitField('submit') 
    
class Locationform(FlaskForm):
    fullname = StringField('fullname')
    center= SelectField('Level', choices=[
    ('Centers', 'Centers'),
    ('Hotel', 'Hotel'),
    ('Restaurant', 'Restaurant'),
    ('Appartment', 'Appartment'),
    ('Resort', 'Resort'),
    ('Super Market', 'Super Market'),
        
], default=None)
    location= StringField('location')
    submit = SubmitField('submit') 
    
  

    
    
# create a search form
class Search(FlaskForm):
    searched = StringField('Searched', validators=[DataRequired()])
    submit = SubmitField('Search') 
    
    
class UserSearch(FlaskForm):
    searched = StringField('Searched', validators=[DataRequired()])
    submit = SubmitField('Search') 
    
class Adsearch(FlaskForm):
    searched = StringField('Searched', validators=[DataRequired()])
    submit = SubmitField('Search') 
    
  
  
#userlogin  
class Post(FlaskForm):
    extra = StringField('extra')
    address = StringField('address')
    telephone = StringField('telephone')
    submit = SubmitField('submit')  
    

class AlumniSignin(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    indexnumber = StringField('indexnumber', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    telephone = StringField('phone', validators=[DataRequired()])
    submit = SubmitField('SignUp')  
    
    
    

class Addschool(FlaskForm):
    name= StringField('phone', validators=[DataRequired()])
    submit = SubmitField('SignUp')  
    
class Adddepartment(FlaskForm):
    name= StringField('phone', validators=[DataRequired()])
    school= SelectField('school',  choices=[(('ccsita','ccsita'),('PA','PA'), ('CUBA','CUBA'), ('PHARMACY','PHARMACY'),('NURSING','NURSING'),( 'SADe','SADe'),('FASS','FASS'))], default=None )
    submit = SubmitField('submit')  
    
class Addprogram(FlaskForm):
    name= StringField('phone', validators=[DataRequired()])
    submit = SubmitField('SignUp')  
    
class Addyear(FlaskForm):
    name= StringField('phone', validators=[DataRequired()])
    submit = SubmitField('SignUp')  

class Chatsingle(FlaskForm):
    chatme= StringField('phone', validators=[DataRequired()])
    submit = SubmitField('SignUp')  
