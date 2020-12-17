url = "https://http-api.d7networks.com/send"
querystring = {
"username":"vkhb2089",
"password":"gFHWgOKL",
"from":"Test%20SMS",
"content":"This%20is%20a%20test%20message%20to%20verify%20the%20DLR%20callback",
"dlr-method":"POST",
"dlr-url":"https://4ba60af1.ngrok.io/receive",
"dlr":"yes",
"dlr-level":"3",
"to":"+97150900XXXX"
}
headers = {
'cache-control': "no-cache"
}
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)