from utils import read_data, read_history_bills, read_history_sold_units, read_history_new_start_deal
import numpy as np


def plot_history(quarter_data, quarters, y_label='Billings (Local)'):

	import matplotlib.pyplot as plt
	fig, ax = plt.subplots(1, 1, figsize=(9,5))
	ax.plot(quarters, quarter_data, marker='o')
	ax.set_xlabel('Quarters')
	ax.set_ylabel(y_label)
	plt.xticks(quarters, ['Q3-2012', 'Q4-2012', 'Q1-2013', 'Q2-2013', 'Q3-2013', 'Q4-2013'])
	# plt.savefig(save_name)
	plt.show()
	plt.close()


if __name__ == '__main__':
	local_quarter_bills, goods_quarter_bills, travel_quarter_bills, quarter_bills = read_history_bills()
	local_quarter_sold, goods_quarter_sold, travel_quarter_sold, quarter_sold = read_history_sold_units()
	local_quarter_new, goods_quarter_new, travel_quarter_new, quarter_new_start = read_history_new_start_deal()

	quarters = np.arange(6)
	# add 4Q13 data
	local_quarter_bills.append(409.2226579820464 + 38.34288229075689)
	goods_quarter_bills.append(282.2456710413219)
	travel_quarter_bills.append(70.55206212449978)
	quarter_bills.append(762.0203911478682 + 38.34288229075689)

	local_quarter_sold.append(13924480.251348432 + 1453928.5333101973)
	goods_quarter_sold.append(10419746.304000074)
	travel_quarter_sold.append(378910.20000000077)
	quarter_sold.append(24723136.755348507 + 1453928.5333101973)

	local_quarter_new.append(46980 + 6974)
	goods_quarter_new.append(12749)
	travel_quarter_new.append(2177)
	quarter_new_start.append(61906 + 6974)

	# plot billings quarter history 
	if 0:
		plot_history(local_quarter_bills, quarters, y_label='Billings in million (Local)')
		plot_history(goods_quarter_bills, quarters, y_label='Billings in million (Goods)')
		plot_history(travel_quarter_bills, quarters, y_label='Billings in million (Travel)')
		plot_history(quarter_bills, quarters, y_label='Billings in million (Total)')

	# plot units quarter history 
	if 0:
		plot_history(local_quarter_sold, quarters, y_label='Units sold (Local)')
		plot_history(goods_quarter_sold, quarters, y_label='Units sold (Goods)')
		plot_history(travel_quarter_sold, quarters, y_label='Units sold (Travel)')
		plot_history(quarter_sold, quarters, y_label='Units sold (Total)')

	# plot new deals quarter history 
	if 0:
		plot_history(local_quarter_new, quarters, y_label='New start deals (Local)')
		plot_history(goods_quarter_new, quarters, y_label='New start deals (Goods)')
		plot_history(travel_quarter_new, quarters, y_label='New start deals (Travel)')
		plot_history(quarter_new_start, quarters, y_label='New start deals (Total)')






