from django.shortcuts import render, redirect
from Student.forms import UpdateProgressForm
from Student.models import Student, Major
from Accounts.models import Account


def onboarding_step1(request):
    user = request.user
    print(user.has_university)
    student_user = Account.objects.filter(pk=request.user.pk)
    user_id = student_user.model.get_user_id(self=user)

    if user.is_active and user.has_university == True:
        if request.method == 'POST':
            progress = request.POST['progress']
            student_model = Student.objects.get(user_id_number=user_id)
            if student_model.course_progress < progress:
                student_model.course_progress = progress
                student_model.save()
                return redirect('/university/onboarding/step2')
            else:
                return redirect('/university/onboarding/step2')

        return render(request, 'Students/onboarding/step1.html')
    else:
        return render(request, 'MainWebsite/index.html')



def onboarding_step2(request):
    user = request.user
    student_user = Account.objects.filter(pk=request.user.pk)
    user_id = student_user.model.get_user_id(self=user)
    student_model = Student.objects.get(user_id_number=user_id)

    if user.is_active and user.has_university == True:
        if request.method == 'POST':
            progress = request.POST['progress']
            if student_model.course_progress < progress:
                student_model.course_progress = progress
                student_model.save()
                return redirect('/university/onboarding/step3')
            else:
                return redirect('/university/onboarding/step3')

        return render(request, 'Students/onboarding/step2.html')
    else:
        return render(request, 'MainWebsite/index.html')




def onboarding_step3(request):
    user = request.user
    majors = Major.objects.all()
    student_user = Account.objects.filter(pk=request.user.pk)
    user_id = student_user.model.get_user_id(self=user)
    student_model = Student.objects.get(user_id_number=user_id)

    if user.is_active and user.has_university == True:
        if request.method == 'POST':
            print(request.POST)
            post_data = request.POST
            progress = post_data['progress']
            first_name = post_data['first-name']
            last_name = post_data['last-name']
            age = post_data['age']
            gender = post_data['gender']
            ethnicity = post_data['ethnicity']
            student_major = post_data['major']
            student_model.first_name = first_name
            student_model.last_name = last_name
            student_model.age = age
            student_model.gender = gender
            student_model.ethnicity = ethnicity
            student_model.major = Major.objects.get(major_title=student_major)


            student_model.save()

            if student_model.course_progress < progress:
                student_model.course_progress = progress
                student_model.save()
                return redirect('/university/onboarding/step4')
            else:
                return redirect('/university/onboarding/step4')

        first_name = student_model.first_name
        last_name = student_model.last_name
        age = student_model.age
        gender = student_model.gender
        ethnicity = student_model.ethnicity
        major = student_model.major
        genderChoices = Student.GENDER_CHOICES
        ethnicityChoices = Student.ETHNICITY_CHOICES

        context = {
            'first_name': first_name,
            'last_name': last_name,
            'age': age,
            'gender': gender,
            'ethnicity': ethnicity,
            'majors': majors,
            'maj': major,
            'genderChoices': genderChoices,
            'ethnicityChoices': ethnicityChoices

        }

        return render(request, 'Students/onboarding/step3.html', context=context)
    else:
        return render(request, 'MainWebsite/index.html')




def onboarding_step4(request):
    user = request.user
    student_user = Account.objects.filter(pk=request.user.pk)
    user_id = student_user.model.get_user_id(self=user)
    student_model = Student.objects.get(user_id_number=user_id)

    if user.is_active and user.has_university == True:
        if request.method == 'POST':
            print(request.POST)
            progress = request.POST['progress']
            if student_model.course_progress < progress:
                student_model.course_progress = progress
                student_model.save()
                return redirect('/university/dashboard')
            else:
                return redirect('/university/dashboard')

        return render(request, 'Students/onboarding/step4.html')
    else:
        return render(request, 'MainWebsite/index.html')


