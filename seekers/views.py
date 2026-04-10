from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail

def home(request):
    return render(request, 'index.html')

def hire(request):
    if request.method == 'POST':
        # Extract form details
        company = request.POST.get('company', '')
        contact = request.POST.get('contact', '')
        position = request.POST.get('position', '')
        salary = request.POST.get('salary', '')
        gender = request.POST.get('gender', '')
        qualifications = request.POST.get('qualifications', '')
        location = request.POST.get('location', '')
        
        # Format the message for WhatsApp
        message = "New Hiring Request!\n\n🏢 Company/Store: {}\n📞 Contact: {}\n💼 Position: {}\n💰 Salary: {}\n🚻 Gender: {}\n🎓 Qualifications: {}\n📍 Location: {}".format(company, contact, position, salary, gender, qualifications, location)
        
        # Send via Email
        try:
            send_mail(
                'New Hiring Request',
                message,
                settings.EMAIL_HOST_USER, # From email
                [settings.EMAIL_HOST_USER], # To email
                fail_silently=False,
            )
        except Exception as e:
            print(f"Email failed: {e}")
            
        html_content = f"""
        {{% extends "base.html" %}}
        {{% block content %}}
        <section style="padding:150px 20px; text-align:center; min-height:80vh;">
            <h2 style="color:#d4af37; font-size:2.5rem; margin-bottom:20px;">Submitted Successfully!</h2>
            <p style="color:#e0e0e0; font-size:1.2rem;">Your hiring request has been sent to our team.</p>
            <p style="color:#888; font-size:1rem; margin-top:30px;">Redirecting you back to home...</p>
        </section>
        <script>
            setTimeout(function() {{
                window.location.href = "/";
            }}, 5000);
        </script>
        {{% endblock %}}
        """
        
        from django.template import Template, Context
        t = Template(html_content)
        c = Context({})
        return HttpResponse(t.render(c))
    
    return render(request, 'hire.html')

def job(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        location = request.POST.get('location', '')
        qualification = request.POST.get('qualification', '')
        skills = request.POST.get('skills', '')
        experience = request.POST.get('experience', '')
        pref_location = request.POST.get('pref_location', '')
        
        message_body = "New Job Application!\n\n👤 Full Name: {}\n📧 Email: {}\n📞 Phone: {}\n📍 Current Location: {}\n🎓 Qualification: {}\n💡 Skills: {}\n⏳ Experience: {}\n🏢 Pref. Location: {}".format(
            full_name, email, phone, location, qualification, skills, experience, pref_location)
        
        resume = request.FILES.get('resume')
        screenshot = request.FILES.get('screenshot')
        
        # Send via Email
        try:
            email_msg = EmailMessage(
                'New Job Application',
                message_body,
                settings.EMAIL_HOST_USER, # From email
                [settings.EMAIL_HOST_USER], # To email
            )
            if resume:
                email_msg.attach(resume.name, resume.read(), resume.content_type)
            if screenshot:
                email_msg.attach(screenshot.name, screenshot.read(), screenshot.content_type)
                
            email_msg.send(fail_silently=False)
        except Exception as e:
            print(f"Email failed: {e}")
            
        html_content = f"""
        {{% extends "base.html" %}}
        {{% block content %}}
        <section style="padding:150px 20px; text-align:center; min-height:80vh;">
            <h2 style="color:#d4af37; font-size:2.5rem; margin-bottom:20px;">Application Submitted!</h2>
            <p style="color:#e0e0e0; font-size:1.2rem;">Your application has been sent to our team.We will contact you in 24 Hours</p>
            <p style="color:#888; font-size:1rem; margin-top:30px;">Redirecting you back to home...</p>
        </section>
        <script>
            setTimeout(function() {{
                window.location.href = "/";
            }}, 5000);
        </script>
        {{% endblock %}}
        """
        
        from django.template import Template, Context
        t = Template(html_content)
        c = Context({})
        return HttpResponse(t.render(c))
    
    return render(request, 'job.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message_text = request.POST.get('message', '')
        
        message_body = f"New Contact Message!\n\n👤 Name: {name}\n📧 Email: {email}\n📝 Message: {message_text}"
        
        # Send via Email
        try:
            send_mail(
                'New Contact Message',
                message_body,
                settings.EMAIL_HOST_USER, # From email
                [settings.EMAIL_HOST_USER], # To email
                fail_silently=False,
            )
        except Exception as e:
            print(f"Email failed: {e}")
            
        html_content = f"""
        {{% extends "base.html" %}}
        {{% block content %}}
        <section style="padding:150px 20px; text-align:center; min-height:80vh;">
            <h2 style="color:#d4af37; font-size:2.5rem; margin-bottom:20px;">Message Sent!</h2>
            <p style="color:#e0e0e0; font-size:1.2rem;">Your message has been sent to our team.</p>
            <p style="color:#888; font-size:1rem; margin-top:30px;">Redirecting you back to home...</p>
        </section>
        <script>
            setTimeout(function() {{
                window.location.href = "/";
            }}, 5000);
        </script>
        {{% endblock %}}
        """
        
        from django.template import Template, Context
        t = Template(html_content)
        c = Context({})
        return HttpResponse(t.render(c))

    return render(request, 'contact.html')

from django.core.mail import EmailMessage

def terms(request):
    return render(request, 'terms.html')

def payment(request):
    return render(request, 'payment.html')
