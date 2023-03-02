import os
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from myapp.models import Person, Hijo 
from .forms import PersonForm, SonForm


 
# Create your views here.

class Inicio(TemplateView):
    template_name = 'baseslider.html'   

def home(request):
    return render(request, 'baseslider.html')
 
 #Forma 2 (Estilo SharmaCoder) | Listar (Version Verificada)
""" def listarPersonas(request):
    personasListado = Person.objects.all()
    messages.success(request, '¡Miembros listados!')
    return render(request, 'show.html', {'persons': personasListado}) """
#Forma 2 (Estilo SharmaCoder) | Listar

#Forma 3 (Estilo moises sepulveda) | Listar (Ultimo Usado Funcional)
""" def listarPersonas(request):
    personasListado = Person.objects.all()
    data = {
        'persons': personasListado,
    }
    messages.success(request, '¡Miembros listados!')
    return render(request, 'show.html', data)   """

#Forma 3 (Estilo moises sepulveda) | Listar

#Forma 4 (Estilo AlgoriSoft) | Listar 

class PersonaListView(ListView):
    model = Person
    template_name = 'show.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Person.objects.all()

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Person.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False) 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Personas'
        context['entity'] = 'Personas'
        context['create_url'] = reverse_lazy('myapp:person_create')
        context['list_url'] = reverse_lazy('myapp:person_list')
        return context 


#Forma 4 (Estilo AlgoriSoft) | Listar 


#Forma 1 (Estilo uskokrum2010) | Create
"""def registrarPersona(request):
    if request.method == "POST": 
        
        name = request.POST['txtName']
        lastname = request.POST['txtLastname']
        dni = request.POST['txtDni']
        celular = request.POST['numCelular']
        gender = request.POST['selectGender']
        member = request.POST['selectMember']
        address = request.POST['textAddress']
        date_birth = request.POST['fechaNacimiento']
        age = request.POST['numEdad']
        state = request.POST['selectState']

        if len(request.FILES) != 0: image = request.FILES['image']

        person = Person.objects.create(
                        name=name, 
                        lastname=lastname, 
                        dni=dni, 
                        celular=celular,
                        gender=gender,
                        member=member,
                        address=address,
                        date_birth=date_birth,
                        age=age,
                        state=state,
                        image=image

                        )
        messages.success(request, '¡Miembro registrado!')
        return render(request, 'index.html')
            
    else:  
        return render(request,'index.html')"""    
#Forma 1 (Estilo uskokrum2010) | Create 


#Forma 2 (Estilo SharmaCoder) | Create (Version Verificada)
""" def registrarPersona(request):
    if request.method == "POST": 
        person = Person()
        person.name = request.POST.get('txtName')
        person.lastname = request.POST.get('txtLastname')
        person.dni = request.POST.get('txtDni')
        person.celular = request.POST.get('numCelular')
        person.gender = request.POST.get('selectGender')
        person.member = request.POST.get('selectMember')
        person.address = request.POST.get('textAddress')
        person.date_birth = request.POST.get('fechaNacimiento')
        person.age = request.POST.get('numEdad')
        person.state = request.POST.get('selectState')

        if len(request.FILES) != 0: 
            person.image = request.FILES['image']

        person.save()
        messages.success(request, '¡Miembro registrado!')
        return render(request, 'index.html')
            
    else:  
        return render(request,'index.html')   """ 
#Forma 2 (Estilo SharmaCoder) | Create (Version Verificada)

#Forma 3 (Estilo moises sepulveda) | Create 
""" def registrarPersona(request,*args, **kwargs):
        data = {}
        hijos = Hijo.objects.all()
        data = {
            'form': PersonForm(),
            'hijos': hijos
        }
        if request.method == 'POST':
            formulario = PersonForm(data=request.POST, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, '¡Miembro registrado!')
            else:
                data["form"] = formulario
        return render (request, 'add.html', data) """
#Forma 3 (Estilo moises sepulveda) | Create 

#Forma 4 (Estilo AlgoriSoft) | Create 

class PersonaCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'add.html'
    success_url = reverse_lazy('myapp:person_list')
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self,request,*args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
                messages.success(request, '¡Miembro registrado!')
            elif action == 'search_hijos':
                    data = []
                    term = request.POST['term']
                    hijos = Hijo.objects.filter(name__icontains=term)[0:10]
                    for i in hijos:
                        item = i.toJSON()
                        item['text'] = i.name
                        data.append(item)
            else:
                data['error'] = 'No se ha Ingresado a una Opcion'
        except Exception as e:
            data['error'] = str(e)
            #return HttpResponse('Exception: Data Not Found')
        return JsonResponse(data, safe=False) 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de una Persona'
        context['entity'] = 'Personas'
        #context['list_url'] = reverse_lazy('myapp:person_list')
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


#Forma 4 (Estilo AlgoriSoft) | Create 



#Forma 1 (Estilo uskokrum2010) | Update
#Primero se Pasan los Valores al Formulario
"""def edicionPersona(request, id):
    person = Person.objects.get(id=id)
    return render(request, "edit.html", {"person": person})"""

#Luego se Guardan Nuevos Valores del Formulario
"""def editarPersona(request):
     if request.method == "POST": 
        id = request.POST['id']
        name = request.POST['txtName']
        lastname = request.POST['txtLastname']
        dni = request.POST['txtDni']
        celular = request.POST['numCelular']
        gender = request.POST['selectGender']
        member = request.POST['selectMember']
        address = request.POST['textAddress']
        date_birth = request.POST['fechaNacimiento']
        age = request.POST['numEdad']
        state = request.POST['selectState']

        if len(request.FILES) != 0: 
          image = request.FILES['image']
         
        person = Person.objects.get(id=id)
        person.id = id 
        person.name = name 
        person.lastname=lastname
        person.dni= dni
        person.celular= celular
        person.gender= gender
        person.member= member
        person.address= address
        person.date_birth= date_birth
        person.age= age
        person.state= state
        if len(person.image) > 0:
                os.remove(person.image.path)
        person.image= image
        person.save()

        messages.success(request, '¡Miembro actualizado!')
        return render(request, "show.html") """
#Forma 1 (Estilo uskokrum2010) | Update        


#Forma 2 (Estilo SharmaCoder) | Update (Version Verificada)

""" def editPerson(request, id):
    person = Person.objects.get(id=id)

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(person.image) > 0:
                os.remove(person.image.path)
            person.image = request.FILES['image']
   
        person.id = request.POST['id']
        person.name = request.POST['txtName']
        person.lastname = request.POST['txtLastname']
        person.dni = request.POST['txtDni']
        person.celular = request.POST['numCelular']
        person.gender = request.POST['selectGender']
        person.member = request.POST['selectMember']
        person.address = request.POST['textAddress']
        person.date_birth = request.POST['fechaNacimiento']
        person.age = request.POST['numEdad']
        person.state = request.POST['selectState']
        
        person.save()
        messages.success(request, '¡Miembro actualizado!')
        return redirect('/myapp/')

    context = {'person':person}
    return render(request, 'edit.html', context) """

#Forma 2 (Estilo SharmaCoder) | Update (Version Verificada)

#Forma 3 (Estilo moises sepulveda) | Update 

""" def editPerson(request, id):
    person = get_object_or_404(Person, id=id)

    data = {
        'form': PersonForm(instance=person)
    }

    if request.method == 'POST':
        formulario = PersonForm(data=request.POST, instance=person, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/myapp/')
        data["form"] = formulario

    return render (request, 'edit.html', data)  """

#Forma 4 (Estilo AlgoriSoft) | Update 

class PersonaUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'edit.html'
    success_url = reverse_lazy('myapp:person_list')
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self,request,*args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
                messages.success(request, '¡Miembro actualizado!')
            elif action == 'search_hijos':
                    data = []
                    term = request.POST['term']
                    hijos = Hijo.objects.filter(name__icontains=term)[0:10]
                    for i in hijos:
                        item = i.toJSON()
                        item['text'] = i.name
                        data.append(item)
            else:
                data['error'] = 'No se ha Ingresado a una Opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de una Persona'
        context['entity'] = 'Personas'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context 




#Forma 4 (Estilo AlgoriSoft) | Update 

#Forma 3 (Estilo moises sepulveda) | Update 


#Forma 2 (Estilo SharmaCoder) | Delete (Version Verificada)
def eliminarPersona(request, id):
    person = Person.objects.get(id=id)

    try:
        if len(person.image) > 0:
            os.remove(person.image.path)
            person.delete()
            messages.success(request, '¡Miembro eliminado!')
            return redirect('/myapp/')
    except:
            messages.success(request, 'Nota: Este Registro no tiene una Foto, favor adjuntar una, antes de intentar eliminar')
            return redirect('/myapp/personas/list/')
            
   
   
    
#Forma 2 (Estilo SharmaCoder) | Delete (Version Verificada)

#Forma 3 (Estilo moises sepulveda) | Delete 

""" def eliminarPersona(request, id):
    person = get_object_or_404(Person, id=id)
    person.delete()
    messages.success(request, '¡Miembro eliminado!')
    return redirect('/myapp/') """

#Forma 3 (Estilo moises sepulveda) | Delete 

def listarSons(request):
    try:
        hijosListado = Hijo.objects.all()
        data = {
            'sons': hijosListado,
        }
        messages.success(request, '¡Miembros listados!')
        return render(request, 'showsons.html', data) 
    except:
            messages.success(request, 'Error de Manipulacion de Usuario')
            return redirect('/myapp/')


def registrarHijo(request):
    try:
        data = {
            'form': SonForm()
        }

        if request.method == 'POST':
            formulario = SonForm(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, '¡Miembro registrado!')
            else:
                data["form"] = formulario 
    except:
            messages.success(request, 'Error de Manipulacion de Usuario')
            return redirect('/myapp/')

    return render (request, 'addson.html', data)


def editHijo(request, id):
    try:
        hijo = get_object_or_404(Hijo, id=id)

        data = {
            'form': SonForm(instance=hijo)
        }

        if request.method == 'POST':
            formulario = SonForm(data=request.POST, instance=hijo)
            if formulario.is_valid():
                formulario.save()
                return redirect('/myapp/')
            data["form"] = formulario
    except:
            messages.success(request, 'Error de Manipulacion de Usuario')
            return redirect('/myapp/')

    return render (request, 'editson.html', data)



def verPersona(request, id):
    try:
        person = Person.objects.get(id=id)
        return render(request, "view.html", {"person": person})
    except:
            messages.success(request, 'Error de Manipulacion de Usuario')
            return redirect('/myapp/')


def verdashboard0(request):
    persons = Person.objects.all()        

    context = {
        "persons": persons
    }

    return render(request, 'chart.html', context)


def verdashboard(request):

    try:
        male_no = Person.objects.filter(gender='Masculino').count()
        male_no = int(male_no)
        print('Number of Male Are',male_no)

        female_no = Person.objects.filter(gender='Femenino').count()
        female_no = int(female_no)
        print('Number of Female Are',female_no)

        gender_list = ['Masculino', 'Femenino']
        gender_number = [male_no, female_no] 

        msi = Person.objects.filter(member='True').count()
        msi = int(msi)
        print('Number of SI Miembros Are',msi)

        mno = Person.objects.filter(member='False').count()
        mno = int(mno)
        print('Number of NO Miembros Are',mno)

        member_list = ['SI', 'NO']
        member_number = [msi, mno]   

        dsi = Person.objects.filter(discipleship='True').count()
        dsi = int(dsi)
        print('Number of SI Discipulados Are',dsi)

        dno = Person.objects.filter(discipleship='False').count()
        dno = int(dno)
        print('Number of NO Discipulados Are',dno)

        discipulados_list = ['SI', 'NO']
        discipulados_number = [dsi, dno]   


        bsi = Person.objects.filter(baptized='True').count()
        bsi = int(bsi)
        print('Number of SI Bautizados Are',bsi)

        bno = Person.objects.filter(baptized='False').count()
        dno = int(bno)
        print('Number of NO Bautizados Are',bno)

        bautizados_list = ['SI', 'NO']
        bautizados_number = [bsi, bno]   

        rolp = Person.objects.filter(familyrol='PAPÁ').count()
        rolp = int(rolp)
        print('Number of PAPÁ Are',rolp)

        rolm = Person.objects.filter(familyrol='MAMÁ').count()
        rolm = int(rolm)
        print('Number of MAMÁ Are',rolm)

        rolna = Person.objects.filter(familyrol='N/A').count()
        rolna = int(rolna)
        print('Number of N/A Are',rolna)

        rol_list = ['PAPÁ','MAMÁ','N/A']
        rol_number = [rolp, rolm, rolna] 

        mp1 = Person.objects.filter(ministry__name__startswith='ANCIANOS').count()
        mp1 = int(mp1)
        print('Number of ANCIANOS Are',mp1)

        mp2 = Person.objects.filter(ministry__name__startswith='CADETES').count()
        mp2 = int(mp2)
        print('Number of CADETES Are',mp2)

        mp3 = Person.objects.filter(ministry__name__startswith='CUADRA_KIDS').count()
        mp3 = int(mp3)
        print('Number of CUADRA_KIDS Are',mp3)
        
        mp4 = Person.objects.filter(ministry__name__startswith='DANZA_Y_CORROS_PENIEL').count()
        mp4 = int(mp4)
        print('Number of DANZA_Y_CORROS_PENIEL Are',mp4)

        mp5 = Person.objects.filter(ministry__name__startswith='DIACONOS_Y_SERVIDORES').count()
        mp5 = int(mp5)
        print('Number of DIACONOS_Y_SERVIDORES Are',mp5)

        mp6 = Person.objects.filter(ministry__name__startswith='INTERSECION').count()
        mp6 = int(mp6)
        print('Number of INTERSECION Are',mp6)

        mp7 = Person.objects.filter(ministry__name__startswith='LIDER_DE_GRUPO_DE_VIDA').count()
        mp7 = int(mp7)
        print('Number of LIDER_DE_GRUPO_DE_VIDA Are',mp7)

        mp8 = Person.objects.filter(ministry__name__startswith='MAESTROS_DE_DISCIPULADO_GENERAL_Y_MAYOR').count()
        mp8 = int(mp8)
        print('Number of MAESTROS_DE_DISCIPULADO_GENERAL_Y_MAYOR Are',mp8)

        mp9 = Person.objects.filter(ministry__name__startswith='MULTIMEDIA_Y_CAMARAS').count()
        mp9 = int(mp9)
        print('Number of MULTIMEDIA_Y_CAMARAS Are',mp9)

        mp10 = Person.objects.filter(ministry__name__startswith='NO_PERTENEZCO_A_NINGUN_MINISTERIO').count()
        mp10 = int(mp10)
        print('Number of NO_PERTENEZCO_A_NINGUN_MINISTERIO Are',mp10)

        mp11 = Person.objects.filter(ministry__name__startswith='PENIEL_WORSHIP').count()
        mp11 = int(mp11)
        print('Number of PENIEL_WORSHIP Are',mp11)

        mp12 = Person.objects.filter(ministry__name__startswith='PRE_ADOLESCENTES').count()
        mp12 = int(mp12)
        print('Number of PRE_ADOLESCENTES Are',mp12)

        mp13 = Person.objects.filter(ministry__name__startswith='SUPERVISOR_DE_ZONA').count()
        mp13 = int(mp13)
        print('Number of SUPERVISOR_DE_ZONA Are',mp13)

        personm_list = ['ANCIANOS', 'CADETES','CUADRA_KIDS','DANZA_Y_CORROS_PENIEL','DIACONOS_Y_SERVIDORES','INTERSECION','LIDER_DE_GRUPO_DE_VIDA','MAESTROS_DE_DISCIPULADO_GENERAL_Y_MAYOR','MULTIMEDIA_Y_CAMARAS','NO_PERTENEZCO_A_NINGUN_MINISTERIO','PENIEL_WORSHIP','PRE_ADOLESCENTES','SUPERVISOR_DE_ZONA']
        personm_number = [mp1, mp2,mp3,mp4,mp5,mp6,mp7,mp8,mp9,mp10,mp11,mp12,mp13]  



        hb1 = Hijo.objects.filter(baptized='True').count()
        hb1 = int(hb1)
        print('Number of SI Bautizados Are',hb1)

        hb2 = Hijo.objects.filter(baptized='False').count()
        hb2 = int(hb2)
        print('Number of NO Bautizados Are',hb2)

        hijo_list = ['SI', 'NO']
        hijo_number = [hb1, hb2]  

        mh1 = Hijo.objects.filter(ministry__name__startswith='ANCIANOS').count()
        mh1 = int(mh1)
        print('Number of ANCIANOS Are',mh1)

        mh2 = Hijo.objects.filter(ministry__name__startswith='CADETES').count()
        mh2 = int(mh2)
        print('Number of CADETES Are',mh2)

        mh3 = Hijo.objects.filter(ministry__name__startswith='CUADRA_KIDS').count()
        mh3 = int(mh3)
        print('Number of CUADRA_KIDS Are',mh3)
        
        mh4 = Hijo.objects.filter(ministry__name__startswith='DANZA_Y_CORROS_PENIEL').count()
        mh4 = int(mh4)
        print('Number of DANZA_Y_CORROS_PENIEL Are',mh4)

        mh5 = Hijo.objects.filter(ministry__name__startswith='DIACONOS_Y_SERVIDORES').count()
        mh5 = int(mh5)
        print('Number of DIACONOS_Y_SERVIDORES Are',mh5)

        mh6 = Hijo.objects.filter(ministry__name__startswith='INTERSECION').count()
        mh6 = int(mh6)
        print('Number of INTERSECION Are',mh6)

        mh7 = Hijo.objects.filter(ministry__name__startswith='LIDER_DE_GRUPO_DE_VIDA').count()
        mh7 = int(mh7)
        print('Number of LIDER_DE_GRUPO_DE_VIDA Are',mh7)

        mh8 = Hijo.objects.filter(ministry__name__startswith='MAESTROS_DE_DISCIPULADO_GENERAL_Y_MAYOR').count()
        mh8 = int(mh8)
        print('Number of MAESTROS_DE_DISCIPULADO_GENERAL_Y_MAYOR Are',mh8)

        mh9 = Hijo.objects.filter(ministry__name__startswith='MULTIMEDIA_Y_CAMARAS').count()
        mh9 = int(mh9)
        print('Number of MULTIMEDIA_Y_CAMARAS Are',mh9)

        mh10 = Hijo.objects.filter(ministry__name__startswith='NO_PERTENEZCO_A_NINGUN_MINISTERIO').count()
        mh10 = int(mh10)
        print('Number of NO_PERTENEZCO_A_NINGUN_MINISTERIO Are',mh10)

        mh11 = Hijo.objects.filter(ministry__name__startswith='PENIEL_WORSHIP').count()
        mh11 = int(mh11)
        print('Number of PENIEL_WORSHIP Are',mh11)

        mh12 = Hijo.objects.filter(ministry__name__startswith='PRE_ADOLESCENTES').count()
        mh12 = int(mh12)
        print('Number of PRE_ADOLESCENTES Are',mh12)

        mh13 = Hijo.objects.filter(ministry__name__startswith='SUPERVISOR_DE_ZONA').count()
        mh13 = int(mh13)
        print('Number of SUPERVISOR_DE_ZONA Are',mh13)

        hijom_list = ['ANCIANOS', 'CADETES','CUADRA_KIDS','DANZA_Y_CORROS_PENIEL','DIACONOS_Y_SERVIDORES','INTERSECION','LIDER_DE_GRUPO_DE_VIDA','MAESTROS_DE_DISCIPULADO_GENERAL_Y_MAYOR','MULTIMEDIA_Y_CAMARAS','NO_PERTENEZCO_A_NINGUN_MINISTERIO','PENIEL_WORSHIP','PRE_ADOLESCENTES','SUPERVISOR_DE_ZONA']
        hijom_number = [mh1, mh2,mh3,mh4,mh5,mh6,mh7,mh8,mh9,mh10,mh11,mh12,mh13]  

        context = {
            'gender_list':gender_list, 
            'gender_number':gender_number,
            'member_list':member_list, 
            'member_number':member_number,
            'discipulados_list':discipulados_list, 
            'discipulados_number':discipulados_number,
            'bautizados_list':bautizados_list, 
            'bautizados_number':bautizados_number,
            'rol_list':rol_list, 
            'rol_number':rol_number,
            'personm_list':personm_list, 
            'personm_number':personm_number,


            'hijo_list':hijo_list, 
            'hijo_number':hijo_number,
            'hijom_list':hijom_list, 
            'hijom_number':hijom_number
        }

        return render(request, 'chart.html', context)
    except:
            messages.success(request, 'Error de Manipulacion de Usuario')
            return redirect('/myapp/')


def listarph(request):
    try:
        person_list = Person.objects.all()
        person_list = {'person_list': person_list,}
        messages.success(request, '¡Miembros listados!')
        return render(request, 'showhp.html', person_list)  
    except:
            messages.success(request, 'Error de Manipulacion de Usuario')
            return redirect('/myapp/')


def listarpm(request):
    try:
        personm_list = Person.objects.all()
        personm_list = {'personm_list': personm_list,}
        messages.success(request, '¡Miembros listados!')
        return render(request, 'showpm.html', personm_list) 
    except:
            messages.success(request, 'Error de Manipulacion de Usuario')
            return redirect('/myapp/')

def listarhm(request):
    try:
        hijom_list = Hijo.objects.all()
        hijom_list = {'hijom_list': hijom_list,}
        messages.success(request, '¡Miembros listados!')
        return render(request, 'showhm.html', hijom_list) 
    except:
            messages.success(request, 'Error de Manipulacion de Usuario')
            return redirect('/myapp/')

