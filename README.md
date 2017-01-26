# DontLoseHope
-- This application is really cool. Work of 36 hours without any sleep. It allows you to submit a photo of someone you have lost(For example a kid in a adventure park). There by training a artifical nueral network. Once there is a match it sends you a text on your phone along with the contact details of the person who has found the one you have lost.

-- The best part of using a NN is that it doesnt require the person to be wearing the same cloths, having the same hairstyle(etc). Facial Recognition is a vast area of research and this projects shows the utilization of it using a working prototype built in 36 hours in submitted to SwapHAcks 2017.


## Running the application

--You would need to get a client key from clarifai https://developer.clarifai.com/ and type ```clarifai config``` with they keys and secret. 
-- you would need to add TWilio and Imgur  client Key in the code too. The twilio key would be needed to added in __init__.py and the Imgur key would be needed to be added in the javascript file(its in the AJAX call).
-- Install the dependencies and then just run ```python __init__.py```

## Working of the application
Flask is used to create a REST'full web server. JavaScript BootSrap for the front end. CLarifai, IMGUR and TWilio API's are used for their respective funcitonality. 


## Contact
--You can email me at devyashsanghai@gmail.com if you need any help and this in hurry documention is too much for you :P
