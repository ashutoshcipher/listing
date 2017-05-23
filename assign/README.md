A. Upload Location/Prop:-

upload(model_name, file, app_name) This takes 3 parameter model_name, file location, app_name

For updating Locations/prop, run the following command
1. python manage.py shell
2. from apps.property.views import upload
3. uploadLocation('Location', 'locations-1.csv', 'property')    // for Location
4. uploadProp('Prop', 'a1-1.csv', 'property')               //  for Prop

B. To download the required file
A file will be created after running following commands

1. python manage.py shell
2. from apps.property.views import download
3. download()

