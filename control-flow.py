price = 1000
gst = 10
totalprice = 0
service = 20

if price >= 1000:
    print("gst is applicable")
    totalprice = (price+gst+service)
    print (totalprice)

else:
    print("gst is not applicable")
    