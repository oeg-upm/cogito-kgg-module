from sseclient import SSEClient
import json

messages = SSEClient('http://localhost:8080/sse')
for msg in messages:
    msg.data.split(',')





# {"results":[{"name":{"title":"Miss","first":"Leslie","last":"Davis"},"picture":{"large":"https://randomuser.me/api/portraits/women/1.jpg","medium":"https://randomuser.me/api/portraits/med/women/1.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/women/1.jpg"}}],"info":{"seed":"03ccac7f407cbe35","results":1,"page":1,"version":"1.3"}}