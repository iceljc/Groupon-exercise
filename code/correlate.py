from utils import read_data
import numpy as np
from datetime import datetime as dt
import datetime
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

if __name__ == '__main__':
	file = '../Groupon/Q4_2013_Groupon_North_America_Data_XLSX.xlsx'
	
	local_bills, travel_bills, goods_bills, local_sold, travel_sold, goods_sold, \
		local_new_bills, travel_new_bills, goods_new_bills, \
		local_units_new, travel_units_new, goods_units_new, \
		local_prev_bills, travel_prev_bills, goods_prev_bills, \
		local_prev_units, travel_prev_units, goods_prev_units, d1, d2, t1, t2 = read_data(file)


	dates = [t1 + datetime.timedelta(days=x) for x in range(0, (t2-t1).days+1)]

	local_bills_hist, travel_bills_hist, goods_bills_hist = [], [], []
	local_units_hist, travel_units_hist, goods_units_hist = [], [], []

	for d in dates:
		## history
		if d not in local_prev_bills:
			local_bills_hist.append(None)
			local_units_hist.append(None)
		else:
			local_bills_hist.append(sum(local_prev_bills[d]))
			local_units_hist.append(sum(local_prev_units[d]))



	bills = [x for x in local_bills_hist if x is not None]
	units = [[x] for x in local_units_hist if x is not None]

	np.random.seed(42)
	ids = np.random.choice(np.arange(len(bills)), size=len(bills), replace=False)
	print('Number of data: ', len(ids))

	x = np.array(units)[ids]
	y = np.array(bills)[ids]

	print("Building linear model ...")
	lin_model = LinearRegression()
	lin_model.fit(x, y)
	y_pred = lin_model.predict(x)


	print('R_squared score:', lin_model.score(x, y))
	# print('RMSE: ', np.sqrt(mean_squared_error(y, y_pred)))
	print('Model parameters: ', lin_model.coef_, lin_model.intercept_)


	# residual
	res = []
	for i in range(len(y_pred)):
		res.append(y[i] - y_pred[i])

	print('Residual sum: ', sum(res))


	xs = np.array([[0], [230000]])
	ys = lin_model.predict(xs)

	import matplotlib.pyplot as plt

	# fig, ax = plt.subplots(1, 1, figsize=(9,5))
	# ax.scatter(units, bills, label='Raw data (2013)')
	# ax.set_xlabel('Units sold (Local)')
	# ax.set_ylabel('Billings (Local)')
	# ax.legend(loc='upper left')
	# # plt.savefig('lin_reg.png')
	# plt.show()
	# plt.close()

	fig, ax = plt.subplots(1, 1, figsize=(9,5))
	ax.scatter(units, bills, label='Raw data (2013)')
	ax.plot(xs, ys, color='red', label='Fitted line')
	ax.set_xlabel('Units sold (Local)')
	ax.set_ylabel('Billings (Local)')
	ax.legend(loc='upper left')
	plt.savefig('./figs/lin_reg.png')
	# plt.show()
	plt.close()


	fig, ax = plt.subplots(1, 1, figsize=(9,5))
	ax.hist(res, bins=30)
	ax.set_xlabel('Residual')
	ax.set_ylabel('Count')
	plt.savefig('./figs/lin_reg_res.png')
	# plt.show()
	plt.close()







