# vinocave
L'application de gestion de cave en Django

## Installation des prérequis
### Virtualenv
* [Sous Windows](https://pymote.readthedocs.io/en/latest/install/windows_virtualenv.html)
* [Sous Linux](https://virtualenv.pypa.io/en/stable/installation/)



## Comment on en est-on arrivé là ?
### Démarrer le projet
Étapes pour recréer un projet à partir de zéro, pas nécessaires, sauf pour recommencer.

```
$ virtualenv env
$ . env/bin/activate
(env)$ pip install django
(env)$ django-admin startproject vinocave
(env)$ cd vinocave
(env)$ python manage.py startapp core
```

Après édition de core/models.py

```
(env)$ python manage.py migrate
(env)$ python manage.py createsuperuser
(env)$ python manage.py runserver
```

On peut naviguer à présent à l'adresse http://127.0.0.1:8000/admin/ pour se connecter et commencer à jouer avec le modèle.

### Ajouter les premières vues (atelier du 7/07)
* [Inspiration : tutoriel Django](https://docs.djangoproject.com/fr/1.11/intro/tutorial01/)

On crée donc nos vues dans le fichier core/views.py :

```
from django.http import HttpResponse


def youhou(request):
    return HttpResponse("Youhou !!")

def index(request):
    return HttpResponse("Index")

def liste(request):
    return HttpResponse("Liste")
```

On rajoute ensuite le "routage" des requètes pour qu'elles parviennent à ces vues:
Dans vinocave/urls.py
```
url(r'^youhou/?', views.youhou, name='youhou'), #routage direct
url(r'^vins/', include('core.urls')), #routage indirect via core.urls
```

Et dans code/urls.py

```
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^liste$', views.liste, name='liste'),
]

```

On a donc l'exemple de deux stratégies différentes:
* Le routage direct (mauvaise pratique), qui consiste à rediriger directement la requète du niveau projet à la vue (vue "youhou" http://127.0.0.1:8000/youhou/ )
* Le routage indirect, par un niveau de routage intermédiaire via l'application "core" (vues "index" http://127.0.0.1:8000/vins et "liste" http://127.0.0.1:8000/vins/liste)

### Jouer avec le contrôleur (atelier du 7/07)
Si l'on rajoute la ligne suivante dans core/views.py:
```
from core.models import Vin
```
On peut maintenant jouer avec les objets en base de données par l'utilisation du "contrôleur", qui est la propriété "objects" de "Vin". Par exemple:
```
Vin.objects.count() #retourne le nombre de bouteilles en bdd
```

### Modifier le modèle de données (atelier du 13/07)
On rajoute la définition de la classe Bouteille dans core/models.py:

```
class Bouteille(models.Model):
    prix = models.DecimalField(_("prix"), max_digits=6, decimal_places=2, blank=True,
        help_text=_("Prix unitaire"))
    contenance = models.DecimalField(_("contenance"), max_digits=4, decimal_places=1, blank=True,
        help_text=_("contenance"))
    provenance = models.CharField(_("provenance"), max_length=255, blank=True,
        help_text=_("provenance de la bouteille"))
    #etiquette = models.ImageField()
    vin = models.ForeignKey("Vin")
```

Pour pouvoir jouer avec il faut en plus :
- Créer la migration correspondante
- Compléter le comportement attendu de l'admin

### Créer la migration
Ça se fait très facilement, en tapant dans la console (toujours avec l'environnement virtuel, bien sûr !)

```
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```
Et voilà, la base de données est à jour des modifications apportées à models.py!

### Compléter le comportement attendu de l'admin
Pour annoncer que l'on veut pouvoir jouer avec les bouteilles dans l'admin, il faut le préciser dans core/admin.py. On importe la classe Bouteille depuis models.py et on invoque la fonction register sur cette nouvelle classe:
```
from .models import Vin, Bouteille

admin.site.register(Vin)
admin.site.register(Bouteille)
```

On relance le serveur de test avec
```
(env)$ python manage.py runserver
```
Et à l'adresse http://localhost:8000/admin/core/ on peut maintenant ajouter supprimer et modifier des bouteilles !
