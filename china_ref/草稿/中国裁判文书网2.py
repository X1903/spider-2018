var _xxcc = '<<(i%h))}e d}f p(7){9 d=0;k(9 i=0;i<7.l;i++){d+=(7.g(i)<<(i%h))+i}e d}f t(7,j){9 d=0;k(9 i=0;i<7.l;i++){d+=(7.g(i)<<(i%h))+(i*j)}e d}f s(7,j){9 d=0;k(9 i=0;i<7.l;i++){d+=(7.g(i)<<(i%h))+(i+j-7.g(i))}e d}f r(7){9 7=7.8(5,5*5)+7.8((5+1)*(5+1),3);9 a=7.8(5)+7.8(-4);9 b=7.8(4)+a.8(-6);e n('
var _amaa = 'makeKey_'
var _ama2 = '2'
var _1 = '5'
var _2 = '(7)'
var _23 = '(6)'

def makeKey_9(str):
    var str = str.substr(5, 5 * 5) + "5" + str.substr(1, 2) + "1" + str.substr((5 + 1) * (5 + 1), 3)
    var a = str.substr(5) + str.substr(4)
    var b = str.substr(12) + a.substr(-6)
    var c = hex_sha1(str.substr(4)) + a.substr(6)
    return hex_md5(c).substr(4, 24)


def makeKey_10(str):
    var base = new Base64()
    var str = base.encode(str.substr(5, 5 * 5 - 1) + "5") + str.substr(1, 2) + str.substr((5 + 1) * (5 + 1), 3)
    var long = 0
    for var i = 0; i < str.substr(1).length; i++:
        long += (str.charCodeAt(i) << (i % 16))

    var aa = long + str.substr(4)
    var long = 0
    var a = str.substr(5)
    for var i = 0; i < a.length; i++:
        long += (a.charCodeAt(i) << (i % 16))

    a = long + "" + str.substr(4)
    var b = hex_md5(str.substr(1)) + hex_sha1(a.substr(5))
    return hex_md5(b).substr(4, 24)


def makeKey_11(str):
    var base = new Base64()
    var str = str.substr(5, 5 * 5 - 1) + "2" + str.substr(1, 2) + str.substr((5 + 1) * (5 + 1), 3)
    var long = 0
    for var i = 0; i < str.substr(1).length; i++:
        long += (str.charCodeAt(i) << (i % 16))

    var aa = long + str.substr(4)
    var long = 0
    var a = str.substr(5)
    for var i = 0; i < a.length; i++:
        long += (a.charCodeAt(i) << (i % 16))

    a = long + "" + str.substr(2)
    var b = str.substr(1) + hex_sha1(a.substr(5))
    return hex_md5(b).substr(2, 24)


def makeKey_136(str):
    return hex_md5(makeKey_18(str) + makeKey_1(str)).substr(1, 24)


def makeKey_137(str):
    return hex_md5(makeKey_19(str) + makeKey_14(str)).substr(2, 24)


def makeKey_138(str):
    return hex_md5(makeKey_0(str) + makeKey_15(str)).substr(3, 24)


def makeKey_139(str):
    return hex_md5(makeKey_1(str) + makeKey_16(str)).substr(4, 24)


def makeKey_140(str):
    return hex_md5(makeKey_4(str) + makeKey_9(str)).substr(1, 24)


def makeKey_141(str):
    return hex_md5(makeKey_5(str) + makeKey_10(str)).substr(2, 24)


def makeKey_142(str):
    return hex_md5(makeKey_3(str) + makeKey_17(str)).substr(3, 24)


def strToLong(str):
    var long = 0
    for var i = 0; i < str.length; i++:
        # 取出相应下标的ascii码 * 2的i次方相加
        long += (str.charCodeAt(i) << (i % 16))

    return long


def strToLongEn(str):
    var long = 0
    for var i = 0; i < str.length; i++:
        long += (str.charCodeAt(i) << (i % 16)) + i

    return long


def strToLongEn2(str, step):
    var long = 0
    for var i = 0; i < str.length; i++:
        long += (str.charCodeAt(i) << (i % 16)) + (i * step)

    return long


def strToLongEn3(str, step):
    var long = 0
    for var i = 0; i < str.length; i++:
        long += (str.charCodeAt(i) << (i % 16)) + (i + step - str.charCodeAt(i))

    return long


def makeKey_0(str):
    # 下标5开始的25的长度+下标36开始的3个长度
    var str = str.substr(5, 5 * 5) + str.substr((5 + 1) * (5 + 1), 3)
    var a = str.substr(5) + str.substr(-4)
    var b = str.substr(4) + a.substr(-6)
    # md5加密后取4开始的24个字符
    return hex_md5(str).substr(4, 24)


def makeKey_1(str):
    var str = str.substr(5, 5 * 5) + "5" + str.substr(1, 2) + "1" + str.substr((5 + 1) * (5 + 1), 3)
    var a = str.substr(5) + str.substr(4)
    var b = str.substr(12) + a.substr(-6)
    var c = str.substr(4) + a.substr(6)
    return hex_md5(c).substr(4, 24)


def makeKey_2(str):
    var str = str.substr(5, 5 * 5) + "15" + str.substr(1, 2) + str.substr((5 + 1) * (5 + 1), 3)
    var a = strToLong(str.substr(5)) + str.substr(4)
    var b = strToLong(str.substr(5)) + str.substr(4)
    var c = str.substr(4) + b.substr(5)
    return hex_md5(c).substr(1, 24)


def makeKey_16(str):
    var base = new Base64()
    var str = str.substr(5, 5 * 5 - 1) + "2" + str.substr(1, 2) + "-" + "5"
    var long = 0
    for var i = 0; i < str.substr(1).length; i++:
        long += (str.charCodeAt(i) << (i % 11))

    var aa = long + str.substr(4)
    var long = 0
    var a = str.substr(5)
    for var i = 0; i < a.length; i++:
        long += (a.charCodeAt(i) << (i % 16)) + i

    a = long + "" + str.substr(2)
    var b = base.encode(a.substr(1)) + strToLongEn2(str.substr(5), 5) + str.substr(2, 3)
    return hex_md5(b).substr(2, 24)


def makeKey_17(str):
    var base = new Base64()
    var str = str.substr(5, 5 * 5 - 1) + "7" + str.substr(1, 2) + "-" + "5"
    var long = 0
    for var i = 0; i < str.substr(1).length; i++:
        long += (str.charCodeAt(i) << (i % 11))

    var aa = long + str.substr(4)
    var long = 0
    var a = str.substr(5)
    for var i = 0; i < a.length; i++:
        long += (a.charCodeAt(i) << (i % 16)) + i

    a = long + "" + str.substr(2)
    var b = base.encode(a.substr(1)) + strToLongEn2(str.substr(5), 5 + 1) + str.substr(2 + 5, 3)
    return hex_md5(b).substr(0, 24)


def makeKey_18(str):
    var base = new Base64()
    var str = str.substr(5, 5 * 5 - 1) + "7" + str.substr(1, 2) + "5" + str.substr(2 + 5, 3)
    var long = 0
    for var i = 0; i < str.substr(1).length; i++:
        long += (str.charCodeAt(i) << (i % 11))

    var aa = long + str.substr(4)
    var long = 0
    var a = str.substr(5)
    for var i = 0; i < a.length; i++:
        long += (a.charCodeAt(i) << (i % 16)) + i

    a = long + "" + str.substr(2)
    var b = a.substr(1) + strToLongEn2(str.substr(5), 5 + 1) + str.substr(2 + 5, 3)
    return hex_md5(b).substr(0, 24)


def makeKey_19(str):
    var base = new Base64()
    var str = str.substr(5, 5 * 5 - 1) + "7" + str.substr(5, 2) + "5" + str.substr(2 + 5, 3)
    var long = 0
    for var i = 0; i < str.substr(1).length; i++:
        long += (str.charCodeAt(i) << (i % 11))

    var aa = long + str.substr(4)
    var long = 0
    var a = str.substr(5)
    for var i = 0; i < a.length; i++:
        long += (a.charCodeAt(i) << (i % 16)) + i

    a = long + "" + str.substr(2)
    var b = a.substr(1) + strToLongEn3(str.substr(5), 5 - 1) + str.substr(2 + 5, 3)
    return hex_md5(b).substr(0, 24)


def makeKey_20(str):
    return hex_md5(makeKey_10(str) + makeKey_5(str)).substr(1, 24)


def makeKey_21(str):
    return hex_md5(makeKey_11(str) + makeKey_3(str)).substr(2, 24)


def makeKey_22(str):
    return hex_md5(makeKey_14(str) + makeKey_19(str)).substr(3, 24)


def makeKey_23(str):
    return hex_md5(makeKey_15(str) + makeKey_0(str)).substr(4, 24)


def makeKey_24(str):
    return hex_md5(makeKey_16(str) + makeKey_1(str)).substr(1, 24)


def makeKey_25(str):
    return hex_md5(makeKey_9(str) + makeKey_4(str)).substr(2, 24)


def makeKey_26(str):
    return hex_md5(makeKey_10(str) + makeKey_5(str)).substr(3, 24)


def makeKey_27(str):
    return hex_md5(makeKey_17(str) + makeKey_3(str)).substr(4, 24)


def makeKey_28(str):
    return hex_md5(makeKey_18(str) + makeKey_7(str)).substr(1, 24)


def makeKey_29(str):
    return hex_md5(makeKey_19(str) + makeKey_3(str)).substr(2, 24)


def makeKey_30(str):
    return hex_md5(makeKey_0(str) + makeKey_7(str)).substr(3, 24)


def makeKey_31(str):
    return hex_md5(makeKey_1(str) + makeKey_8(str)).substr(4, 24)


def makeKey_32(str):
    return hex_md5(makeKey_4(str) + makeKey_14(str)).substr(3, 24)


def makeKey_33(str):
    return hex_md5(makeKey_5(str) + makeKey_15(str)).substr(4, 24)


def makeKey_34(str):
    return hex_md5(makeKey_3(str) + makeKey_16(str)).substr(1, 24)


def makeKey_7(str):
    var base = new Base64()
    var str = base.encode(str.substr(5, 5 * 4) + "55" + str.substr(1, 2)) + str.substr((5 + 1) * (5 + 1), 3)
    var long = 0
    for var i = 0; i < str.substr(1).length; i++:
        long += (str.charCodeAt(i) << (i % 16 + 5)) + 3 + 5

    var aa = long + str.substr(4)
    var long = 0
    var a = str.substr(5)
    for var i = 0; i < a.length; i++:
        long += (a.charCodeAt(i) << (i % 16))

    a = long + "" + str.substr(4)
    var b = hex_md5(str.substr(1)) + strToLong(a.substr(5))
    return hex_md5(b).substr(3, 24)


def makeKey_8(str):
    var base = new Base64()
    var str = base.encode(str.substr(5, 5 * 5 - 1) + "5" + "-" + "5") + str.substr(1, 2) + str.substr((5 + 1) * (5 + 1), 3)
    var long = 0
    for var i = 0; i < str.substr(1).length; i++:
        long += (str.charCodeAt(i) << (i % 16))

    var aa = long + str.substr(4)
    var long = 0
    var a = str.substr(5)
    for var i = 0; i < a.length; i++:
        long += (a.charCodeAt(i) << (i % 16))

    a = long + "" + str.substr(4)
    var b = hex_md5(str.substr(1)) + strToLongEn(a.substr(5))
    return hex_md5(b).substr(4, 24)


def makeKey_143(str):
    return hex_md5(makeKey_7(str) + makeKey_18(str)).substr(4, 24)


def makeKey_144(str):
    return hex_md5(makeKey_17(str) + makeKey_19(str)).substr(1, 24)


def makeKey_145(str):
    return hex_md5(makeKey_18(str) + makeKey_0(str)).substr(2, 24)


def makeKey_146(str):
    return hex_md5(makeKey_19(str) + makeKey_1(str)).substr(3, 24)


def makeKey_147(str):
    return hex_md5(makeKey_0(str) + makeKey_4(str)).substr(4, 24)


def makeKey_148(str):
    return hex_md5(makeKey_1(str) + makeKey_5(str)).substr(3, 24)


def makeKey_149(str):
    return hex_md5(makeKey_4(str) + makeKey_3(str)).substr(4, 24)


def makeKey_150(str):
    return hex_md5(makeKey_14(str) + makeKey_19(str)).substr(1, 24)


def makeKey_151(str):
    return hex_md5(makeKey_15(str) + makeKey_0(str)).substr(2, 24)


def makeKey_152(str):
    return hex_md5(makeKey_16(str) + makeKey_1(str)).substr(3, 24)


def makeKey_12(str):
    var base = new Base64()
    var str = str.substr(5, 5 * 5 - 1) + str.substr((5 + 1) * (5 + 1), 3) + "2" + str.substr(1, 2)
    var long = 0
    for var i = 0; i < str.substr(1).length; i++:
        long += (str.charCodeAt(i) << (i % 16))

    var aa = long + str.substr(4)
    var long = 0
    var a = str.substr(5)
    for var i = 0; i < a.length; i++:
        long += (a.charCodeAt(i) << (i % 16))

    a = long + "" + str.substr(2)
    var b = str.substr(1) + hex_sha1(str.substr(5))
    return hex_md5(b).substr(1, 24)


def makeKey_13(str):
    var base = new Base64()
    var str = str.substr(5, 5 * 5 - 1) + "2" + str.substr(1, 2)
    var long = 0
    for var i = 0; i < str.substr(1).length; i++:
        long += (str.charCodeAt(i) << (i % 16))

    var aa = long + str.substr(4)
    var long = 0
    var a = str.substr(5)
    for var i = 0; i < a.length; i++:
        long += (a.charCodeAt(i) << (i % 16))

    a = long + "" + str.substr(2)
    var b = base.encode(str.substr(1) + hex_sha1(str.substr(5)))
    return hex_md5(b).substr(1, 24)


def makeKey_14(str):
    var base = new Base64()
    var str = str.substr(5, 5 * 5 - 1) + "2" + str.substr(1, 2)
    var long = 0
    for var i = 0; i < str.substr(1).length; i++:
        long += (str.charCodeAt(i) << (i % 16))

    var aa = long + str.substr(4)
    var long = 0
    var a = str.substr(5)
    for var i = 0; i < a.length; i++:
        long += (a.charCodeAt(i) << (i % 16))

    a = long + "" + str.substr(2)
    var b = base.encode(str.substr(1) + str.substr(5) + str.substr(1, 3))
    return hex_sha1(b).substr(1, 24)


def makeKey_181(str):
    return hex_md5(makeKey_19(str) + makeKey_15(str)).substr(1, 24)


def makeKey_182(str):
    return hex_md5(makeKey_0(str) + makeKey_16(str)).substr(2, 24)


def makeKey_183(str):
    return hex_md5(makeKey_1(str) + makeKey_9(str)).substr(3, 24)


def makeKey_184(str):
    return hex_md5(makeKey_4(str) + makeKey_10(str)).substr(4, 24)


def makeKey_185(str):
    return hex_md5(makeKey_14(str) + makeKey_17(str)).substr(3, 24)


def makeKey_186(str):
    return hex_md5(makeKey_15(str) + makeKey_18(str)).substr(4, 24)


def makeKey_187(str):
    return hex_md5(makeKey_16(str) + makeKey_19(str)).substr(4, 24)


def makeKey_188(str):
    return hex_md5(makeKey_9(str) + makeKey_0(str)).substr(1, 24)


def makeKey_189(str):
    return hex_md5(makeKey_10(str) + makeKey_1(str)).substr(2, 24)


def makeKey_190(str):
    return hex_md5(makeKey_17(str) + makeKey_4(str)).substr(3, 24)


def makeKey_191(str):
    return hex_md5(makeKey_18(str) + makeKey_19(str)).substr(4, 24)


def makeKey_192(str):
    return hex_md5(makeKey_19(str) + makeKey_0(str)).substr(1, 24)


def makeKey_193(str):
    return hex_md5(makeKey_0(str) + makeKey_1(str)).substr(2, 24)


def makeKey_194(str):
    return hex_md5(makeKey_1(str) + makeKey_4(str)).substr(3, 24)


def makeKey_195(str):
    return hex_md5(makeKey_4(str) + makeKey_14(str)).substr(4, 24)


def makeKey_196(str):
    return hex_md5(makeKey_5(str) + makeKey_15(str)).substr(3, 24)


def makeKey_197(str):
    return hex_md5(makeKey_3(str) + makeKey_16(str)).substr(4, 24)


def makeKey_198(str):
    return hex_md5(makeKey_3(str) + makeKey_9(str)).substr(1, 24)


def makeKey_199(str):
    return hex_md5(makeKey_7(str) + makeKey_1(str)).substr(2, 24)


def makeKey_15(str):
    var base = new Base64()
    var str = str.substr(5, 5 * 5 - 1) + "2" + str.substr(1, 2)
    var long = 0
    for var i = 0; i < str.substr(1).length; i++:
        long += (str.charCodeAt(i) << (i % 16))

    var aa = long + str.substr(4)
    var long = 0
    var a = str.substr(5)
    for var i = 0; i < a.length; i++:
        long += (a.charCodeAt(i) << (i % 16))

    a = long + "" + str.substr(2)
    var b = base.encode(a.substr(1) + str.substr(5) + str.substr(2, 3))
    return hex_sha1(b).substr(1, 24)


def makeKey_130(str):
    return hex_md5(makeKey_14(str) + makeKey_7(str)).substr(3, 24)


def makeKey_131(str):
    return hex_md5(makeKey_15(str) + makeKey_10(str)).substr(4, 24)


def makeKey_132(str):
    return hex_md5(makeKey_16(str) + makeKey_17(str)).substr(3, 24)


def makeKey_133(str):
    return hex_md5(makeKey_9(str) + makeKey_18(str)).substr(4, 24)


def makeKey_134(str):
    return hex_md5(makeKey_10(str) + makeKey_19(str)).substr(1, 24)


def makeKey_135(str):
    return hex_md5(makeKey_17(str) + makeKey_0(str)).substr(2, 24)


def makeKey_153(str):
    return hex_md5(makeKey_9(str) + makeKey_4(str)).substr(1, 24)


def makeKey_154(str):
    return hex_md5(makeKey_10(str) + makeKey_5(str)).substr(1, 24)


def makeKey_155(str):
    return hex_md5(makeKey_17(str) + makeKey_3(str)).substr(2, 24)


def makeKey_156(str):
    return hex_md5(makeKey_18(str) + makeKey_7(str)).substr(3, 24)


def makeKey_157(str):
    return hex_md5(makeKey_19(str) + makeKey_3(str)).substr(4, 24)


def makeKey_158(str):
    return hex_md5(makeKey_0(str) + makeKey_7(str)).substr(1, 24)


def makeKey_159(str):
    return hex_md5(makeKey_1(str) + makeKey_8(str)).substr(2, 24)


def makeKey_160(str):
    return hex_md5(makeKey_4(str) + makeKey_14(str)).substr(3, 24)


def makeKey_161(str):
    return hex_md5(makeKey_19(str) + makeKey_15(str)).substr(4, 24)


def makeKey_162(str):
    return hex_md5(makeKey_0(str) + makeKey_16(str)).substr(1, 24)


def makeKey_163(str):
    return hex_md5(makeKey_1(str) + makeKey_9(str)).substr(2, 24)


def makeKey_164(str):
    return hex_md5(makeKey_4(str) + makeKey_10(str)).substr(3, 24)


def makeKey_165(str):
    return hex_md5(makeKey_5(str) + makeKey_17(str)).substr(4, 24)


def makeKey_166(str):
    return hex_md5(makeKey_3(str) + makeKey_18(str)).substr(3, 24)


def makeKey_167(str):
    return hex_md5(makeKey_7(str) + makeKey_19(str)).substr(4, 24)


def makeKey_168(str):
    return hex_md5(makeKey_0(str) + makeKey_0(str)).substr(1, 24)


def makeKey_169(str):
    return hex_md5(makeKey_1(str) + makeKey_1(str)).substr(2, 24)


def makeKey_170(str):
    return hex_md5(makeKey_4(str) + makeKey_4(str)).substr(3, 24)


def makeKey_171(str):
    return hex_md5(makeKey_17(str) + makeKey_5(str)).substr(1, 24)


def makeKey_172(str):
    return hex_md5(makeKey_18(str) + makeKey_3(str)).substr(2, 24)


def makeKey_173(str):
    return hex_md5(makeKey_19(str) + makeKey_7(str)).substr(3, 24)


def makeKey_174(str):
    return hex_md5(makeKey_0(str) + makeKey_17(str)).substr(4, 24)


def makeKey_175(str):
    return hex_md5(makeKey_1(str) + makeKey_18(str)).substr(1, 24)


def makeKey_176(str):
    return hex_md5(makeKey_4(str) + makeKey_19(str)).substr(2, 24)


def makeKey_35(str):
    return hex_md5(makeKey_7(str) + makeKey_9(str)).substr(2, 24)


def makeKey_36(str):
    return hex_md5(makeKey_8(str) + makeKey_10(str)).substr(3, 24)


def makeKey_37(str):
    return hex_md5(makeKey_6(str) + makeKey_17(str)).substr(1, 24)


def makeKey_38(str):
    return hex_md5(makeKey_12(str) + makeKey_18(str)).substr(2, 24)


def makeKey_39(str):
    return hex_md5(makeKey_14(str) + makeKey_19(str)).substr(3, 24)


def makeKey_40(str):
    return hex_md5(makeKey_15(str) + makeKey_0(str)).substr(4, 24)


def makeKey_41(str):
    return hex_md5(makeKey_16(str) + makeKey_1(str)).substr(3, 24)


def makeKey_42(str):
    return hex_md5(makeKey_9(str) + makeKey_4(str)).substr(4, 24)


def makeKey_43(str):
    return hex_md5(makeKey_10(str) + makeKey_5(str)).substr(1, 24)


def makeKey_44(str):
    return hex_md5(makeKey_17(str) + makeKey_3(str)).substr(2, 24)


def makeKey_45(str):
    return hex_md5(makeKey_18(str) + makeKey_7(str)).substr(3, 24)


def makeKey_46(str):
    return hex_md5(makeKey_19(str) + makeKey_17(str)).substr(4, 24)


def makeKey_47(str):
    return hex_md5(makeKey_0(str) + makeKey_18(str)).substr(1, 24)


def makeKey_48(str):
    return hex_md5(makeKey_1(str) + makeKey_19(str)).substr(2, 24)


def makeKey_49(str):
    return hex_md5(makeKey_4(str) + makeKey_0(str)).substr(3, 24)


def makeKey_50(str):
    return hex_md5(makeKey_5(str) + makeKey_1(str)).substr(4, 24)


def makeKey_51(str):
    return hex_md5(makeKey_3(str) + makeKey_4(str)).substr(1, 24)


def makeKey_52(str):
    return hex_md5(makeKey_7(str) + makeKey_14(str)).substr(2, 24)


def makeKey_53(str):
    return hex_md5(makeKey_12(str) + makeKey_15(str)).substr(3, 24)


def makeKey_54(str):
    return hex_md5(makeKey_14(str) + makeKey_16(str)).substr(4, 24)


def makeKey_55(str):
    return hex_md5(makeKey_15(str) + makeKey_9(str)).substr(3, 24)


def makeKey_56(str):
    return hex_md5(makeKey_16(str) + makeKey_10(str)).substr(4, 24)


def makeKey_57(str):
    return hex_md5(makeKey_9(str) + makeKey_17(str)).substr(1, 24)


def makeKey_58(str):
    return hex_md5(makeKey_10(str) + makeKey_18(str)).substr(2, 24)


def makeKey_59(str):
    return hex_md5(makeKey_17(str) + makeKey_19(str)).substr(3, 24)


def makeKey_60(str):
    return hex_md5(makeKey_18(str) + makeKey_0(str)).substr(1, 24)


def makeKey_61(str):
    return hex_md5(makeKey_19(str) + makeKey_1(str)).substr(2, 24)


def makeKey_62(str):
    return hex_md5(makeKey_0(str) + makeKey_4(str)).substr(3, 24)


def makeKey_63(str):
    return hex_md5(makeKey_1(str) + makeKey_19(str)).substr(4, 24)


def makeKey_64(str):
    return hex_md5(makeKey_4(str) + makeKey_0(str)).substr(3, 24)


def makeKey_65(str):
    return hex_md5(makeKey_14(str) + makeKey_1(str)).substr(1, 24)


def makeKey_66(str):
    return hex_md5(makeKey_15(str) + makeKey_4(str)).substr(2, 24)


def makeKey_67(str):
    return hex_md5(makeKey_16(str) + makeKey_5(str)).substr(3, 24)


def makeKey_68(str):
    return hex_md5(makeKey_9(str) + makeKey_3(str)).substr(4, 24)


def makeKey_69(str):
    return hex_md5(makeKey_10(str) + makeKey_7(str)).substr(1, 24)


def makeKey_70(str):
    return hex_md5(makeKey_17(str) + makeKey_0(str)).substr(2, 24)


def makeKey_71(str):
    return hex_md5(makeKey_18(str) + makeKey_1(str)).substr(3, 24)


def makeKey_72(str):
    return hex_md5(makeKey_19(str) + makeKey_4(str)).substr(4, 24)


def makeKey_73(str):
    return hex_md5(makeKey_0(str) + makeKey_17(str)).substr(1, 24)


def makeKey_74(str):
    return hex_md5(makeKey_1(str) + makeKey_18(str)).substr(2, 24)


def makeKey_75(str):
    return hex_md5(makeKey_14(str) + makeKey_19(str)).substr(3, 24)


def makeKey_76(str):
    return hex_md5(makeKey_15(str) + makeKey_0(str)).substr(4, 24)


def makeKey_77(str):
    return hex_md5(makeKey_16(str) + makeKey_1(str)).substr(3, 24)


def makeKey_78(str):
    return hex_md5(makeKey_9(str) + makeKey_4(str)).substr(4, 24)


def makeKey_79(str):
    return hex_md5(makeKey_10(str) + makeKey_9(str)).substr(1, 24)


def makeKey_80(str):
    return hex_md5(makeKey_17(str) + makeKey_10(str)).substr(2, 24)


def makeKey_81(str):
    return hex_md5(makeKey_18(str) + makeKey_17(str)).substr(3, 24)


def makeKey_82(str):
    return hex_md5(makeKey_14(str) + makeKey_18(str)).substr(1, 24)


def makeKey_83(str):
    return hex_md5(makeKey_15(str) + makeKey_19(str)).substr(4, 24)


def makeKey_84(str):
    return hex_md5(makeKey_16(str) + makeKey_0(str)).substr(1, 24)


def makeKey_85(str):
    return hex_md5(makeKey_9(str) + makeKey_1(str)).substr(2, 24)


def makeKey_86(str):
    return hex_md5(makeKey_10(str) + makeKey_4(str)).substr(3, 24)


def makeKey_87(str):
    return hex_md5(makeKey_14(str) + makeKey_14(str)).substr(4, 24)


def makeKey_88(str):
    return hex_md5(makeKey_15(str) + makeKey_15(str)).substr(1, 24)


def makeKey_89(str):
    return hex_md5(makeKey_16(str) + makeKey_16(str)).substr(2, 24)


def makeKey_90(str):
    return hex_md5(makeKey_9(str) + makeKey_9(str)).substr(3, 24)


def makeKey_91(str):
    return hex_md5(makeKey_10(str) + makeKey_10(str)).substr(4, 24)


def makeKey_92(str):
    return hex_md5(makeKey_17(str) + makeKey_17(str)).substr(3, 24)


def makeKey_93(str):
    return hex_md5(makeKey_18(str) + makeKey_18(str)).substr(4, 24)


def makeKey_94(str):
    return hex_md5(makeKey_19(str) + makeKey_19(str)).substr(1, 24)


def makeKey_95(str):
    return hex_md5(makeKey_0(str) + makeKey_0(str)).substr(2, 24)


def makeKey_96(str):
    return hex_md5(makeKey_1(str) + makeKey_1(str)).substr(3, 24)


def makeKey_97(str):
    return hex_md5(makeKey_4(str) + makeKey_4(str)).substr(4, 24)


def makeKey_98(str):
    return hex_md5(makeKey_5(str) + makeKey_5(str)).substr(3, 24)


def makeKey_99(str):
    return hex_md5(makeKey_3(str) + makeKey_3(str)).substr(4, 24)


def makeKey_100(str):
    return hex_md5(makeKey_7(str) + makeKey_3(str)).substr(1, 24)


def makeKey_101(str):
    return hex_md5(makeKey_10(str) + makeKey_7(str)).substr(2, 24)


def makeKey_102(str):
    return hex_md5(makeKey_17(str) + makeKey_18(str)).substr(1, 24)


def makeKey_103(str):
    return hex_md5(makeKey_18(str) + makeKey_19(str)).substr(2, 24)


def makeKey_104(str):
    return hex_md5(makeKey_19(str) + makeKey_0(str)).substr(3, 24)


def makeKey_105(str):
    return hex_md5(makeKey_0(str) + makeKey_0(str)).substr(4, 24)


def makeKey_106(str):
    return hex_md5(makeKey_1(str) + makeKey_1(str)).substr(1, 24)


def makeKey_107(str):
    return hex_md5(makeKey_14(str) + makeKey_14(str)).substr(2, 24)


def makeKey_108(str):
    return hex_md5(makeKey_15(str) + makeKey_15(str)).substr(3, 24)


def makeKey_109(str):
    return hex_md5(makeKey_16(str) + makeKey_16(str)).substr(4, 24)


def makeKey_110(str):
    return hex_md5(makeKey_9(str) + makeKey_9(str)).substr(1, 24)


def makeKey_111(str):
    return hex_md5(makeKey_10(str) + makeKey_10(str)).substr(2, 24)


def makeKey_112(str):
    return hex_md5(makeKey_17(str) + makeKey_17(str)).substr(3, 24)


def makeKey_113(str):
    return hex_md5(makeKey_18(str) + makeKey_18(str)).substr(4, 24)


def makeKey_114(str):
    return hex_md5(makeKey_19(str) + makeKey_19(str)).substr(3, 24)


def makeKey_115(str):
    return hex_md5(makeKey_0(str) + makeKey_0(str)).substr(4, 24)


def makeKey_116(str):
    return hex_md5(makeKey_1(str) + makeKey_1(str)).substr(1, 24)


def makeKey_117(str):
    return hex_md5(makeKey_4(str) + makeKey_4(str)).substr(2, 24)


def makeKey_118(str):
    return hex_md5(makeKey_5(str) + makeKey_15(str)).substr(3, 24)


def makeKey_119(str):
    return hex_md5(makeKey_3(str) + makeKey_16(str)).substr(1, 24)


def makeKey_120(str):
    return hex_md5(makeKey_19(str) + makeKey_9(str)).substr(1, 24)


def makeKey_121(str):
    return hex_md5(makeKey_0(str) + makeKey_10(str)).substr(2, 24)


def makeKey_122(str):
    return hex_md5(makeKey_1(str) + makeKey_17(str)).substr(3, 24)


def makeKey_123(str):
    return hex_md5(makeKey_4(str) + makeKey_18(str)).substr(4, 24)


def makeKey_124(str):
    return hex_md5(makeKey_5(str) + makeKey_19(str)).substr(1, 24)


def makeKey_125(str):
    return hex_md5(makeKey_3(str) + makeKey_0(str)).substr(2, 24)


def makeKey_3(str):
    var str = str.substr(5, 5 * 5) + '15' + str.substr(1, 2) + str.substr((5 + 1) * (5 + 1), 3)
    var a = strToLongEn(str.substr(5)) + str.substr(4)
    var b = str.substr(4) + a.substr(5)
    var c = strToLong(str.substr(5)) + str.substr(4)
    return hex_md5(b).substr(3, 24)


def makeKey_4(str):
    var str = str.substr(5, 5 * 5) + '2' + str.substr(1, 2) + str.substr((5 + 1) * (5 + 1), 3)
    var long = 0
    for var i = 0; i < str.substr(1).length; i++:
        long += (str.charCodeAt(i) << (i % 16))

    var aa = long + str.substr(4)
    var long = 0
    var a = str.substr(5)
    for var i = 0; i < a.length; i++:
        long += (a.charCodeAt(i) << (i % 16)) + i

    a = long + '' + str.substr(4)
    var b = hex_md5(str.substr(1)) + strToLong(a.substr(5))
    return hex_md5(b).substr(3, 24)


def makeKey_5(str):
    var base = new Base64()
    var str = base.encode(str.substr(5, 5 * 5) + str.substr(1, 2) + '1') + str.substr((5 + 1) * (5 + 1), 3)
    var a = strToLongEn(str.substr(4, 10)) + str.substr(-4)
    var b = hex_md5(str.substr(4)) + a.substr(2)
    var a = str.substr(3)
    var c = strToLong(str.substr(5)) + str.substr(4)
    var aa = long + str.substr(4)
    var long = 0
    for var i = 0; i < a.length; i++:
        long += (a.charCodeAt(i) << (i % 12)) + i

    a = long + '' + str.substr(4)
    return hex_md5(str).substr(4, 24)


def makeKey_6(str):
    var base = new Base64()
    var str = str.substr(5, 5 * 5) + str.substr((5 + 1) * (5 + 1), 3)
    var a = base.encode(str.substr(4, 10)) + str.substr(2)
    var b = str.substr(6) + a.substr(2)
    var c = strToLong(str.substr(5)) + str.substr(4)
    var aa = long + str.substr(4)
    var long = 0
    var a = str.substr(5)
    for var i = 0; i < a.length; i++:
        long += (a.charCodeAt(i) << (i % 16)) + i

    a = long + '' + str.substr(4)
    return hex_md5(b).substr(2, 24)


def makeKey_126(str):
    return hex_md5(makeKey_7(str) + makeKey_1(str)).substr(3, 24)


def makeKey_127(str):
    return hex_md5(makeKey_3(str) + makeKey_4(str)).substr(4, 24)


def makeKey_128(str):
    return hex_md5(makeKey_7(str) + makeKey_5(str)).substr(1, 24)


def makeKey_129(str):
    return hex_md5(makeKey_8(str) + makeKey_3(str)).substr(2, 24)


def makeKey_177(str):
    return hex_md5(makeKey_9(str) + makeKey_0(str)).substr(3, 24)


def makeKey_178(str):
    return hex_md5(makeKey_10(str) + makeKey_1(str)).substr(4, 24)


def makeKey_179(str):
    return hex_md5(makeKey_17(str) + makeKey_4(str)).substr(1, 24)


def makeKey_180(str):
    return hex_md5(makeKey_18(str) + makeKey_14(str)).substr(3, 24)

# 获取cookies
var cookie = getCookie('vjkl5')
# 定义函数的列表长度为 200
var arrFun = [makeKey_0, makeKey_1, makeKey_2, makeKey_3, makeKey_4, makeKey_5, makeKey_6, makeKey_7, makeKey_8, makeKey_9, makeKey_10, makeKey_11, makeKey_12, makeKey_13, makeKey_14, makeKey_15, makeKey_16, makeKey_17, makeKey_18, makeKey_19, makeKey_20, makeKey_21, makeKey_22, makeKey_23, makeKey_24, makeKey_25, makeKey_26, makeKey_27, makeKey_28, makeKey_29, makeKey_30, makeKey_31, makeKey_32, makeKey_33, makeKey_34, makeKey_35, makeKey_36, makeKey_37, makeKey_38, makeKey_39, makeKey_40, makeKey_41, makeKey_42, makeKey_43, makeKey_44, makeKey_45, makeKey_46, makeKey_47, makeKey_48, makeKey_49, makeKey_50, makeKey_51, makeKey_52, makeKey_53, makeKey_54, makeKey_55, makeKey_56, makeKey_57, makeKey_58, makeKey_59, makeKey_60, makeKey_61, makeKey_62, makeKey_63, makeKey_64, makeKey_65, makeKey_66, makeKey_67, makeKey_68, makeKey_69, makeKey_70, makeKey_71, makeKey_72, makeKey_73, makeKey_74, makeKey_75, makeKey_76, makeKey_77, makeKey_78, makeKey_79, makeKey_80, makeKey_81, makeKey_82, makeKey_83, makeKey_84, makeKey_85, makeKey_86, makeKey_87, makeKey_88, makeKey_89, makeKey_90, makeKey_91, makeKey_92, makeKey_93, makeKey_94, makeKey_95, makeKey_96, makeKey_97, makeKey_98, makeKey_99, makeKey_100, makeKey_101, makeKey_102, makeKey_103, makeKey_104, makeKey_105, makeKey_106, makeKey_107, makeKey_108, makeKey_109, makeKey_110, makeKey_111, makeKey_112, makeKey_113, makeKey_114, makeKey_115, makeKey_116, makeKey_117, makeKey_118, makeKey_119, makeKey_120, makeKey_121, makeKey_122, makeKey_123, makeKey_124, makeKey_125, makeKey_126, makeKey_127, makeKey_128, makeKey_129, makeKey_130, makeKey_131, makeKey_132, makeKey_133, makeKey_134, makeKey_135, makeKey_136, makeKey_137, makeKey_138, makeKey_139, makeKey_140, makeKey_141, makeKey_142, makeKey_143, makeKey_144, makeKey_145, makeKey_146, makeKey_147, makeKey_148, makeKey_149, makeKey_150, makeKey_151, makeKey_152, makeKey_153, makeKey_154, makeKey_155, makeKey_156, makeKey_157, makeKey_158, makeKey_159, makeKey_160, makeKey_161, makeKey_162, makeKey_163, makeKey_164, makeKey_165, makeKey_166, makeKey_167, makeKey_168, makeKey_169, makeKey_170, makeKey_171, makeKey_172, makeKey_173, makeKey_174, makeKey_175, makeKey_176, makeKey_177, makeKey_178, makeKey_179, makeKey_180, makeKey_181, makeKey_182, makeKey_183, makeKey_184, makeKey_185, makeKey_186, makeKey_187, makeKey_188, makeKey_189, makeKey_190, makeKey_191, makeKey_192, makeKey_193, makeKey_194, makeKey_195, makeKey_196, makeKey_197, makeKey_198, makeKey_199]
# strToLong(str) ==> 将每个字符转换成ascii码,乘以2的它的下标的幂次方,相加
# long
# for index,val in enumerate(str):
#     long += ord(val)*2**index
# reduce(lambda x,y:x+y, [ord(x)*2**i for i,x in enumerate(str)])
# cookies按以上方法转化成数字后除以200取余数
var funIndex = strToLong(cookie) % arrFun.length
# 以余数为下标获取相应的加密函数
var fun = arrFun[funIndex]
# 使用加密函数对cookie进行加密
var result = fun(cookie);
