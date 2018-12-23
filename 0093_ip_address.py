def restoreIpAddresses(s):
    """
    :type s: str
    :rtype: List[str]
    """
    return list(filter(lambda x: is_valid(x), get_children(s)))


def get_children(s):
    """
    :type s: str
    :rtype: List[str]
    """
    if s is None:
        return []  # if the last decimal we tried to add was invalid, this will happen
    if s.count('.') == 3:
        return [s]  # if the decimal count is 3, we are done, just return the string in a list
    else:
        idx = 0
        for index, c in enumerate(s[::-1]):  # look for the last index of '.'
            if c == '.':
                idx = len(s) - index
                break
        # add decimals in all of the next possible locations, and get the children of them
        x = get_children(add_decimal(s, idx + 1))
        x.extend(get_children(add_decimal(s, idx + 2)))
        x.extend(get_children(add_decimal(s, idx + 3)))
        return x


def add_decimal(s, location):
    if len(s) > location:
        return s[:location] + '.' + s[location:]
    else:
        return None


def is_valid(s):
    if s.count('.') != 3:
        return False
    else:
        split = s.split('.')
        for spl in split:
            # check if there are leading zeros on something > 0, or if it's out of range
            if (spl[0] == '0' and len(spl) > 1) or int(spl) > 255 or int(spl) < 0:
                return False
        return True
