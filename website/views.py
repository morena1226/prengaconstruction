from django.shortcuts import get_object_or_404, render
from .models import Project


def home(request):
    return render(request, 'home.html', {'projects': Project.objects.all()})


def content_page(request, page):
    pages = {
        'services': {
            'title': 'Shërbimet',
            'eyebrow': 'Çfarë bëjmë',
            'intro': 'Zgjidhje të plota për çati, punime druri, rinovime dhe mirëmbajtje.',
            'sections': [
                ('Çati', 'Ndërtim, rinovim dhe riparim me materiale të qëndrueshme dhe montim profesional.'),
                ('Punime druri', 'Struktura, korniza, panelime dhe elemente dekorative të realizuara me precizion.'),
                ('Rinovim dhe riparime', 'Modernizim i banesave dhe ndërhyrje të shpejta për çdo problem të çatisë ose strukturës.'),
                ('Izolim dhe mirëmbajtje', 'Mbrojtje termike dhe hidroizolim, së bashku me kontrolle periodike për jetëgjatësi.'),
            ],
        },
        'projects': {
            'title': 'Projektet',
            'eyebrow': 'Punimet tona',
            'intro': 'Disa nga punimet e realizuara nga ekipi i Prenga Construction.',
            'sections': [
                ('Çati e re', 'Strukturë solide, mbrojtje e plotë dhe përfundim profesional.'),
                ('Detaje druri', 'Elemente druri me estetikë moderne dhe rezistencë të lartë.'),
                ('Rinovim banese', 'Zgjidhje të personalizuara që i japin objektit pamje dhe funksion të ri.'),
                ('Strukturë druri', 'Dru i përzgjedhur dhe montim i saktë për një çati të sigurt.'),
            ],
        },
        'about': {
            'title': 'Rreth nesh',
            'eyebrow': 'Prenga Construction',
            'intro': 'Punojmë me përkushtim për të ndërtuar hapësira të sigurta, të qëndrueshme dhe të bukura.',
            'sections': [
                ('Eksperiencë', 'Mbi 15 vjet përvojë në çati, punime druri, rinovime dhe riparime.'),
                ('Cilësi', 'Përdorim materiale të garantuara dhe i kushtojmë rëndësi çdo detaji të punimit.'),
                ('Besueshmëri', 'Planifikim i qartë, komunikim i drejtpërdrejtë dhe respektim i afateve të dakordësuara.'),
            ],
        },
        'contact': {
            'title': 'Kontakt',
            'eyebrow': 'Flasim për projektin tuaj',
            'intro': 'Na kontaktoni për një vlerësim dhe këshillim të përshtatur për nevojat tuaja.',
            'sections': [
                ('Telefon', '0693345460'),
                ('Email', 'pprenga179@gmail.com'),
                ('Lokacioni', 'Durrës, Shqipëri. Marrim punime edhe jashtë Durrësit.'),
            ],
        },
    }
    context = pages[page]
    if page == 'projects':
        context = {**context, 'projects': Project.objects.all()}
    return render(request, 'content_page.html', context)


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})
