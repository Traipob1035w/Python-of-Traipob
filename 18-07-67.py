# start 
dataset = [1,50,60,3,89,200]
if not dataset : 
    print ('รายการว่างเปล่า')
else:
    print('มีข้อมูล')
    max = dataset[0]
    print(max)
    for x in dataset:
        if x > max:
            max = x 
    print(max)
    # END