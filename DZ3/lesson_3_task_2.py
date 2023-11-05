from smartphone import Smartphone

catalog = [
            Smartphone("xiaomi", "redmi_6A", "+79999999999"),
            Smartphone("iphone", "XR", "+79999999911"),
            Smartphone("iphone", "XS", "+79999999922"),
            Smartphone("iphone", "X", "+79999999933"),
            Smartphone("iphone", "5s", "+79999999944"),
           ]

for smartphone in catalog:
    smartphone.print_info()
