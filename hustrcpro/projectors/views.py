from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader

from django.db import connection

from projectors.models import Build, Brand, Projector, Room, Statusrecord, Maintenancerecord
from projectors.models import Problem

def index(request):
    item_list = ['Build', 'Brand', 'Projector']
    template = loader.get_template('projectors/index.html')  
    context = RequestContext(request, {
        'item_list': item_list,
    })
    return HttpResponse(template.render(context))

def builds(request):
    builds_list = Build.objects.order_by('build_id')[:25]
    template = loader.get_template('projectors/builds.html')
    context = RequestContext(request, {
        'builds_list': builds_list,
    })
    return HttpResponse(template.render(context))

def build_rooms(request, build_id):
    build = Build.objects.get(build_id=build_id)
    build_rooms_list = Room.objects.filter(build_id=build_id).order_by('room_id')
    #build_room_projector_list = []
    #for room in build_rooms_list:
    #    # room_id, room_name, projector_id, projector_name, brand_id, brand_cn, brand_en, model_number, 
    #    
    #    projector = Projector.objects.get(room_id = room.room_id)
    #    if projector is None:
    #        continue
    #    brand = Brand.objects.get(brand_id = projector.brand_id)
    #    #elem = list(room) + list(projector) + list(brand)
    #    elem = [room.room_id, room.room_name, projector.projector_id, brand.brand_id, brand.brand_cn, brand.brand_en, brand.model_number]
    #    build_room_projector_list.append(elem)
    
    #cursor = connection.cursor()
    #cursor.execute("""select r.build_id, r.room_id, r.room_name, p.projector_id, b.brand_id, b.brand_cn, b.brand_en, b.model_number from Rooms r left join Projectors p on r.room_id = p.room_id left join Brands b on p.brand_id = b.brand_id where r.build_id = %s""", [build_id])
    #build_room_projector_list = cursor.fetchall()
    
    build_room_projector_list = Room.objects.room_projectors(build_id)
    template = loader.get_template('projectors/rooms.html')
    context = RequestContext(request, {
        'build_rooms_list': build_rooms_list,
        'build': build,
        'build_room_projector_list': build_room_projector_list,
    })
    return HttpResponse(template.render(context))

def brands(request):
    brands_list = Brand.objects.order_by('brand_id')
    template = loader.get_template('projectors/brands.html')  
    context = RequestContext(request, {
        'brands_list': brands_list,
    })
    return HttpResponse(template.render(context))

def brand_projector(request, brand_id):
    brand = Brand.objects.get(brand_id = brand_id)
    brand_projector_list = Brand.objects.brand_projectors(brand_id)
    template = loader.get_template('projectors/brand_projector.html')
    context = RequestContext(request, {
        'brand': brand,
        'brand_projector_list': brand_projector_list,
    })
    return HttpResponse(template.render(context))

def projectors(request):
    projector_list = Projector.objects.detail()
    template = loader.get_template('projectors/projectors.html')
    context = RequestContext(request, {
        'projector_list': projector_list,
    })
    return HttpResponse(template.render(context))

def status_records(request, projector_id):
    status_records = Statusrecord.objects.filter(projector_id = projector_id)
    template = loader.get_template('projectors/status_records.html')
    context = RequestContext(request, {
        'status_records': status_records,
    })
    return HttpResponse(template.render(context))

def maintenance_records(request, projector_id):
    maintenance_records = Maintenancerecord.objects.filter(projector_id = projector_id)
    template = loader.get_template('projectors/maintenance_records.html')
    context = RequestContext(request, {
        'maintenance_records': maintenance_records,
    })
    return HttpResponse(template.render(context))

def problems(request):
	problems_list = Problem.objects.detail()
	template = loader.get_template('projectors/problems.html')
	context = RequestContext(request, {
		'problems_list': problems_list,
	})
	return HttpResponse(template.render(context))

def projector_problems(request, projector_id):
	projector_problems_list = Problem.objects.filter(projector_id = projector_id)
	template = loader.get_template('projectors/projector_problems.html')
	context = RequestContext(request, {
		'projector_problems': projector_problems_list,
	})
	return HttpResponse(template.render(context))
def add_problem(request, projector_id):
	p = get_object_or_404(Projector, pk=projector_id)
	return HttpResponse('mess')
	 
