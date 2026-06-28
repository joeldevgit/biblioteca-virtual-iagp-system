# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .models import Hero, Servicio, Contador, About, Portfolio, Skill, Testimonio, BlogPost, PartnerLogo, ContactMessage


# def home(request):
#     if request.method == "POST":
#         ContactMessage.objects.create(
#             nombre=request.POST.get("name", ""),
#             email=request.POST.get("email", ""),
#             asunto=request.POST.get("subject", ""),
#             mensaje=request.POST.get("message", ""),
#         )
#         messages.success(request, "Mensaje enviado correctamente.")
#         return redirect("home")

#     context = {
#         "hero": Hero.objects.first(),
#         "servicios": Servicio.objects.filter(activo=True),
#         "contadores": Contador.objects.filter(activo=True),
#         "about": About.objects.first(),
#         "portfolio_items": Portfolio.objects.filter(activo=True),
#         "skills": Skill.objects.filter(activo=True),
#         "testimonios": Testimonio.objects.filter(activo=True),
#         "posts": BlogPost.objects.filter(activo=True)[:3],
#         "partners": PartnerLogo.objects.filter(activo=True),
#     }
#     return render(request, "inicio/index.html", context)




from django.shortcuts import render

def home(request):
    return render(request, "inicio/index.html")