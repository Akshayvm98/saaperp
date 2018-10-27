from django.shortcuts import render ,get_object_or_404, redirect, HttpResponse, HttpResponseRedirect
from schoolerp.models import Profile, Classroom, Student, Subject, Exam, Test, Score
import math
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout


	
def home(request):
	return render(request,'home.html')

def signin(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			return render(request, "home.html")

	return render(request, "signin.html")	

def signup(request):
	if request.method=="POST":
		username=request.POST.get('username')
		password=request.POST.get('password')
		email=request.POST.get('email')
		firstname=request.POST.get('firstname')
		lastname=request.POST.get('lastname')

		
		user = User.objects.filter(username=username).exists()
		print(user)
		if user:
			return HttpResponse("Please Check the Info, User might already exist.")
		else:
			user = User.objects.create_user(username=username, email=email, password=password)
			return render(request, 'signin.html')
	return render(request, "signup.html")

def signout(request):
	logout(request)
	return render(request, "home.html")

def dashboard(request):
	teacher=request.user
	class_rooms = Classroom.objects.filter(classteacher=teacher.profile)
	# print(class_rooms.id)
	return render(request, "dashboard.html", {'classrooms':class_rooms})

def classroom(request,pk):
	cr = Classroom.objects.get(pk=pk)
	students=Student.objects.filter(classroom=cr)
	return render(request, "classroom.html", {'students':students})

def exam(request):
	teacher=request.user
	class_rooms = Classroom.objects.filter(classteacher=teacher.profile)
	if request.method == "POST":
		examname=request.POST.get('examname')
		cid=int(request.POST.get('classroom'))
		classroom = Classroom.objects.get(pk=cid)
		Exam.objects.create(examname=examname, classroom=classroom)
		return redirect('/exam/')
	return render(request, 'exam.html',{'classrooms':class_rooms})

def test(request):
	subject=Subject.objects.all()
	profile=Profile.objects.filter(profession="TEACHER")
	
	exam=Exam.objects.all()
	class_rooms=Classroom.objects.all()
	if request.method == "POST":
		sid=int(request.POST.get('subject'))
		subject=Subject.objects.get(pk=sid)
		duration=request.POST.get('duration')
		eid=int(request.POST.get('examname'))
		examname=Exam.objects.get(pk=eid)
		
		cid=int(request.POST.get('classroom'))
		classroom = Classroom.objects.get(pk=cid)
		maxmarks=request.POST.get('maxmarks')
		vid=request.POST.get('evaluatedby')
		evaluatedby=Profile.objects.get(pk=vid)
		print(type(vid))
		
		Test.objects.create(exam=examname,classroom=classroom, subject=subject, 
							maxmarks=maxmarks, duration=duration, evaluatedby=evaluatedby )
		
		return redirect('/test/')
	return render(request, "test.html",{'subject':subject,'exam':exam,'profile':profile,
										'classrooms':class_rooms})

def score(request):
	exam=Exam.objects.all()
	subject=Subject.objects.all()
	teacher=request.user
	class_rooms = Classroom.objects.filter(classteacher=teacher.profile)
	cr = Classroom.objects.all()
	students=Student.objects.all()

	if request.method == "POST":
		eid=int(request.POST.get('exam'))
		exam=Exam.objects.get(pk=eid)

		tid=int(request.POST.get('test'))
		test=Test.objects.get(pk=tid)
		
		sid=int(request.POST.get('student'))
		student=Test.objects.get(pk=sid)
		cid=int(request.POST.get('score'))
		score=Test.objects.get(pk=cid)

		Score.objects.create(exam=exam, test=test,student=student,score=score,classroom=classroom)
		return redirect('/score/')
	return render(request, "score.html",{'exam':exam,'subject':subject,'classrooms':class_rooms,'students':students})









































































# def index(request):
# 	enteries=teachermark.objects.all()
# 	return render(request,'index.html')

# def home(request):
# 	return render(request,'home.html')

# def viewmarks(request):
# 	return render(request,'viewmarks.html')

# def studentdetails(request):
# 	return render(request,'studentdetails.html')

# def studentmarks(request):
# 	if request.method=="POST":
# 		name_of_the_test=request.POST.get('name_of_the_test')
# 		rollnumber = request.POST.get('rollnumber')
# 		studentname = request.POST.get('studentname')
# 		obtainedmarks=request.POST.get('omarks')
# 		maxtestmarks = request.POST.get('maxtestmarks')
		
# 		teachermark.objects.create(name=name)

# 	return render(request,'studentmarks.html')			

# def details(request,pk):
# 	entry=get_object_or_404(teachermark,pk=pk)
# 	return render(request,'templates/marksentry.html',{'entry':entry})
