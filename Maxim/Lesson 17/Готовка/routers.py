from chat.message_views import getMessage, sendMessage

routes = [
    ('GET', '/', getMessage,  'getmsg'),
    ('POST', '/message', sendMessage,  'sendmsg'),
]