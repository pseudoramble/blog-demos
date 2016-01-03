from datetime import date

from NAV import NAV

def navOf(ticker, date):
    if date and date.year > 2014:
        return NAV(ticker, 71.80)
    else:
        return NAV(ticker, 70.87)

if __name__ == '__main__':
    ticker = 'FUSEX'
    nav_2014 = navOf(ticker, date(2014, 12, 31))
    nav_2015 = navOf(ticker, date(2015, 12, 31))

    print('For the ticker %s:' % ticker)
    
    if nav_2015 < nav_2014:
        print('\tAt a NAV of %s (versus %s), 2014 was a better year than 2015' % (nav_2014, nav_2015))
    else:
        print('\tAt a NAV of %s (versus %s), 2015 was a better year than 2014' % (nav_2015, nav_2014))

    shares = 1000000
    total_value = nav_2015 * shares

    print('\tWith %d shares of %s, the total value of your holdings are $%.2f' % (shares, ticker, total_value))
