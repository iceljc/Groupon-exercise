from utils import read_data
import numpy as np
from datetime import datetime as dt
import datetime
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# build polynomial regression model on units
# fill up missing units and billings

if __name__ == '__main__':
	file = '../Groupon/Q4_2013_Groupon_North_America_Data_XLSX.xlsx'
	
	local_bills, travel_bills, goods_bills, local_sold, travel_sold, goods_sold, \
		local_new_bills, travel_new_bills, goods_new_bills, \
		local_units_new, travel_units_new, goods_units_new, \
		local_prev_bills, travel_prev_bills, goods_prev_bills, \
		local_prev_units, travel_prev_units, goods_prev_units, d1, d2, t1, t2 = read_data(file)


	dates = [t1 + datetime.timedelta(days=x) for x in range(0, (t2-t1).days+1)]
	dates_4q = [d1 + datetime.timedelta(days=x) for x in range(0, (d2-d1).days+1)]


	ts = []
	local_units_prev = []
	for i in range(len(dates)):
		if dates[i] in local_prev_bills and sum(local_prev_units[dates[i]]) > 0:
			ts.append(i)
			local_units_prev.append(np.log(sum(local_prev_units[dates[i]])))


	local_bills_new_start, local_units_new_start = [], []
	for d in dates_4q:
		if d not in local_new_bills:
			local_bills_new_start.append(None)
			local_units_new_start.append(None)
		else:
			local_bills_new_start.append(sum(local_new_bills[d]))
			local_units_new_start.append(sum(local_units_new[d]))


	if 0:
		import matplotlib.pyplot as plt
		fig, ax = plt.subplots(1, 1, figsize=(9,5))
		ax.scatter(ts, local_units_prev)
		ax.set_xlabel('Start dates (1/1/2013 - 12/31/2013)')
		ax.set_ylabel('log(Units sold) (Local)')
		plt.savefig('./figs/local_units_date_raw.png')
		# plt.show()
		plt.close()




	# cut the leanding and trailing points
	ts = ts[50:310]
	local_units_prev = local_units_prev[50:310]

	np.random.seed(42)
	ids = np.random.choice(np.arange(len(ts)), size=len(ts), replace=False)

	# split train and test set
	split = 0.8
	ids_train = ids[:int(np.floor(split*len(ids)))]
	ids_test = ids[int(np.floor(split*len(ids))):]

	print('Number of total points: ', len(ids))
	print('Number of training points: ', len(ids_train))
	print('Number of test points: ', len(ids_test))

	print("Training polynomial regression model...")
	x_train = np.array([[x] for x in ts])[ids_train]
	y_train = np.array([y for y in local_units_prev])[ids_train]

	x_test = np.array([[x] for x in ts])[ids_test]
	y_test = np.array([y for y in local_units_prev])[ids_test]

	poly = PolynomialFeatures(degree=6)
	x_train_poly = poly.fit_transform(x_train)

	model = LinearRegression()
	model.fit(x_train_poly, y_train)

	y_train_pred = model.predict(x_train_poly)

	print('Train R-squared: ', model.score(x_train_poly, y_train))
	print('Train RMSE: ', np.sqrt(mean_squared_error(y_train, y_train_pred)))

	errors = []
	for i in range(len(y_train)):
		errors.append(y_train[i] - y_train_pred[i])

	print('Average error: ', sum(errors) / len(errors))

	# Model evaluation
	x_test_poly = poly.fit_transform(x_test)
	y_test_pred = model.predict(x_test_poly)
	r2_test = r2_score(y_test, y_test_pred)
	rmse_test = np.sqrt(mean_squared_error(y_test, y_test_pred))
	print('Test R-sqaured: ', r2_test)
	print('Test RMSE: ', rmse_test)


	# Impute missing data
	t_miss = np.arange(292, 303)
	t_miss = np.array([[t] for t in t_miss])
	x_poly_miss = poly.fit_transform(t_miss)

	y_miss = model.predict(x_poly_miss)
	units_impute = []
	bills_impute = []

	# get the correlation from linear regression model of bills and units, (correlate.py)
	k = 25.28195355
	c = 144066.24059898686

	for y in y_miss:
		units_impute.append(np.exp(y))
		bills_impute.append(k*np.exp(y) + c)

	print('Imputed billings of Local (sum): ', sum(bills_impute)*1e-6)
	print('Imputed units of Local (sum): ', sum(units_impute))

	

	if 0:
		# print(dates[50], dates[309])
		x = np.arange(50, 320)
		x = np.array([[d] for d in x])
		x_poly = poly.fit_transform(x)
		y_pred = model.predict(x_poly)

		import matplotlib.pyplot as plt
		fig, ax = plt.subplots(1, 1, figsize=(9,5))
		ax.scatter(ts, local_units_prev, label='Raw data')
		ax.plot(x, y_pred, color='red', label='Regression model (degree=6)')
		ax.set_xlabel('Start dates (2/20/2013 - 11/6/2013)')
		ax.set_ylabel('log(Units sold) (Local)')
		ax.legend(loc='best')
		plt.savefig('./figs/local_units_date_fit.png')
		# plt.show()
		plt.close()

	if 0:
		import matplotlib.pyplot as plt

		s = dates.index(dt.strptime('2013-10-1', '%Y-%m-%d'))
		e = dates.index(dt.strptime('2013-12-31', '%Y-%m-%d'))

		xs = np.arange(s, e+1)
		fig, ax = plt.subplots(1, 1, figsize=(9,5))
		ax.scatter(xs, local_units_new_start, label='Raw data')
		ax.scatter(np.arange(s+19, s+30), units_impute, c='red', label='Imputed data')
		ax.set_xlabel('Start dates (10/1/2013 - 12/31/2013)')
		ax.set_ylabel('Units sold (Local)')
		ax.legend(loc='best')
		plt.savefig('./figs/local_units_imputed.png')
		# plt.show()
		plt.close()


		fig, ax = plt.subplots(1, 1, figsize=(9,5))
		ax.scatter(xs, local_bills_new_start, label='Raw data')
		ax.scatter(np.arange(s+19, s+30), bills_impute, c='red', label='Imputed data')
		ax.set_xlabel('Start dates (10/1/2013 - 12/31/2013)')
		ax.set_ylabel('Billings (Local)')
		ax.legend(loc='best')
		plt.savefig('./figs/local_bills_imputed.png')
		# plt.show()
		plt.close()










