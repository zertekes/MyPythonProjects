exam_st_date = (3, 7, 2018)
day = exam_st_date[0]
month = exam_st_date[1]
year = exam_st_date[-1]
print ('The examination will start from: %i/%i/%i'%exam_st_date )
print (f'The day: {day}' )
print (f'The month: {month}')
print (f'The year: {year}')
new_day = int(input('Please give a new day for the exam: '))
new_month = int(input('Please give a new month for the exam: '))
new_year = int(input('Please give a new year for the exam: '))
new_exam_st_date = (new_day, new_month, new_year)
print ('The examination will start from: %i/%i/%i'%new_exam_st_date )