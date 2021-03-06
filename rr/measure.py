import datetime
import statistics

class RR(object):

    def __init__(self):
        self.rates = []
        self.last_breath = None

    def breath(self):
        now_breath = datetime.datetime.now()
        if self.last_breath is not None:
            self.rates.append(now_breath - self.last_breath)

        self.last_breath = now_breath

    def __str__(self):

        if len(self.rates) == 0:
            rr = 0
        else:
            sum_of_rates = 0
            for r in self.rates:
                sum_of_rates += 60/r.total_seconds()
            rr = sum_of_rates / len(self.rates)

        comment = "Too fast" if rr > 30 else "Normal"

        if rr == 0:
            return "Average RR: --"
        else:
            return "Average RR: {:2.2f} ({})".format(rr, comment)


