from apps.property.models import Prop, Location, City
from django.core.exceptions import ValidationError
import csv
from django.apps import apps
from django.db import connection
from django.db.models import Q

def upload(model_name, file,app_label):
    model_name = apps.get_model(app_label=app_label, model_name=model_name)
    f  = open(file)
    reader = csv.reader(f)
    keys = [x.name for x in model_name._meta.fields]
    dict_list = []
    for r in reader:
        d = { keys[i] : r[i] if r[i] != "\\N" else r[i] == '' for i in range(len(r))}
        dict_list.append(d)

    rows_with_error = []
    for i, row in enumerate(dict_list):
        try:
            check_row = model_name.objects.filter(id = row['id']).update(**row)
            if check_row <=0:
                m = model_name(**row)
                m.full_clean()
                m.save()
                print("{} record created".format(i+1))
            else:
                print("{} record updated".format(i+1))
        except ValidationError as e:
            rows_with_error.append(i + 1)
    f.close()


def download():
    #joined = Prop.objects.all().extra(tables=["property_location"], where=["project = p_name OR alias LIKE '%' || project || '%'"])
    keys = [x.name for x in Prop._meta.fields]
    keys.extend(["".join(['location__', x.name]) for x in Location._meta.fields])
    keys.extend(["".join(['location__cityf__', x.name]) for x in City._meta.fields])
    rows = Prop.objects.filter(location__isnull=False).select_related('location', 'location__cityf').values_list(*keys)
    #cursor = connection.cursor()
    #cursor.execute(" SELECT * from property_prop INNER JOIN property_location ON property_prop.project = property_location.p_name OR \
    #               property_location.alias LIKE '%' || property_prop.project || '%' ")
    #rows = cursor.fetchall()
    f = open('data.csv', "w")
    writer = csv.writer(f, delimiter=',')
    writer.writerow(keys)
    for line in rows:
        writer.writerow(line)
    f.close()

def uploadProp(model_name, file,app_label):
    model_name = apps.get_model(app_label=app_label, model_name=model_name)
    f  = open(file)
    reader = csv.reader(f)
    keys = [x.name for x in model_name._meta.fields]
    dict_list = []
    for r in reader:
        d = { keys[i] : r[i] if r[i] != "\\N" else r[i] == '' for i in range(len(r))}
        dict_list.append(d)

    rows_with_error = []
    for i, row in enumerate(dict_list):
        try:
            check_row = model_name.objects.filter(id = row['id']).update(**row)
            if check_row <=0:
                m = model_name(**row)
                location = Location.objects.filter(Q(p_name__icontains = row['project']) | Q(alias__icontains = row['project']))
                if location:
                    m.location = location[0]
                m.full_clean()
                m.save()
                print("{} record created".format(i+1))
            else:
                print("{} record updated".format(i+1))
        except ValidationError as e:
            rows_with_error.append(i + 1)
    f.close()


def uploadLocation(model_name, file,app_label):
    model_name = apps.get_model(app_label=app_label, model_name=model_name)
    f  = open(file)
    reader = csv.reader(f)
    keys = [x.name for x in model_name._meta.fields]
    dict_list = []
    for r in reader:
        d = { keys[i] : r[i] if r[i] != "\\N" else r[i] == '' for i in range(len(r))}
        dict_list.append(d)

    rows_with_error = []
    for i, row in enumerate(dict_list):
        try:
            check_row = model_name.objects.filter(id = row['id']).update(**row)
            if check_row <=0:
                m = model_name(**row)
                try:
                    refer_key = 1                     # if the file has reference key(id) for the same, it will be used in case 1
                    city = City.objects.get(id = refer_key)
                    m.cityf = city
                except City.DoesNotExist:
                    pass
                m.full_clean()
                m.save()
                print("{} record created".format(i+1))
            else:
                print("{} record updated".format(i+1))
        except ValidationError as e:
            rows_with_error.append(i + 1)
    f.close()



