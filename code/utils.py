import pandas as pd
import xlrd
from datetime import datetime as dt
import datetime
import collections
import numpy as np

# read data from csv file and output according to segments

def read_data(file):
	data = pd.read_excel(file, sheet_name='Q4 2013 Raw Data')
	df = pd.DataFrame(data)

	local_bills, travel_bills, goods_bills = [], [], []
	local_sold, travel_sold, goods_sold = [], [], []
	data_len = df.shape[0]
	local_pos_bills = []
	pos, neg = 0, 0

	date_time1 = dt.strptime('2013-10-20', '%Y-%m-%d')
	date_time2 = dt.strptime('2013-10-30', '%Y-%m-%d')
	local_miss, travel_miss, goods_miss = 0, 0, 0

	new_local, new_travel, new_goods = 0, 0, 0
	d1 = dt.strptime('2013-10-1', '%Y-%m-%d')
	d2 = dt.strptime('2013-12-31', '%Y-%m-%d')

	local_new_bills = collections.defaultdict(list)
	travel_new_bills = collections.defaultdict(list)
	goods_new_bills = collections.defaultdict(list)

	local_units_new = collections.defaultdict(list)
	travel_units_new = collections.defaultdict(list)
	goods_units_new = collections.defaultdict(list)

	t1 = dt.strptime('2013-1-1', '%Y-%m-%d')
	t2 = dt.strptime('2013-12-31', '%Y-%m-%d')
	local_prev_bills = collections.defaultdict(list)
	travel_prev_bills = collections.defaultdict(list)
	goods_prev_bills = collections.defaultdict(list)

	local_prev_units = collections.defaultdict(list)
	travel_prev_units = collections.defaultdict(list)
	goods_prev_units = collections.defaultdict(list)

	x1 = dt.strptime('2013-10-1', '%Y-%m-%d')
	x2 = dt.strptime('2013-10-31', '%Y-%m-%d')
	x3 = dt.strptime('2013-11-30', '%Y-%m-%d')
	x4 = dt.strptime('2013-12-31', '%Y-%m-%d')

	local_oct, local_nov, local_dec = 0, 0, 0

	for i in range(data_len):
		# print(df['Start Date'][i].month)

		if df['Segment'][i] == 'Local':
			local_bills.append(df['Billings'][i])
			local_sold.append(df['Units Sold'][i])
			
			if df['Start Date'][i] >= date_time1 and df['Start Date'][i] <= date_time2:
				local_miss += 1

			if df['Start Date'][i] >= d1 and df['Start Date'][i] <= d2:
				new_local += 1
				local_new_bills[df['Start Date'][i]].append(df['Billings'][i])
				local_units_new[df['Start Date'][i]].append(df['Units Sold'][i])

			if df['Billings'][i] > 0:
				local_pos_bills.append(df['Billings'][i])
				pos += 1
			else:
				neg += 1

			if df['Start Date'][i] >= t1 and df['Start Date'][i] <= t2:
				local_prev_bills[df['Start Date'][i]].append(df['Billings'][i])
				local_prev_units[df['Start Date'][i]].append(df['Units Sold'][i])

			if df['Start Date'][i] >= x1 and df['Start Date'][i] <= x2:
				local_oct += 1
			elif df['Start Date'][i] > x2 and df['Start Date'][i] <= x3:
				local_nov += 1
			elif df['Start Date'][i] > x3 and df['Start Date'][i] <= x4:
				local_dec += 1
			
			# if df['Start Date'][i] == dt.strptime('2013-1-2', '%Y-%m-%d'):
			# 	count += 1

		elif df['Segment'][i] == 'Travel':
			travel_bills.append(df['Billings'][i])
			travel_sold.append(df['Units Sold'][i])
			if df['Start Date'][i] >= date_time1 and df['Start Date'][i] <= date_time2:
				travel_miss += 1

			if df['Start Date'][i] >= d1 and df['Start Date'][i] <= d2:
				new_travel += 1
				travel_new_bills[df['Start Date'][i]].append(df['Billings'][i])
				travel_units_new[df['Start Date'][i]].append(df['Units Sold'][i])

			if df['Start Date'][i] >= t1 and df['Start Date'][i] <= t2:
				travel_prev_bills[df['Start Date'][i]].append(df['Billings'][i])
				travel_prev_units[df['Start Date'][i]].append(df['Units Sold'][i])

		elif df['Segment'][i] == 'Goods':
			goods_bills.append(df['Billings'][i])
			goods_sold.append(df['Units Sold'][i])
			if df['Start Date'][i] >= date_time1 and df['Start Date'][i] <= date_time2:
				goods_miss += 1
				# print(df['Start Date'][i], df['Segment'][i], df['Billings'][i], df['Inventory Type'][i])

			if df['Start Date'][i] >= d1 and df['Start Date'][i] <= d2:
				new_goods += 1
				goods_new_bills[df['Start Date'][i]].append(df['Billings'][i])
				goods_units_new[df['Start Date'][i]].append(df['Units Sold'][i])

			if df['Start Date'][i] >= t1 and df['Start Date'][i] <= t2:
				goods_prev_bills[df['Start Date'][i]].append(df['Billings'][i])
				goods_prev_units[df['Start Date'][i]].append(df['Units Sold'][i])


	print('New start deals (Local): ', new_local)
	print('New start deals (Travel): ', new_travel)
	print('New start deals (Goods): ', new_goods)
	print('New start deals (Total): ', new_local + new_travel + new_goods)

	return local_bills, travel_bills, goods_bills, local_sold, travel_sold, goods_sold, \
			local_new_bills, travel_new_bills, goods_new_bills, \
			local_units_new, travel_units_new, goods_units_new, \
			local_prev_bills, travel_prev_bills, goods_prev_bills, \
			local_prev_units, travel_prev_units, goods_prev_units, \
			d1, d2, t1, t2


def read_history_bills():
	local_hist_bills = [[133.414773040001, 137.32169341, 138.2], [126.8, 139.9, 164.4],
						[162.7, 143, 163.4], [143.8, 162.2, 153.2], 
						[139.951253500419, 136.667939635306, 133.795040003333]]
	goods_hist_bills = [[26.73390913, 33.0089146900001, 50.8], [64.3, 85.1, 64.3], 
						[47.3, 46, 51], [62.8, 71.7, 67.1], 
						[61.2799836759975, 67.0249821456223, 63.1949831658725]]
	travel_hist_bills = [[16.77076593, 15.43664508, 14.3], [16.6, 14.6, 18.5], 
						[22.6, 13.6, 20.3], [18.9, 22.9, 22.8], 
						[22.404491599, 22.738886996, 21.735700805]]

	length = len(local_hist_bills)
	local_quarter_bills, goods_quarter_bills, travel_quarter_bills = [], [], []

	for i in range(length):
		local_quarter_bills.append(sum(local_hist_bills[i]))
		goods_quarter_bills.append(sum(goods_hist_bills[i]))
		travel_quarter_bills.append(sum(travel_hist_bills[i]))
		
		# print('='*10)
		# for j in range(len(local_hist_bills[i])):
		# 	local = local_hist_bills[i][j]
		# 	goods = goods_hist_bills[i][j]
		# 	travel = travel_hist_bills[i][j]
		# 	s = local + goods + travel
		# 	print(local/s*100, goods/s*100, travel/s*100)


	quarter_bills = []
	for i in range(length):
		quarter_bills.append(local_quarter_bills[i] + goods_quarter_bills[i] + travel_quarter_bills[i])


	# print(local_quarter_bills)
	# print(quarter_bills)
	return local_quarter_bills, goods_quarter_bills, travel_quarter_bills, quarter_bills


def read_history_sold_units():
	local_hist_sold = [[4400800.10000015, 4233714.74000015, 4991814.5900003], 
						[5177435.73000021, 4920379.3800001, 5502182.2500001], 
						[5330316.29726036, 4823771.58353314, 5530983.02738704], 
						[4807696.58068375, 5592799.03939435, 5755797.88019551], 
						[4996243.06950783, 4902360.84446155, 4967460.86742924]]
	goods_hist_sold = [[855156.18, 1162884.17, 1629823.06000001], 
						[1879696.70000002, 2583171.53000003, 1915783.55000002], 
						[1596737.74000001, 1491286.16, 1685055.23], 
						[2470160.52000001, 2726325.92000002, 2651338.24000003], 
						[2267942.73401611, 2471564.28926946, 2346841.51157256]]
	travel_hist_sold = [[61283.3600000001, 84984.5499999999, 60253.49], 
						[74358.37, 87332.5699999999, 93702.5999999998], 
						[84821.4899999999, 55029.8100000001, 84685.82], 
						[102090.52, 144592.28, 142509.04], 
						[103020.751007052, 108411.787686473, 105751.941380432]]

	length = len(local_hist_sold)
	local_quarter_sold, goods_quarter_sold, travel_quarter_sold = [], [], []

	for i in range(length):
		local_quarter_sold.append(sum(local_hist_sold[i]))
		goods_quarter_sold.append(sum(goods_hist_sold[i]))
		travel_quarter_sold.append(sum(travel_hist_sold[i]))


	quarter_sold = []
	for i in range(length):
		quarter_sold.append(local_quarter_sold[i] + goods_quarter_sold[i] + travel_quarter_sold[i])

	
	return local_quarter_sold, goods_quarter_sold, travel_quarter_sold, quarter_sold



def read_history_new_start_deal():
	local_hist_new_start = [[13543, 12926, 12814], [14544, 13914, 15374], 
							[12375, 11846, 13041], [10790, 14281, 13815], 
							[14173, 13075, 10670]]
	goods_hist_new_start = [[334, 448, 525], [770, 1079, 1310], 
							[992, 1197, 1499], [1755, 2185, 2610], 
							[2796, 2887, 2847]]
	travel_hist_new_start = [[211, 277, 217], [262, 270, 334], 
							[243, 188, 205], [329, 471, 458], 
							[506, 537, 571]]

	length = len(local_hist_new_start)
	local_quarter_new, goods_quarter_new, travel_quarter_new = [], [], []

	for i in range(length):
		local_quarter_new.append(sum(local_hist_new_start[i]))
		goods_quarter_new.append(sum(goods_hist_new_start[i]))
		travel_quarter_new.append(sum(travel_hist_new_start[i]))

	quarter_new_start = []
	for i in range(length):
		quarter_new_start.append(local_quarter_new[i] + goods_quarter_new[i] + travel_quarter_new[i])

	

	return local_quarter_new, goods_quarter_new, travel_quarter_new, quarter_new_start


