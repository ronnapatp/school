/*:
## แบบฝึกหัดแอป - การแปลงประเภท

 >แบบฝึกหัดเหล่านี้เป็นการเน้นย้ำแนวคิดการใช้งาน Swift ในบริบทของแอปการติดตามข้อมูลฟิตเนส

 หากคุณทำแบบฝึกหัดเกี่ยวกับการคำนวณข้อมูลฟิตเนสเสร็จสิ้นแล้ว แสดงว่าคุณได้คำนวณเปอร์เซ็นต์ของจำนวนก้าวเป้าหมายประจำวันที่ผู้ใช้ทำได้สำเร็จแล้ว แต่คุณได้คำนวณโดยให้ `steps` เป็นประเภท `Double` ซึ่งคุณไม่สามารถติดตามจำนวนก้าวแบบบางส่วนได้ ดังนั้น `steps` จึงควรจะเป็นประเภท `Int` มากกว่า ลองประกาศ `steps` เป็นประเภท `Int` แล้วระบุค่าระหว่าง 500 ถึง 6,000 จากนั้นประกาศ `goal` เป็นประเภท `Int` แล้วตั้งค่าให้เท่ากับ 10,000

 ทีนี้ให้สร้างค่าคงที่ `percentOfGoal` ของประเภท `Double` ที่เท่ากับเปอร์เซ็นต์ของเป้าหมายที่ทำสำเร็จแล้วจนถึงตอนนี้ โดยคุณจะต้องแปลงค่าคงที่ของประเภท `Int` ให้เป็นประเภท `Double` ในการคำนวณของคุณ
 */


/*:
 _ลิขสิทธิ์ © 2021 Apple Inc._

 _การอนุญาต ณ ที่นี้ ไม่มีค่าใช้จ่ายใดๆ สำหรับบุคคลที่ได้รับสำเนาของซอฟต์แวร์นี้ รวมถึงไฟล์เอกสารที่เกี่ยวข้อง (เรียกว่า "ซอฟต์แวร์") เพื่อการใช้งานซอฟต์แวร์โดยไม่มีข้อจำกัด รวมถึงแต่ไม่จำกัดเฉพาะ สิทธิ์ในการใช้งาน คัดลอก แก้ไข รวมเข้าด้วยกัน เผยแพร่ แจกจ่าย ให้ช่วงสิทธิ์ และ/หรือขายสำเนาของซอฟต์แวร์ และอนุญาตให้บุคคลที่ได้รับซอฟต์แวร์ไปเพื่อกระทำการดังกล่าว ต้องปฏิบัติตามเงื่อนไขต่อไปนี้_

 _ประกาศลิขสิทธิ์ข้างต้นและประกาศอนุญาตนี้จะรวมอยู่ในสำเนาทั้งหมดหรือส่วนสำคัญของซอฟต์แวร์_

 _ซอฟต์แวร์นี้จัดหาให้ "อย่างที่เป็น" โดยไม่มีการรับประกันใดๆ ไม่ว่าโดยชัดแจ้งหรือโดยนัย รวมถึงแต่ไม่จำกัดเพียงการรับประกันเรื่องความสามารถทางการค้า ความเหมาะสมในการใช้งานสำหรับวัตถุประสงค์อย่างใดเป็นการเฉพาะ และการไม่ละเมิด เจ้าของลิขสิทธิ์หรือผู้ถือครองสิทธิ์จะไม่รับผิดในทุกกรณีต่อข้อเรียกร้อง ความเสียหาย หรือความรับผิดใดๆ ไม่ว่าจะเป็นการกระทำของสัญญา การละเมิด หรือการกระทำอื่นใด ที่เกิดขึ้นจากหรือเกี่ยวข้องกับซอฟต์แวร์หรือการใช้งาน รวมถึงข้อตกลงอื่นๆ ในซอฟต์แวร์นี้_

[ก่อนหน้า](@previous)  |  หน้า 8 จาก 8
 */