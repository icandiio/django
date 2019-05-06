def increase(dic, k, k2str=False, prefix=""):
    if k2str:
        k = "%s%s" % (prefix, k)
    dic.update({k: dic.get(k) + 1}) if k in dic else dic.update({k: 1})
