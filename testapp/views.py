from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.core.serializers import serialize
from testapp.models import Student
from testapp.mixins import SerializeMixin,HttpResponseMixin
from django.core.exceptions import ObjectDoesNotExist
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .utils import is_json
from .forms import StudentForm

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class StudentCrud(SerializeMixin,HttpResponseMixin,View):
    def id_valid(self,id):
        try:
            std=Student.objects.get(id=id)
        except ObjectDoesNotExist:
            std=None
        return std

    def get(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps("Please Enter Valid Json Data only!!!")
            return self.render_to_response(json_data,status=400)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is not None:
            std=self.id_valid(id)
            if std is None:
                json_data=json.dumps("Enter id={} is not available".format(id))
                return self.render_to_response(json_data,status=400)
            json_data=self.serialize([std,])
            return self.render_to_response(json_data)
        std=Student.objects.all()
        json_data=self.serialize(std)
        return self.render_to_response(json_data)

    def put(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps("Please Enter Valid Json Data only!!!")
            return self.render_to_response(json_data,status=400)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is None:
            json_data=json.dumps("Enter id={} is not available".format(id))
            return self.render_to_response(json_data,status=400)
        std=self.id_valid(id)
        if std is None:
            json_data=json.dumps("Enter id={} is not available".format(id))
            return self.render_to_response(json_data,status=400)
        provided_data=json.loads(data)
        print(provided_data)
        original_data={
        'Name':std.Name,
        'Father_Name':std.Father_Name,
        'Cell_no':std.Cell_no,
        'Address':std.Address
        }
        original_data.update(provided_data)
        form=StudentForm(original_data,instance=std)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps("Data Updated Successfully!!!")
            return self.render_to_response(json_data)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_response(json_data,status=400)


    def post(self,request,*args,**kwargs):
        data=request.body
        valid_jason=is_json(data)
        if not valid_jason:
            json_data=json.dumps("Please Enter Valid Json Data only!!!")
            return self.render_to_response(json_data,status=400)
        # json_data=json.dumps("Data Successfully updated!!!")
        # return self.render_to_response(json_data)
        stddata=json.loads(data)
        form=StudentForm(stddata)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps("Data Successfully updated!!!")
            return self.render_to_response(json_data)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_response(json_data,status=400)



    def delete(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps("Please Enter Valid Json Data only!!!")
            return self.render_to_response(json_data,status=400)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is None:
            json_data=json.dumps("Enter id={} is shoul not be None".format(id))
            return self.render_to_response(json_data,status=400)
        std=self.id_valid(id)
        if std is None:
            json_data=json.dumps("Enter id={} is not available".format(id))
            return self.render_to_response(json_data,status=400)
        std.delete()
        # print(t)
        json_data=json.dumps( 'Student with id={} deleted Successfully'.format(id))
        return self.render_to_response(json_data)






















@method_decorator(csrf_exempt, name='dispatch')
class StudentView(SerializeMixin,HttpResponseMixin,View):
    def is_id_valid(self,id):
        try:
            std=Student.objects.get(id=id)
        except ObjectDoesNotExist:
            std=None
        return std

    def put(self,request,id,*args,**kwargs):
        std=self.is_id_valid(id)
        if std is None:
            json_data=json.dumps( 'Sorry Student with id={} does not Exist'.format(id))
            return self.render_to_response(json_data,status=404)
        data=request.body
        valid_jason=is_json(data)
        if not valid_json:
            json_data=json.dumps("Please Enter Valid Json Data only!!!")
            return self.render_to_response(json_data,status=400)
        provided_data=json.loads(data)
        original_data={
        'Name':std.Name,
        'Father_Name':std.Father_Name,
        'Cell_no':std.Cell_no,
        'Address':std.Address
        }
        original_data.update(provided_data)
        form=StudentForm(original_data,instance=std)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps("Data Updated Successfully!!!")
            return self.render_to_response(json_data)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_response(json_data,status=400)

    def get(self,request,id,*args,**kwargs):
        try:
            qs=Student.objects.get(id=id)
        except ObjectDoesNotExist:
            json_data=json.dumps( 'Sorry Student with id={} does not Exist'.format(id))
            # return HttpResponse(json_data,content_type='application/json')
            return render_to_response(json_data,status=404)
        else:
            json_data=self.serialize([qs,])
            # return HttpResponse(json_data,content_type='application/json')
            return render_to_response(json_data)

    def delete(self,request,id,*args,**kwargs):
        std=self.is_id_valid(id)
        if std is None:
            json_data=json.dumps( 'Sorry Student with id={} does not Exist'.format(id))
            return self.render_to_response(json_data,status=404)
        std.delete()
        # print(t)
        json_data=json.dumps( 'Student with id={} deleted Successfully'.format(id))
        return self.render_to_response(json_data)




@method_decorator(csrf_exempt, name='dispatch')
class StudentListView(SerializeMixin,HttpResponseMixin,View):

    def get(self,request,*args,**kwargs):
        qs=Student.objects.all()
        json_data=self.serialize(qs)
        return HttpResponse(json_data,content_type='application/json')


    def post(self,request,*args,**kwargs):
        data=request.body
        valid_jason=is_json(data)
        if not valid_jason:
            json_data=json.dumps("Please Enter Valid Json Data only!!!")
            return self.render_to_response(json_data,status=400)
        # json_data=json.dumps("Data Successfully updated!!!")
        # return self.render_to_response(json_data)
        stddata=json.loads(data)
        form=StudentForm(stddata)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps("Data Successfully updated!!!")
            return self.render_to_response(json_data)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_response(json_data,status=400)



















# def emp_data_view(request):
#     emp_data={
#     'eno':100,
#     'ename':'Ganesh Goud',
#     'esal':20000,
#     'eaddr':'Aurangabad'
#     }
#     resp='<h1>Student Number:{},<br>Student Name:{},<br>Student Salary:{},<br>Student Address:{}</h1>'.format(
#     emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eaddr'])
#     return HttpResponse(resp)
#
#
# import json
# def emp_data_jsonview(request):
#     emp_data={
#     'eno':100,
#     'ename':'Ganesh Goud',
#     'esal':20000,
#     'eaddr':'Aurangabad'
#     }
#     json_data=json.dumps(emp_data)
#     return HttpResponse(json_data)
#
#
# def emp_data_jsonview(request):
#     emp_data={
#     'eno':100,
#     'ename':'Ganesh Goud',
#     'esal':20000,
#     'eaddr':'Aurangabad'
#     }
#     json_data=json.dumps(emp_data)
#     return HttpResponse(json_data,content_type='application/json')
#
# def emp_data_jsonview(request):
#     emp_data={
#     'eno':100,
#     'ename':'Ganesh Goud',
#     'esal':20000,
#     'eaddr':'Aurangabad'
#     }
#     json_data=json.dumps(emp_data)
#     return HttpResponse(json_data,content_type='application/json')
#
# from django.http import JsonResponse
# def emp_data_jsonview1(request):
#     emp_data={
#     'eno':100,
#     'ename':'Ganesh Goud',
#     'esal':20000,
#     'eaddr':'Aurangabad'
#     }
#     return JsonResponse(emp_data)
#
# #Class Based views
# # from django.views.generic import View
# # class JsonCbv(View):
# #     def get(self,request,*args,**kwargs):
# #         emp_data={
# #         'eno':100,
# #         'ename':'Ganesh Goud',
# #         'esal':20000,
# #         'eaddr':'Aurangabad'
# #         }
# #         return JsonResponse(emp_data)
#
#
#
#
#
# from django.views.generic import View
# class JsonCbv(View):
#     def get(self,request,*args,**kwargs):
#         json_data=json.dumps({'msg':'These message is from Get method'})
#         return HttpResponse(json_data,content_type='application/json')
#
#
#     def post(self,request,*args,**kwargs):
#         json_data=json.dumps({'msg':'These message is from POST method'})
#         return HttpResponse(json_data,content_type='application/json')
#
#
#     def put(self,request,*args,**kwargs):
#         json_data=json.dumps({'msg':'These message is from put method'})
#         return HttpResponse(json_data,content_type='application/json')
#
#
#     def delete(self,request,*args,**kwargs):
#         json_data=json.dumps({'msg':'These message is from delete method'})
#         return HttpResponse(json_data,content_type='application/json')
