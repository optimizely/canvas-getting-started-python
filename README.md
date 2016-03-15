#Getting Started with Canvas (Python)

##Canvas Overview

Canvas allows developers to easily build integrations on the Optimizely platform. Within a Canvas App, developers can programmatically access information about the current user with the user’s OAuth token. Developers can build apps that further improve their Optimizely usage or extend functionality. 

* View current Canvas Apps in the Apps Tabs in your [dashboard](https://app.optimizely.com).

* Canvas [Developer Guide](http://developers.optimizely.com/apps/).

##Demo App

We’ve created a demo app that shows you:

1. How to decode the Canvas `signed_request` to get the user’s access token.
2. How to use that access token to leverage the Optimizely REST API.
3. How to use [Optimizely User Interface (OUI)](https://github.com/optimizely/oui) to style your app so that it looks right at home in the Optimizely platform, which is required in the design guidelines. 

The app simply displays the current status of experiments in the user’s project. 

Using the instructions below, you can run the app locally as an iframe within Optimizely, and use it as a starting point for your own project. The possibilities are endless! 

![Screenshot](https://github.com/optimizely/canvas-getting-started-python/blob/master/static/img/canvas-screenshot.png)

###Deploying the App
1. Login to or create an Optimizely [Developer Account](https://www.optimizely.com/?modal=devsignup).
2. In your dashboard, click the Apps tab and turn on the 'Your Canvas Sandbox' app.
3. Clone this repo locally.
4. Install requirements: `pip install -r requirements.txt`.
5. Run the app locally: `python application.py`.
6. View the app by clicking on the Your Canvas Sandbox tab from the Optimizely dashboard.
7. Enable "Load unsafe scripts" by clicking the grey shield on the right hand side of your address bar.  [Screenshot](https://github.com/optimizely/canvas-getting-started-python/blob/master/static/img/unsafe-scripts.png) (Your browser will try to prevent the iframe from loading because the Optimizely app is on https, while your Canvas Sandbox app is on http). 

**Please note:** We publicly exposed the Client Secret for use with the Canvas Sandbox App because this app will only run content on localhost within Optimizely, which does not present a security risk. <b> Normally</b> you would not want to share your Client Secret publicly. 

### Building the App

Each Canvas app points to a hosted web application external to Optimizely that's embedded in the Optimizely dashboard as an iframe. The iframe URL includes a `signed_request` parameter, which needs to be decoded. Using the `signed_request` parameter, you can extract information about the user, as well as their `access_token` so you can start using the REST API on their behalf. 

To learn more about the decoding process read the [“Verifying the Context”](http://developers.optimizely.com/apps/#verifying-the-context). In this app, I used the [Canvas Python SDK](https://github.com/optimizely/canvas_python_SDK) to handle the decoding. 

```
user_info = optimizely_canvas_sdk.extract_user_context(signed_request, CLIENT_SECRET)
``` 
After successfully decoding, we leverage the access_token to issue requests on the user’s behalf. In this app, I use Optimizely’s Python client library[link] to make API calls. I make a call to query for all the user’s experiments given the current `project_id`:

`experiments = client.Projects.get(current_project_id).experiments()`

We then iterate through each experiment and cache the experiment status. The front-end then renders these results. 

### Next Steps

You can use the Canvas Sandbox as a starting point for your own app. If you are interested in having your application included within the Optimizely App Marketplace, please follow the [guidelines](http://developers.optimizely.com/apps/#app-guidelines) to make sure your app is ready for the review process and please follow these [steps](http://developers.optimizely.com/canvas/#register-your-app): 

## Join the Canvas Community! 

* [App ideas](http://optimize.ly/app-ideas) (Community Driven) 
* Apps Developer Guide: http://developers.optimizely.com/apps
* Questions? Shoot us an email: developers@optimizely.com or use [Gitter](https://gitter.im/optimizely/apps)!
