import dbcreds
import dbhelper
import uuid
from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

@app.post('/api/client')
def new_client():
    try:
        error = dbhelper.check_endpoint_info(request.json,["username","email","password","image_url","bio"])
        # if it has req info "username","email","password","image_url","bio" then returns none
        if(error != None):
            return make_response(jsonify(error),400)
        results = dbhelper.run_procedure('call new_client(?,?,?,?,?)',
                [request.json.get("username"),request.json.get("email"),request.json.get("password"),request.json.get("image_url"),request.json.get("bio")])
        # if results come back as a list jsonify results
        if(type(results) == list):
            return make_response(jsonify(results),200)
        else:
            return make_response('sorry something went wrong',500)
    # some except blocks with possible errors
    except TypeError:
        print('invalid input type, try again.')
    except UnboundLocalError:
        print('coding error')
    except ValueError:
        print('value error, try again')   

@app.post('/api/login')
def login():
    try:
        error = dbhelper.check_endpoint_info(request.json,["username","password"])
        # if it has req info "username","password" then returns none
        if(error != None):
            return make_response(jsonify(error),400)
        token = uuid.uuid4().hex
        results = dbhelper.run_procedure('call login(?,?,?)',
                [request.json.get("username"),request.json.get("password"),token])
        # if results come back as a list jsonify results
        if(type(results) == list):
            return make_response(jsonify(results),200)         
        else:
            return make_response('sorry something went wrong',500)
    # some except blocks with possible errors
    except TypeError:
        print('invalid input type, try again.')
    except UnboundLocalError:
        print('coding error')
    except ValueError:
        print('value error, try again')   

@app.delete('/api/login')
def delete_token():
    try:
        error = dbhelper.check_endpoint_info(request.json,["token"])
        # if it has req info "token" then returns none
        if(error != None):
            return make_response(jsonify(error),400)
        results = dbhelper.run_procedure('call delete_token(?)',[request.json.get("token")])
        # if results come back as a None make response with success message results
        if(results == None):
            return make_response('deletion successful',200)
        else:
            return make_response('sorry something went wrong',500)
    # some except blocks with possible errors
    except TypeError:
        print('invalid input type, try again.')
    except UnboundLocalError:
        print('coding error')
    except ValueError:
        print('value error, try again') 


@app.get('/api/client')
def get_profile():
    try:
        error = dbhelper.check_endpoint_info(request.args,["token"])
        # if it has req info "token" then returns none
        if(error != None):
            return make_response(jsonify(error),400)
        results = dbhelper.run_procedure('call get_profile(?)',[request.args.get("token")])
        # if results come back as a list jsonify results
        if(type(results) == list):
            return make_response(jsonify(results),200)
        else:
            return make_response('sorry something went wrong',500)
    # some except blocks with possible errors
    except TypeError:
        print('invalid input type, try again.')
    except UnboundLocalError:
        print('coding error')
    except ValueError:
        print('value error, try again')  






if(dbcreds.production_mode == True):
    print("Running Production Mode")
    import bjoern #type: ignore
    bjoern.run(app,"0.0.0.0",5194)
else:
    from flask_cors import CORS
    CORS(app)
    print("Running in Testing Mode")
    app.run(debug=True)