


from tastypie.resources import Resource
from tastypie import fields



class RiakObject(object):

	def __init__(self, initial=None):
	    self.__dict__['_data'] = {}

	    if hasattr(initial, 'items'):
	        self.__dict__['_data'] = initial

	def __getattr__(self, name):
	    return self._data.get(name, None)

	def __setattr__(self, name, value):
	    self.__dict__['_data'][name] = value

	def to_dict(self):
	    return self._data


class DataResource(Resource):
	fields_data = fields.ListField(attribute='fields_data', default=[])

	class Meta:
	    resource_name = 'data'
	    include_resource_uri = False
	    always_return_data = True
	    list_allowed_methods = ['get','post']
	    object_class = RiakObject
	   

	def detail_uri_kwargs(self, bundle_or_obj):
	    kwargs = {}
	    return kwargs

	def obj_get_list(self,bundle,**kwargs):

		fields_data= [1,2,3,4]

		data=[{"fields_data":fields_data}]
		
		return map(RiakObject,data)

	def obj_create(self,bundle,**kwargs):
		data = bundle.data
		name = data.get("name")
		print ":::::::name::::::::::",name
		fields_data= [1,2,3,4]
		bundle.data={"fields_data":fields_data}
		bundle = self.full_hydrate(bundle)
		return bundle
		
