def getOrdinal(n): return "%d%s" % (
    n, {1: "<sup>st</sup>", 2: "<sup>nd</sup>", 3: "<sup>rd</sup>"}.get(n if n < 20 else n % 10, "<sup>th</sup>"))
