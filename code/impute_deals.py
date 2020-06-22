from utils import read_data
import numpy as np
from datetime import datetime as dt
import datetime


if __name__ == '__main__':
	file = '../Groupon/Q4_2013_Groupon_North_America_Data_XLSX.xlsx'
	
	local_bills, travel_bills, goods_bills, local_sold, travel_sold, goods_sold, \
		local_new_bills, travel_new_bills, goods_new_bills, \
		local_units_new, travel_units_new, goods_units_new, \
		local_prev_bills, travel_prev_bills, goods_prev_bills, \
		local_prev_units, travel_prev_units, goods_prev_units, d1, d2, t1, t2 = read_data(file)


	dates = [d1 + datetime.timedelta(days=x) for x in range(0, (d2-d1).days+1)]

	local_bills_new_start, travel_bills_new_start, goods_bills_new_start = [],[],[]
	local_units_new_start, travel_units_new_start, goods_units_new_start = [],[],[]
	local_deal_new_start, travel_deal_new_start, goods_deal_new_start = [], [], []

	for d in dates:
		if d not in local_new_bills:
			local_bills_new_start.append(None)
			local_units_new_start.append(None)
			local_deal_new_start.append(None)
		else:
			local_bills_new_start.append(sum(local_new_bills[d]))
			local_units_new_start.append(sum(local_units_new[d]))
			local_deal_new_start.append(len(local_new_bills[d]))


	# Apply linear interpolation
	x1 = 0
	x2 = 12
	y1 = local_deal_new_start[18]
	y2 = local_deal_new_start[30]

	k = (y2 - y1) / (x2 - x1)
	b = y1 - k * x1

	imputed_deal = []
	for x in range(x1+1, x2):
		imputed_deal.append(k*x + b)


	print('Imputed deals sum: ', sum(imputed_deal))

	if 1:
		import matplotlib.pyplot as plt

		xs = np.arange(len(dates))
		fig, ax = plt.subplots(1, 1, figsize=(9,5))
		ax.scatter(xs, local_deal_new_start, label='Raw data')
		ax.set_xlabel('Start dates (10/1/2013 - 12/31/2013)')
		ax.set_ylabel('New start deals number in 4Q13 (Local)')
		ax.legend(loc='upper right')
		plt.savefig('./figs/local_new_deals_raw.png')
		# plt.show()
		plt.close()


		fig, ax = plt.subplots(1, 1, figsize=(9,5))
		ax.scatter(xs, local_deal_new_start, label='Raw data')
		ax.scatter(np.arange(19, 30), imputed_deal, c='red', label='Imputed data')
		ax.set_xlabel('Start dates (10/1/2013 - 12/31/2013)')
		ax.set_ylabel('New start deals number in 4Q13 (Local)')
		ax.legend(loc='upper right')
		plt.savefig('./figs/local_new_deals.png')
		# plt.show()
		plt.close()









