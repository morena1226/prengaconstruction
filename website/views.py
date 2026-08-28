from django.shortcuts import get_object_or_404, render
from .models import Project


def home(request):
    return render(request, 'home.html', {'projects': Project.objects.all()})


def content_page(request, page):
    pages = {
        'services': {
            'title': 'Ndërtim dhe riparim çatie në Durrës',
            'seo_title': 'Ndërtim dhe riparim çatie në Durrës | Prenga Construction',
            'meta_description': 'Ndërtim çatie, riparim çatie, rikonstruksion, hidroizolim dhe punime druri në Durrës dhe në të gjithë Shqipërinë.',
            'eyebrow': 'Çfarë bëjmë',
            'intro': 'Ofrojmë zgjidhje të sigurta dhe afatgjata për çati dhe struktura druri në Durrës, si edhe në zona të tjera të Shqipërisë.',
            'sections': [
                ('Ndërtim çatie', 'Realizojmë çati të reja me strukturë të fortë, materiale cilësore dhe montim profesional, të përshtatura për objektin dhe kushtet e zonës.'),
                ('Riparim çatie', 'Ndërhyjmë për rrjedhje, tjegulla të dëmtuara dhe probleme të strukturës, duke identifikuar shkakun dhe ofruar një zgjidhje të qëndrueshme.'),
                ('Rikonstruksion çatie', 'Rinovojmë çatitë e vjetra duke përforcuar ose zëvendësuar pjesët e konsumuara, me kujdes për sigurinë, izolimin dhe pamjen e objektit.'),
                ('Punime druri', 'Ndërtojmë skelete çatie, streha, pergola, tavane dhe elemente të tjera druri me matje të sakta dhe përfundim cilësor.'),
            ],
        },
        'projects': {
            'title': 'Projektet',
            'seo_title': 'Projekte çatie dhe punime druri | Prenga Construction',
            'meta_description': 'Shikoni projekte të realizuara nga Prenga Construction: çati të reja, riparime çatie, rikonstruksione dhe punime druri në Shqipëri.',
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
            'seo_title': 'Rreth Prenga Construction | Specialistë çatie në Durrës',
            'meta_description': 'Njihuni me Prenga Construction, ekip me mbi 15 vjet përvojë në ndërtim çatie, riparime, rinovime dhe punime druri në Shqipëri.',
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
            'seo_title': 'Kontakt për ndërtim dhe riparim çatie në Durrës',
            'meta_description': 'Kontaktoni Prenga Construction për ofertë dhe këshillim për ndërtim ose riparim çatie, punime druri dhe rinovime në Shqipëri.',
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
