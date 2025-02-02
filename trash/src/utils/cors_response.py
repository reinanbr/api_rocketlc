def response_in_cors(body):
    return     {'statusCode': 200,
    'headers': {
  "Access-Control-Allow-Origin": "*", #Required for CORS support to work
  "Access-Control-Allow-Credentials": True, #// Required for cookies, authorization headers with HTTPS
  "Access-Control-Allow-Headers": "Origin,Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token,locale",
  "Access-Control-Allow-Methods": "POST, OPTIONS"
},'body':body}