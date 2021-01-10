from django.shortcuts import render


def home(request):
	return render(request, 'home.html')


def reverse(request):
	user_text = request.GET['usertext']
	rever = user_text[: :-1]
	s = user_text.split()
	l = len(s)
	
	return render(request, 'reverse.html', {'text':user_text,'text1':l, 'text2':rever})
