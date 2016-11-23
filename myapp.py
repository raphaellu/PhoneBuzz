from flask import *
from twilio.rest import TwilioRestClient
import twilio.twiml
from twilio.util import RequestValidator
import time
from time import strftime, localtime
from database import db, Call

account_sid = "AC603bdae185464326b59f75982befc9c5" # Your Account SID from www.twilio.com/console
auth_token  = "65a6f6eb6b11237fbdb9c073b8ea4b99"  # Your Auth Token from www.twilio.com/console
client = TwilioRestClient(account_sid, auth_token)
validator = RequestValidator(auth_token)
mysite = "http://phonebuzz-phase1-lelu.herokuapp.com/" # phase 1 site to handle phoneBuzz call
# The X-Twilio-Signature header attached to the request
twilio_signature = 'RSOYDt4T1cUTdK1PDd93/VVr8B8='
app = Flask(__name__)

curr_call = Call('', 0, 0, '') # create new Call entry
all_calls = Call.query.all() # a list of all history calls

# below is for phase 2 & 3:
@app.route('/')
def index():
    return render_template('index.html', all_calls=all_calls)

@app.route('/outbound_call', methods=['GET','POST'])
def outbound_call():
    global curr_call
    num = validate_num(request.form['phoneNum'])
    hours = request.form['hours']
    minutes = request.form['minutes']
    seconds = request.form['seconds']
    # if num is not valid, raise error msg
    if (num == -1):
        return render_template('index.html', status=-1, message="Please enter a valid number : +1XXXXXXXXXX", all_calls=all_calls)
    
    sleep_time = validate_time(hours, minutes, seconds)
    time.sleep(sleep_time);
    call = client.calls.create(to=num, 
                           from_="+12565308617", 
                           url=mysite+"phonebuzz")
    # assign info to current call (preparing for adding into database)
    curr_call.phone = num
    curr_call.delay = int(sleep_time) # sleeping time is definitely an int, validated by HTML5 
    curr_call.time = strftime("%Y-%m-%d %H:%M:%S", localtime())
    return render_template('index.html', status=1, message="A call to "+num + " has been sent.", all_calls=all_calls)

# validate sleeping time
# HTML5 validates numbers and this function converts strings to floats and return in seconds
def validate_time(h, m, s):
    if (h == '' or float(h) < 0): h = 0
    if (m == '' or float(m) < 0): m = 0
    if (s == '' or float(m) < 0): s = 0
    return float( float(h) * 3600 + float(m) * 60 + float(s))
# validate if a phone number is valid
def validate_num(str):
    # missing country code
    if str[0:2] != '+1' and len(str) == 10:
        return "+1"+str
    # correctly formated    
    elif str[0:2] == '+1' and len(str) == 12:
        return str
    # other cases return error
    else:
        return -1

# below is for phase 1 

@app.route('/phonebuzz', methods=['GET','POST'])
def phonebuzz():
    resp = twilio.twiml.Response()
    # ask user to enter a num for game
    with resp.gather(action="/handle_input", method="POST", timeout=10) as g:
        g.say("Please enter a number to start fizz buzz game, followed by the pound sign.")
    return str(resp)

@app.route('/handle_input', methods=['GET','POST'])    
def handle_input():
    global curr_call
    nm = request.values.get('Digits', '')
    resp = twilio.twiml.Response()
    if nm.isdigit():  # if input is valid
        res = generate_phonebuzz(int(nm))
        if (res == -1): # if the number is too large, ask for re-entering the num
            resp.say("You entered a very large number, why don't we try a smaller one ?")
            resp.redirect("/phonebuzz")
        else: 
            resp.say(", ".join(res) + ",,,,Game finished. Goodbye!")
    else: # if input is invalid, ask for re-entering the num
        resp.say("You did not enter a valid number.")
        resp.redirect("/phonebuzz")
    curr_call.number = int(nm)
    db.session.add(curr_call) # add curr call into database
    db.session.commit()
    all_calls = Call.query.all() # update the list of all history calls
    return str(resp)

    
def generate_phonebuzz(nm):
    if (nm >= 1000) :
        return -1
    res = []
    for i in range(1, nm+1):
        if (i % 5 == 0 and i % 3 == 0): res.append("Fizz Buzz")
        elif (i % 5 == 0): res.append("Buzz")
        elif (i % 3 == 0): res.append("Fizz")
        else : res.append(str(i))    
    return res
