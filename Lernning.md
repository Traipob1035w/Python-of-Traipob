##### การเรียนเขียนโปรแกรม ####
 ctrl+B                 = เปิดปิด Explorer
 ctrl+J                 = เปิดปิด Terminal
 ctrl+shift+N           = เปิด VS Code ใหม่ขึ้นมา
 cd \                   = ทำให้อยู่ใน drive-C
 cd ..                  = ถอยไปทีละขั้นจนถึง drive-C
 dir                    = แสดง folder ใน driveC
 mkdir ตามด้วยชื่อ folder  = สร้าง folder 
shift + alt + ลูกศรลง    = คัดลอกลงมาบรรทัดข้างล่าง
ctrl + shift + k        = ลบทีละบรรทัดจากล่างขึ้นบน
alt + ลูกศรขึ้น-ลง         = สลับบรรทัด
วางเคอเซอร์ ณ จุดที่ต้องการ และ กด shift + alt แล้วลากเคอเซอร์ลง  = พิมทีละหลายบรรทัด
ctrl + D = เลือกคำที่เหมือนกัน และสามารถแก้ไขพร้อมกันได้
ctrl + F2 = เลือกคำที่เหมือนกันทั้งหมด และสามารถแก้ไขพร้อมกันได้
cyrl + P = ค้นหาไฟล์
ctrl + w = ปิดแท็บไปเรื่อยๆ 
ctrl + / = คอมเม้นบรรทัดนั้นๆ 

Oprators 
 x1 = 1+3 #บวก
 x2 = 3-3 #
 x3 = 2*3 #
 x4 = 6/3 #
 x5 = 23%3 # mod การหารเอาเศษเหลือ
 x6 = 2**3 #การยกกำลัง
 x7 = 4 // 6 #หารโดยไม่เอาเศษ หรือปัดเศษทิ้ง
 x8 &= 3 # x1 = x1 & 3 AND

  # ลูป for ที่ทำการแสดงผลตัวเลขจาก1- 100 (เลขคู่)
for i in range(1 , 101):
    if i % 2 ==0 :
        print(i)

         money = (int(input("price : ")))
 if  money == 50 :
 print ("coke")
 elif money == 60 :
  print ("papsy")
 elif money == 30 :
  print ("lay")
 else :
  print ("ไม่พบรายการ")

# ลูป   while แสดงเลขคู่
i = 1 
# คำสั่งวนซ้ำ
while i <= 10 :
        # คำสั่งเช็คเงื่อนไข
        if i % 2 ==0:
            print(i)
            # คำสั่งเพิ่มค่า
        i +=1
<!-- ####เครื่องคิดเลข#### -->
rider = (int(input("number1 : ")))
saber = (int(input("number2 : ")))
def yaho(rider,saber):
   print("บวก :",rider+saber)

def gang(rider,saber):
  print("ลบ :",rider-saber)

def yae(rider,saber):
 print("คูณ :",rider*saber)

def riden(rider,saber):
   print("หาร :",rider/saber)

yaho(rider,saber)
gang(rider,saber)
yae(rider,saber)
riden(rider,saber)