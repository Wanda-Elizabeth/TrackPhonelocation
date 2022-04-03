import phonenumbers
from test import number

from phonenumbers import geocoder
ch_number=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_number,"en"))
from phonenumbers import carrier
service_number=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(ch_number,"en"))

from test import number2
from phonenumbers import geocoder
ch_number2=phonenumbers.parse(number2,"CH")
print(geocoder.description_for_number(ch_number2,"en"))
from phonenumbers import carrier
service_number=phonenumbers.parse(number2,"RO")
print(carrier.name_for_number(ch_number2,"en"))

from test import number3
from phonenumbers import geocoder
ch_number3=phonenumbers.parse(number3,"CH")
print(geocoder.description_for_number(ch_number3,"en"))
from phonenumbers import carrier
service_number=phonenumbers.parse(number3,"RO")
print(carrier.name_for_number(ch_number3,"en"))

from test import number4
from phonenumbers import geocoder
ch_number4=phonenumbers.parse(number4,"CH")
print(geocoder.description_for_number(ch_number4,"en"))
from phonenumbers import carrier
service_number=phonenumbers.parse(number4,"RO")
print(carrier.name_for_number(ch_number4,"en"))

from test import number5
from phonenumbers import geocoder
ch_number5=phonenumbers.parse(number5,"CH")
print(geocoder.description_for_number(ch_number5,"en"))
from phonenumbers import carrier
service_number=phonenumbers.parse(number5,"RO")
print(carrier.name_for_number(ch_number5,"en"))

from test import number6
from phonenumbers import geocoder
ch_number6=phonenumbers.parse(number6,"CH")
print(geocoder.description_for_number(ch_number6,"en"))
from phonenumbers import carrier
service_number=phonenumbers.parse(number6,"RO")
print(carrier.name_for_number(ch_number6,"en"))








