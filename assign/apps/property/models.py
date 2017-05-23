from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)


# Create your models here.`_id` int(11) NOT NULL AUTO_INCREMENT,
class Location(models.Model):
    id = models.IntegerField(null=False, blank=False, primary_key=True)
    city_id = models.CharField(max_length=200, null = True, blank = True)
    leafnode = models.IntegerField(null = True, blank = True)
    coordinate_x = models.FloatField(null =  True, blank = True)
    coordinate_y = models.FloatField(null=True, blank=True)
    alias = models.CharField(max_length=1000, null = True, blank = True)
    demography = models.CharField(max_length=200, null = True, blank = True)
    popular = models.CharField(max_length = 10, null = True, blank = True)
    p_name = models.CharField(max_length=200, null = True, blank = True)
    parents_id = models.CharField(max_length=500, null = True, blank = True)
    source = models.CharField(max_length=200, null = True, blank = True)
    map_geomentry_bounds_ne_lat = models.FloatField(null =  True, blank = True)
    map_geomentry_bounds_ne_lng = models.FloatField(null =  True, blank = True)
    map_geomentry_bounds_sw_lat = models.FloatField(null =  True, blank = True)
    map_geomentry_bounds_sw_lng = models.FloatField(null=True, blank=True)
    map_geomentry_location_lat = models.FloatField(null=True, blank=True)
    map_geomentry_location_lng = models.FloatField(null=True, blank=True)
    map_geomentry_viewport_ne_lat = models.FloatField(null=True, blank=True)
    map_geomentry_viewport_ne_lng = models.FloatField(null=True, blank=True)
    map_geomentry_viewport_sw_lat = models.FloatField(null=True, blank=True)
    map_geomentry_viewport_sw_lng = models.FloatField(null=True, blank=True)
    map_geometry_locationtype = models.CharField(max_length=200, null = True, blank = True)
    map_addresscomp1 = models.CharField(max_length=500, null = True, blank = True)
    map_addresscomp2 = models.CharField(max_length=500, null=True, blank=True)
    map_addresscomp3 = models.CharField(max_length=500, null=True, blank=True)
    map_addresscomp4 = models.CharField(max_length=500, null=True, blank=True)
    map_addresscomp5 = models.CharField(max_length=500, null=True, blank=True)
    map_addresscomp6 = models.CharField(max_length=500, null=True, blank=True)
    map_addresscomp7 = models.CharField(max_length=500, null=True, blank=True)
    map_addresscomp8 = models.CharField(max_length=500, null=True, blank=True)
    map_addresscomp9 = models.CharField(max_length=500, null=True, blank=True)
    map_addresscomp10 = models.CharField(max_length=500, null=True, blank=True)
    map_placeid = models.CharField(max_length=500, null=True, blank=True)
    map_formatted_address = models.CharField(max_length=1000, null=True, blank=True)
    map_types = models.CharField(max_length=1000, null=True, blank=True)
    cityf = models.ForeignKey(City, null = True, blank = True)

    def __str__(self):
        return "{}".format(self.id)




class Prop(models.Model):
    id = models.CharField(null=False, blank=False, max_length=20, primary_key=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    sale_rent = models.CharField(max_length=20, null=True, blank=True)
    res_com_agr = models.CharField(max_length=20, null=True, blank=True)
    property_type = models.CharField(max_length=200, null=True, blank=True)
    project = models.CharField(max_length=200, null=True, blank=True)
    project_id = models.CharField(max_length=200, null=True, blank=True)
    project_id_flag = models.CharField(max_length=200, null=True, blank=True)
    locality = models.CharField(max_length=200, null=True, blank=True)
    super_built_area = models.FloatField(null=True, blank=True)
    area_unit = models.CharField(max_length=20, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    price_unit = models.CharField(max_length=20, null=True, blank=True)
    rate = models.FloatField(null=True, blank=True)
    rate_unit = models.CharField(max_length=20, null=True, blank=True)
    transaction_type = models.CharField(max_length=50, null=True, blank=True)
    bhk = models.IntegerField(null = True, blank = True)
    area_max = models.FloatField(null=True, blank=True)
    price_max = models.FloatField(null=True, blank=True)
    built_up_area = models.FloatField(null=True, blank=True)
    carpet_area = models.FloatField(null=True, blank=True)
    maintainance = models.CharField(max_length=50, null=True, blank=True)
    maintainance_unit = models.CharField(max_length=50, null=True, blank=True)
    furnishing = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    meta_description = models.CharField(max_length=500, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    address_id = models.CharField(max_length=1000, null=True, blank=True)
    project_add_id = models.CharField(max_length=50, null=True, blank=True)
    latitude = models.CharField(max_length=50, null=True, blank=True)
    longitude = models.CharField(max_length=50, null=True, blank=True)
    property_code = models.CharField(max_length=50, null=True, blank=True)
    in_search = models.CharField(max_length=50, null=True, blank=True)
    views = models.CharField(max_length=50, null=True, blank=True)
    source = models.CharField(max_length=50, null=True, blank=True)
    source_crawl = models.CharField(max_length=50, null=True, blank=True)
    url = models.CharField(max_length=500, null=True, blank=True)
    posted_on = models.CharField(max_length=500, null=True, blank=True)
    crawled_on = models.CharField(max_length=500, null=True, blank=True)
    posted_by_type = models.CharField(max_length=200, null=True, blank=True)
    posted_by_CF_ID = models.CharField(max_length=50, null=True, blank=True)
    posted_by_name = models.CharField(max_length=50, null=True, blank=True)
    posted_by_company = models.CharField(max_length=200, null=True, blank=True)
    posted_by_address = models.CharField(max_length=200, null=True, blank=True)
    facing = models.CharField(max_length=50, null=True, blank=True)
    balconies = models.CharField(max_length=50, null=True, blank=True)
    ownership = models.CharField(max_length=50, null=True, blank=True)
    deposit = models.CharField(max_length=50, null=True, blank=True)
    posession_from = models.CharField(max_length=50, null=True, blank=True)
    building_status = models.CharField(max_length=50, null=True, blank=True)
    loaction_Id_CF = models.CharField(max_length=50, null=True, blank=True)
    Id_CF = models.CharField(max_length=50, null=True, blank=True)
    floor_no = models.CharField(max_length=200, null=True, blank=True)
    servant_accomodation = models.CharField(max_length=50, null=True, blank=True)
    age_of_construction = models.CharField(max_length=50, null=True, blank=True)
    car_parking = models.CharField(max_length=50, null=True, blank=True)
    over_looking = models.CharField(max_length=50, null=True, blank=True)
    flooring = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    build_message = models.CharField(max_length=500, null=True, blank=True)
    date_format = models.CharField(max_length=50, null=True, blank=True)
    crawled_date_epoch = models.CharField(max_length=50, null=True, blank=True)
    city_id = models.CharField(max_length=50, null=True, blank=True)
    super_built_area_sqft = models.FloatField(null=True, blank=True)
    rate_sqft = models.FloatField(null=True, blank=True)
    is_parent = models.CharField(max_length=5, null=True, blank=True)
    property_type_norm = models.CharField(null = True, blank = True, max_length=50)
    location = models.ForeignKey(Location, null = True, blank = True)

    def __str__(self):
        return "{}".format(self.id)

























