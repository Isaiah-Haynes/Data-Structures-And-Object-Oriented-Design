from Fitting import *

x = [0, 1, 2, 3]
y = [0, 1, 4, 9]


print(fit_data(quad, x, y))
x = [0, 1, 2, 3]
y = [0, 1, 4, 9]
params_expected = [1, 0, 0]
rmse_expected = 0          
params, rmse, y = fit_data(quad, x, y)
#self.assertAlmostEqual(params[0], 1, 3)
#self.assertAlmostEqual(params[1], 0, 3)
#self.assertAlmostEqual(params[2], 0, 3)
#self.assertAlmostEqual(rmse, rmse_expected, 3)
