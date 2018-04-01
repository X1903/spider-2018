function getA(e) {
    var g = $(e);
    var l = g.attr("itemid")
    a = {}
    a.type = g.attr("ftype")
    a.fileUuid = g.attr("fuid")
    a.model = 'play'
    a.itemId = l
    a.item = undefined
    a.rescUrl = g.attr("rurl")
    a.expireTime = g.attr("extime")
    a.token = g.attr("token")
    a.callBack = g.attr("cbk")
    a.saveAs = g.attr("svs")
    a.resJsCallback = g.attr("rcbk")
    a.custPlayCallBack = undefined
    a.pkg = g.attr("pkg")
    return a
}

function getG(a) {
    var b = a.model,
        c = a.itemId,
        e = a.item,
        f = a.callBack,
        g = a.type,
        l = a.rescUrl,
        n = a.expireTime,
        q = a.token,
        p = a.pkg,
        m = a.pkgItems,
        v = a.saveAs,
        d = a.resJsCallback,
        h = a.vcode;
    g = dfu(g, l, n, q, h, p, v)
    l = "playLog" == b ? !0 : !1
    n = "cache" == b ? !0 : !1
    g.isc = n
    g.ilg = l
    g.pkgItems = m
    return g
}

function getB(g) {
    b = cqbj(g);
    b = $.extend(b, a.gt_captchaResult || {});
    return b
}

function crawl(e) {
    a = getA(e)
    g = getG(a)
    b = getB(g)
    return b
}