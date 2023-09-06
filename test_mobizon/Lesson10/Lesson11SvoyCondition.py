


def all_sended_sms(locator, number):

    def _predicate(dr):
        allsms = dr.find_elements(*locator)
        if len(allsms) == number:
            return allsms

    return _predicate

