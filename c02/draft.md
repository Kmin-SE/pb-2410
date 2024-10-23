- Input: ngay, thang, nam
- Output: Hợp lệ / Không hợp lệ

Lên ý tưởng:
- Input: 01/10/2024
=> Câu hỏi: Như thế nào là hợp lệ? => ngày hợp lệ và tháng hợp lệ và năm hợp lệ
=> Câu hỏi: ngày hợp lệ? tháng hợp lệ? năm hợp lệ?
- ngày hợp lệ: ngày trong đoạn [1, 31], có 1 số tháng chỉ có 30, 28, 29 ngày
- tháng hợp lệ: tháng trong đoạn [1, 12]
- năm hợp lệ: nam > 0

nam => thang => ngay

if nam > 0:
    if thang >= 1 and thang <= 12:
        if thang == 1 or thang == 3 ...:
            if ngay >= 1 and ngay <= 31:
                "Hop le"
            else:
                "Khong hop le"
        elif thang == 4 or thang == 6 ...
            if ngay >= 1 and ngay <= 30:
                "Hop le"
            else:
                "Khong hop le"
        else:
            if nam nhuận:
                if ngay >= 1 and ngay <= 29:
                    "Hop le"
                else:
                    "Khong hop le"
            else:
                if ngay >= 1 and ngay <= 28:
                    "Hop le"
                else:
                    "Khong hop le"
    else:
        "Khong hop le"
else:
    "Khong hop le"

Refactor 1:
if nam > 0:
    if thang == 1 or thang == 3 ...:
        if ngay >= 1 and ngay <= 31:
            "Hop le"
        else:
            "Khong hop le"
    elif thang == 4 or thang == 6 ...
        if ngay >= 1 and ngay <= 30:
            "Hop le"
        else:
            "Khong hop le"
    elif thang == 2:
        if nam nhuận:
            if ngay >= 1 and ngay <= 29:
                "Hop le"
            else:
                "Khong hop le"
        else:
            if ngay >= 1 and ngay <= 28:
                "Hop le"
            else:
                "Khong hop le"
    else:
        "Khong hop le"
else:
    "Khong hop le"

Refactor 2:
if nam > 0:
    if (thang == 1 or thang == 3 ...) and (ngay >= 1 and ngay <= 31):
        "Hop le"
    elif (thang == 4 or thang == 6 ...) and (ngay >= 1 and ngay <= 30):
        "Hop le"
    elif thang == 2:
        if nam nhuận:
            if ngay >= 1 and ngay <= 29:
                "Hop le"
            else:
                "Khong hop le"
        else:
            if ngay >= 1 and ngay <= 28:
                "Hop le"
            else:
                "Khong hop le"
    else:
        "Khong hop le"
else:
    "Khong hop le"

Refactor 3:

max_ngay = -1
if thang == 1 or thang == 3 ...:
    max_ngay = 31
elif thang == 4 or thang == 6 ...:
    max_ngay = 30
else:
    if nam nhuận:
        max_ngay = 29
    else:
        max_ngay = 28

if ngay >= 1 and ngay <= max_ngay and  và thang >= 1 and thang <= 12 and nam > 0:
    "Hợp lệ"
else:
    "Không hợp lệ"