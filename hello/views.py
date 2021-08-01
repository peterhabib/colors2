from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})




from django.shortcuts import render
import csv, io
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from .models import Data

# Create your views here.
def home(request):
    return render(request,'index.html')



def patient(request):
    return render(request,'./creative/patient.html')



@permission_required('admin.can_add_log_entry')
def data_upload(request):
    templates = "data_upload.html"

    prompt = {
        'order': 'Order of the CSV should be Name, Age, Email, Adress'
    }

    if request.method == "GET":
        return render(request,templates, prompt)


    csv_file = request.FILES['file']


    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Data.objects.update_or_create(
            Name=column[0],
            Age = column[1],
            Email = column[2],
            Adress = column[3],
        )

    context = {}
    return render(request, templates, context)
