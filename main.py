"""
simple pandas script to calcualte monthly rent amounts.

see desc.txt or readme.md for a description

"""

import calendar
import pandas as pd, numpy as np


__input__ = 'template example.xlsx'
__output__ = 'output example.xlsx'



def normalize(l):
    # normalize list on float on sum 
    return [i/sum(l) for i in l]



def main():

    df = pd.read_excel(__input__).set_index('members', drop = True)
    df.columns = [item for item in df.columns]

    metrics = pd.read_excel(__input__, names = ['metric', 'value'], header = None, sheet_name = 1).set_index('metric').value


    month_map = df[[item for item in df.columns if item in calendar.month_name]]

    prorate_map = (month_map.transpose()*df.prorate_factor).transpose()
    prorate_map = prorate_map.apply(normalize)

    prorated_rent = prorate_map*metrics.monthly_rent

    credit_series = -prorate_map[metrics.credit_month_applied]*metrics.credit

    prorated_rent[metrics.credit_month_applied] += credit_series


    avg_col = prorated_rent.replace(0, np.NaN).mean(axis = 1)
    avg_row = prorated_rent.replace(0, np.NaN).mean()
    prorated_rent.loc['TOTAL'] = prorated_rent.sum()
    prorated_rent['TOTAL'] = prorated_rent.sum(axis = 1)
    prorated_rent.loc['(present average)'] = avg_row
    prorated_rent['(active average)'] = avg_col


    with pd.ExcelWriter(__output__) as writer:
        prorated_rent.to_excel(writer, sheet_name = 'prorated rent')



if __name__ == '__main__':

    with open('desc.txt') as f:
        print(f.read())

    main()