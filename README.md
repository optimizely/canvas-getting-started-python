#Getting Started with Canvas (Python)

##Canvas Overview

Canvas allows developers to easily build integrations on the Optimizely platform. Within a Canvas App, developers can programmatically access information about the current user, including their OAuth token. Developers can build apps that further improve their Optimizely usage or extend functionality. 

* View current Canvas Apps [x].

* Canvas Documentation [x] 

##Demo App

This app simply displays the current status of experiments in a given project. Here we leverage the Canvas Sandbox App[link], which takes an application running on localhost and runs it natively within Optimizely in an iframe. This Sandbox app makes it really easy for developers to build and test applications before formally submitting as a Canvas App. 

![Screenshot](https://github.com/optimizely/canvas-getting-started-python/blob/master/static/img/canvas-screenshot.png)

###Deploying the App
1. Create an Optimizely [Developer Account](https://www.optimizely.com/?modal=devsignup)
2. In your dashboard, click the Apps tab and turn on the Canvas Sandbox app
3. Clone repo locally.
4. Install requirements: `pip install -r requirements.txt`
5. Run the app locally: `python application.py`
6. View the app from within the Canvas Sandbox app
7. Lastly, enable "Load unsafe scripts". [Screenshot](https://github.com/optimizely/canvas-getting-started-python/blob/master/static/img/unsafe-scripts.png) 

**Please note:** We publicly exposed the Client Secret for use with the Canvas Sandbox App because this app will only run content on localhost within Optimizely, which does not present a security risk. <b> Normally</b> you would not want to share your Client Secret publicly. 

### Building the App

Instead of registering our Canvas app with Optimizely, we will develop this app using the Canvas Sandbox app. Each Canvas app points to a hosted application that becomes embedded in the Optimizely dashboard as an iframe. This Sandbox app, simply loads applications running on localhost (port 4001.) in the iframe. By leveraging Canvas, developers don’t have to manage the OAuth process, as Canvas conveniently provides context on the current user. Developers are provided with the user’s context through decoding the `signed_request`. Once decoded:
```
{"context":
    {"user":
        {"email": "jon@optimizely.com"},
     "environment":
         {"current_account": 123456,
          "current_project": 78910},
     "client":
         {"access_token": "abcdefg1234543",
          "token_type": "bearer",
          "expires_in": 7200}
    }
}
```
To learn more about the decoding process read the “Verifying the Context”[link]. In this app, I used the Canvas Python SDK[link] to handle the decoding. 

```
user_info = optimizely_canvas_sdk.extract_user_context(signed_request, CLIENT_SECRET)
``` 
After successfully decoding, we leverage the access_token to issue requests on the user’s behalf. In this app, I use the Python client library[link] to make API calls. I make a call to query for all the user’s experiments given the current project_id. Use the client it looks like this:

`experiments = client.Projects.get(current_project_id).experiments()`

We then iterate through each experiment and cache the experiment status. The front-end then renders these results. 

### Next Steps

Currently, this app works locally and is available for testing through the Canvas Sandbox app. If you would like to publish your app for the Optimizely community, please follow these steps: http://developers.optimizely.com/canvas/#register-your-app. [link]


## Getting Help

* Canvas app ideas (Community Driven): link 
* Canvas Documentation: link
* Questions? Shoot us an email: developers@optimizely.com

