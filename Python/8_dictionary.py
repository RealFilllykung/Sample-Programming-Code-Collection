#อารมณ์ประมาณ structure ในภาษา programming อื่นๆ

engToThaiMonth = {
    "Jan": "ม.ค.",
    "Feb": "ก.พ.",
    "Mar": "มี.ค.",
    "Apr": "เม.ย.",
    "May": "พ.ค.",
    "Jun": "มิ.ย.",
    "Jul": "ก.ค.",
    "Aug": "ส.ค.",
    "Sep": "ก.ย.",
    "Oct": "ต.ค.",
    "Nov": "พ.ย.",
    "Dec": "ธ.ค."
}

print(engToThaiMonth["Jan"])
print(engToThaiMonth.get("Feb"))
print(engToThaiMonth.get("Mac","Not found in dictionary"))