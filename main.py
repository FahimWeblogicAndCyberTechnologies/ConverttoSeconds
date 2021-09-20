def conversion(sec):
    sec_value = sec % (24 * 3600)
    hour_value = sec_value // 3600
    sec_value %= 3600
    min = sec_value // 60
    sec_value %= 60
    print("Converted sec value in hour:", hour_value)
    print("Converted sec value in minutes:", min)


sec = 50000
conversion(sec)