# Optimizely Python Canvas Package
# Authors: 
# Becca Bruggman <rebecca@optimizely.com>
# Jon Gaulding <jon@optimizely.com>

import base64
import hashlib
import hmac
import json
import os
import urllib

class OptimizelyCanvasValidationError(Exception):
  pass

def _decode_context(unhashed_context):
  return json.loads(base64.b64decode(unhashed_context))

def _validate_context(hashed_context, unhashed_context, optimizely_oauth_client_secret):
  hashed_context=urllib.unquote(hashed_context).decode('utf8') 

  re_hashed_context = base64.b64encode(hmac.new(optimizely_oauth_client_secret, unhashed_context, hashlib.sha256).hexdigest())

  if hashed_context != re_hashed_context:
    raise OptimizelyCanvasValidationError()

def extract_user_context(signed_request, optimizely_oauth_client_secret):
    hashed_context, unhashed_context = signed_request.split('.')
    try:
	  _validate_context(hashed_context, unhashed_context, optimizely_oauth_client_secret)
	  return _decode_context(unhashed_context)
    except OptimizelyCanvasValidationError:
	  raise OptimizelyCanvasValidationError("Error: Request not properly signed")

 

 

  






