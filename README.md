#Getting Started with Canvas (Python)

##Canvas Overview

Canvas allows developers to easily build integrations on the Optimizely platform. Within a Canvas App, developers can programmatically access information about the current user, including their OAuth token. Developers can build apps that further improve their Optimizely usage or extend functionality. 

Check out the apps that have already been built [x].

Read the Canvas Documentation [x] 

##Demo App

This app simply displays the current status of experiments in a given project. Here we leverage the Canvas Sandbox App, which takes an application running on localhost and runs it natively within Optimizely in an iframe. This Sandbox app makes it really easy for developers to build and test applications before formally submitting as a Canvas App. 

[screenshot]

###Deploying the App
1. Create an Optimizely Developer Account [link x]
2. In the app dashboard[link x], click Apps and turn on Canvas Sandbox [screenshot]
3. Clone repo into a local directory.
4. Install requirements: `pip install -r requirements.txt`
5. Run the app locally: `python application py`
6. View the app from within the Canvas Tab
7. Load unsafe scripts [screenshot] 

**Please note:** We publicly exposed the Client Secret for use with the Canvas Sandbox App because this app will only run content on localhost within Optimizely, which does not present a security risk. <b> Normally</b> you would not want to share your Client Secret publicly. 

### Building the App

Instead of registering a Canvas app with Optimizely we will develop this app using the Canvas Sandbox app.Each Canvas app points to a hosted application that becomes embedded into the Optimizely dashboard as iframes. By leveraging Canvas, developers don’t have to manage the OAuth process, as Canvas provides context on the current user. Developers are provided with the user’s context through decoding the `signed_request`. Once decoded:
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
To learn more about the decoding process read the “Verifying the Context” [link]. In this app, I used the Canvas Python SDK to handle the decoding. 

```
user_info = optimizely_canvas_sdk.extract_user_context(signed_request, CLIENT_SECRET)
``` 
After successfully decoding, we leverage the access_token to issue requests on the user’s behalf. In this app, I use the Python client library[link] to make API calls. I make a call to query for all the user’s experiments given the current project_id. Use the client it looks like this:

`experiments = client.Projects.get(current_project_id).experiments()`

We then iterate through each experiment and cache the experiment status. The front-end then renders these results. 


### Next Steps

Currently, this app only works locally and is available through the Canvas sandbox app. If you would like to publish for the Optimizely community, please follow these steps. <steps>  


## Need Help

* Canvas app ideas (Community Driven): link 
* Canvas Documentation: link
* Questions? Shoot us an email: developers@optimizely.com

