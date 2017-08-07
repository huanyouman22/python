#!/usr/bin/python
#coding=utf-8
import xlsxwriter

workbook = xlsxwriter.Workbook('demo1.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A',20)
bold = workbook.add_format({'bold':True})

worksheet.write('A1','hello')
worksheet.write('A2','world',bold)
worksheet.write('B2',u'中文测试',bold)
worksheet.write(2,0,32)
worksheet.write(3,0,32.5)
worksheet.write(4,0,'=SUM(A3:A4)')

worksheet.insert_image('B5','cpu_time.png')


chart = workbook.add_chart({type,'line'})
workshet.insert_chart("C10",chart)
chart.add_series({
	'categories':'=Sheet1!$A$1:$A$5',
	'values':'=Sheet1!$A$1:$A$5',
	'line':{'color':'red'},
	})

chart.set_x_axis({
	'name':'Earning per Quqrter',
	'name_font':'{'size':'14px','bold':True}'
	'num_font':'{'italic':True}'
	})
