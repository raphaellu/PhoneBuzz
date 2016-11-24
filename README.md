# PhoneBuzz
PhoneBuzz is an implementation of FizzBuzz over the phone. For those unfamiliar with the game of FizzBuzz, it works like this:

Players generally sit in a circle. The player designated to go first says the number "1", and each player thenceforth counts one number in turn. However, any number divisible by three is replaced by the word fizz and any divisible by five by the word buzz . Numbers divisible by both become fizz buzz.

A typical round of fizz buzz is as follows: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, Fizz Buzz, 31, 32, Fizz, 34, Buzz, Fizz, ...

* [Github - Final Source code](https://github.com/raphaellu/PhoneBuzz) 

## Powered by
* Twilio
* Flask
* Heroku
* Flask-SQLAlchemy
* PostgreSQL


## Phase 1
For phase 1, you will be able to point a Twilio phone # at my web app and be able to play FizzBuzz via the phone.

* [Github - Source code for phase 1](https://github.com/raphaellu/PhoneBuzz-phase1)

#### If you want a quick glance:
1. Simply call +1(256) 530-8617 to start the game!

#### If you have a Twilio phone #:
1. Please point your Twilio phone # to the web app: [http://phonebuzz-phase1-lelu.herokuapp.com/phonebuzz](http://phonebuzz-phase1-lelu.herokuapp.com/phonebuzz) 
2. Please select **HTTP POST** for http request type
3. call your Twilio phone # to start the game

## Phase 2
Augmented web application that provides an interface which allows a user to initiate an outbound phone call to a # to play PhoneBuzz as in phase 1.
This is powered by the Twilio API.

* [Github - Source code for phase 2](https://github.com/raphaellu/PhoneBuzz-phase2) 
* Link to Web Application: [http://phonebuzz-phase2-lelu.herokuapp.com/](http://phonebuzz-phase2-lelu.herokuapp.com/)

## Phase 3 & 4

* [Github - Source code for phase 3 & 4](https://github.com/raphaellu/PhoneBuzz) 

### Phase 3

Similar to the simple FizzBuzz challenge, but with an optional delay to the phone call. User will be able to enter the delay time before requesting a call. 

**Currently it only handles delay that is less than 30s*

* Link to Web Application: [http://phonebuzz-phase3-lelu.herokuapp.com/](http://phonebuzz-phase3-lelu.herokuapp.com/)

### Phase 4

A storage system is added to the application. A history of PhoneBuzz calls made will show below the inputs on the home page and users can replay history calls. 

* Link to Web Application: [http://phonebuzz-phase4-lelu.herokuapp.com/](http://phonebuzz-phase3-lelu.herokuapp.com/)


