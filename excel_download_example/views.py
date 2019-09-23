from django.http import HttpResponse
from django.template import loader
import csv

def index(request):
    template = loader.get_template('excel_download_example/index.html')
    default_data = {'hello':'world'}
    return HttpResponse(template.render(context=default_data, request=request))


def endpoint(request):
    if request.is_ajax():
        with open('templates/excel_download_example/temp/some_csv.csv', 'w+') as input_file:
            writer = csv.writer(input_file)
            for key,value in dict(request.GET).items():
                writer.writerow([key, value])

    data = open('templates/excel_download_example/temp/some_csv.csv','r').read()
    response = HttpResponse(data, content_type='application/x-download')
    response['Content-Disposition'] = 'attachment;filename=data.csv'

    return response
