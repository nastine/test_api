import os
from django.conf import settings
from annoying.decorators import ajax_request
from datetime import datetime

@ajax_request
def json_images(request):
    path = os.path.join(settings.MEDIA_ROOT)
    data = []
    for f in os.listdir(path):
        d = {}
        d['name'] = f.title()
        d['type'] = 'file' if os.path.isfile(path+'/'+str(f)) else 'directory'
        d['date'] = datetime.fromtimestamp(os.path.getmtime(path+'/'+str(f))).strftime('%Y-%m-%d %H:%M:%S')
        data.append(d)
    return {'data': data}

