from utils import read_data
from datetime import datetime as dt
import datetime
import collections
import numpy as np


if __name__ == '__main__':

	file = '../Groupon/Q4_2013_Groupon_North_America_Data_XLSX.xlsx'
	
	local_bills, travel_bills, goods_bills, local_sold, travel_sold, goods_sold, \
		local_new_bills, travel_new_bills, goods_new_bills, \
		local_units_new, travel_units_new, goods_units_new, \
		local_prev_bills, travel_prev_bills, goods_prev_bills, \
		local_prev_units, travel_prev_units, goods_prev_units, d1, d2, t1, t2 = read_data(file)

	print('Local bills: ', len(local_bills))
	print('Travel bills: ', len(travel_bills))
	print('Goods bills: ', len(goods_bills))
	print('Total bills: ', len(local_bills)+len(travel_bills)+len(goods_bills))

	print()

	print('Local bill sum: ', sum(local_bills)*1e-6)
	print('Travel bill sum: ', sum(travel_bills)*1e-6)
	print('Goods bill sum: ', sum(goods_bills)*1e-6)
	print('Sum: ', (sum(local_bills) + sum(travel_bills) + sum(goods_bills))*1e-6)

	print()

	print('Local units sold: ', sum(local_sold))
	print('Travel units sold: ', sum(travel_sold))
	print('Goods units sold: ', sum(goods_sold))
	print('Total units sold: ', sum(local_sold) + sum(travel_sold) + sum(goods_sold))


	# Q1-Q4 2013
	dates = [t1 + datetime.timedelta(days=x) for x in range(0, (t2-t1).days+1)]
	# Q4 2013
	dates_4q = [d1 + datetime.timedelta(days=x) for x in range(0, (d2-d1).days+1)]

	local_bills_new_start, travel_bills_new_start, goods_bills_new_start = [],[],[]
	local_units_new_start, travel_units_new_start, goods_units_new_start = [],[],[]
	local_deal_new_start, travel_deal_new_start, goods_deal_new_start = [], [], []

	local_bills_hist, travel_bills_hist, goods_bills_hist = [], [], []
	local_units_hist, travel_units_hist, goods_units_hist = [], [], []

	for d in dates_4q:
		if d not in local_new_bills:
			local_bills_new_start.append(None)
			local_units_new_start.append(None)
			local_deal_new_start.append(None)
		else:
			local_bills_new_start.append(sum(local_new_bills[d]))
			local_units_new_start.append(sum(local_units_new[d]))
			local_deal_new_start.append(len(local_new_bills[d]))

		if d not in travel_new_bills:
			travel_bills_new_start.append(None)
			travel_units_new_start.append(None)
			travel_deal_new_start.append(None)
		else:
			travel_bills_new_start.append(sum(travel_new_bills[d]))
			travel_units_new_start.append(sum(travel_units_new[d]))
			travel_deal_new_start.append(len(travel_new_bills[d]))

		if d not in goods_new_bills:
			goods_bills_new_start.append(None)
			goods_units_new_start.append(None)
			goods_deal_new_start.append(None)
		else:
			goods_bills_new_start.append(sum(goods_new_bills[d]))
			goods_units_new_start.append(sum(goods_units_new[d]))
			goods_deal_new_start.append(len(goods_new_bills[d]))


	for d in dates:
		## history
		if d not in local_prev_bills:
			local_bills_hist.append(None)
			local_units_hist.append(None)
		else:
			local_bills_hist.append(sum(local_prev_bills[d]))
			local_units_hist.append(sum(local_prev_units[d]))

		if d not in travel_prev_bills:
			travel_bills_hist.append(None)
			travel_units_hist.append(None)
		else:
			travel_bills_hist.append(sum(travel_prev_bills[d]))
			travel_units_hist.append(sum(travel_prev_units[d]))

		if d not in goods_prev_bills:
			goods_bills_hist.append(None)
			goods_units_hist.append(None)
		else:
			goods_bills_hist.append(sum(goods_prev_bills[d]))
			goods_units_hist.append(sum(goods_prev_units[d]))


	import matplotlib.pyplot as plt

	if 0:
		fig, ax = plt.subplots(1, 1, figsize=(9,5))
		ax.scatter(local_sold, local_bills, label='Raw data (Local)')
		ax.set_xlabel('Units sold (Local)')
		ax.set_ylabel('Billings (Local)')
		ax.legend(loc='best')
		plt.savefig('./figs/local_bill_unit_raw.png')
		# plt.show()
		plt.close()

		fig, ax = plt.subplots(1, 1, figsize=(9,5))
		ax.scatter(goods_sold, goods_bills, label='Raw data (Goods)')
		ax.set_xlabel('Units sold (Goods)')
		ax.set_ylabel('Billings (Goods)')
		ax.legend(loc='best')
		plt.savefig('./figs/goods_bill_unit_raw.png')
		# plt.show()
		plt.close()

		fig, ax = plt.subplots(1, 1, figsize=(9,5))
		ax.scatter(travel_sold, travel_bills, label='Raw data (Travel)')
		ax.set_xlabel('Units sold (Travel)')
		ax.set_ylabel('Billings (Travel)')
		ax.legend(loc='best')
		plt.savefig('./figs/travel_bill_unit_raw.png')
		# plt.show()
		plt.close()

	# plot Q4 - 2013
	# local
	if 0:
		# ts = np.arange(len(dates_4q))
		# fig, ax = plt.subplots(1, 1, figsize=(9,5))
		# ax.plot(ts, local_bills_new_start, marker='o')
		# ax.set_xlabel('Start dates (10/1/2013 - 12/31/2013)')
		# ax.set_ylabel('Billings (Local)')
		# # plt.savefig('./figs2/local_units_hist.png')
		# plt.show()
		# plt.close()

		# fig, ax = plt.subplots(1, 1, figsize=(9,5))
		# ax.plot(ts, local_units_new_start, marker='o')
		# ax.set_xlabel('Start dates (10/1/2013 - 12/31/2013)')
		# ax.set_ylabel('Units sold (Local)')
		# # plt.savefig('./figs2/local_units_hist.png')
		# plt.show()
		# plt.close()


		xs = np.arange(len(dates))
		fig, ax = plt.subplots(1, 1, figsize=(9,5))
		ax.plot(xs, local_bills_hist, marker='o')
		ax.set_xlabel('Start dates (1/1/2013 - 12/31/2013)')
		ax.set_ylabel('Billings (Local)')
		plt.savefig('./figs/local_bills_hist.png')
		# plt.show()
		plt.close()

		fig, ax = plt.subplots(1, 1, figsize=(9,5))
		ax.plot(xs, local_units_hist, marker='o')
		ax.set_xlabel('Start dates (1/1/2013 - 12/31/2013)')
		ax.set_ylabel('Units sold (Local)')
		plt.savefig('./figs/local_units_hist.png')
		# plt.show()
		plt.close()

		fig, ax = plt.subplots(1, 1, figsize=(9,5))
		ax.scatter(local_units_hist, local_bills_hist)
		ax.set_xlabel('Units sold (Local)')
		ax.set_ylabel('Billings (Local)')
		plt.savefig('./figs/local_units_vs_bills_hist.png')
		# plt.show()
		plt.close()


	if 0:
		ts = np.arange(len(dates_4q))
		fig, ax = plt.subplots(1, 1, figsize=(9,5))
		ax.plot(ts, travel_bills_new_start, marker='o')
		ax.set_xlabel('Start dates (10/1/2013 - 12/31/2013)')
		ax.set_ylabel('Billings (Travel)')
		# plt.savefig('./figs2/local_units_hist.png')
		plt.show()
		plt.close()

		fig, ax = plt.subplots(1, 1, figsize=(9,5))
		ax.plot(ts, travel_units_new_start, marker='o')
		ax.set_xlabel('Start dates (10/1/2013 - 12/31/2013)')
		ax.set_ylabel('Units sold (Travel)')
		# plt.savefig('./figs2/local_units_hist.png')
		plt.show()
		plt.close()


		# xs = np.arange(len(dates))
		# fig, ax = plt.subplots(1, 1, figsize=(9,5))
		# ax.plot(xs, travel_bills_hist, marker='o')
		# ax.set_xlabel('Start dates (1/1/2013 - 12/31/2013)')
		# ax.set_ylabel('Billings (Travel)')
		# # plt.savefig('./figs2/local_units_hist.png')
		# plt.show()
		# plt.close()

		# fig, ax = plt.subplots(1, 1, figsize=(9,5))
		# ax.plot(xs, travel_units_hist, marker='o')
		# ax.set_xlabel('Start dates (1/1/2013 - 12/31/2013)')
		# ax.set_ylabel('Units sold (Travel)')
		# # plt.savefig('./figs2/local_units_hist.png')
		# plt.show()
		# plt.close()


	if 0:
		ts = np.arange(len(dates_4q))
		fig, ax = plt.subplots(1, 1, figsize=(9,5))
		ax.plot(ts, goods_bills_new_start, marker='o')
		ax.set_xlabel('Start dates (10/1/2013 - 12/31/2013)')
		ax.set_ylabel('Billings (Goods)')
		# plt.savefig('./figs2/local_units_hist.png')
		plt.show()
		plt.close()

		fig, ax = plt.subplots(1, 1, figsize=(9,5))
		ax.plot(ts, goods_units_new_start, marker='o')
		ax.set_xlabel('Start dates (10/1/2013 - 12/31/2013)')
		ax.set_ylabel('Units sold (Goods)')
		# plt.savefig('./figs2/local_units_hist.png')
		plt.show()
		plt.close()


		# xs = np.arange(len(dates))
		# fig, ax = plt.subplots(1, 1, figsize=(9,5))
		# ax.plot(xs, goods_bills_hist, marker='o')
		# ax.set_xlabel('Start dates (1/1/2013 - 12/31/2013)')
		# ax.set_ylabel('Billings (Goods)')
		# # plt.savefig('./figs2/local_units_hist.png')
		# plt.show()
		# plt.close()

		# fig, ax = plt.subplots(1, 1, figsize=(9,5))
		# ax.plot(xs, goods_units_hist, marker='o')
		# ax.set_xlabel('Start dates (1/1/2013 - 12/31/2013)')
		# ax.set_ylabel('Units sold (Goods)')
		# # plt.savefig('./figs2/local_units_hist.png')
		# plt.show()
		# plt.close()











