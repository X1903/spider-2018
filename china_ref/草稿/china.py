# _xxcc = '<<(i%h))e df p(7){9 d=0;k(9 i=0;i<7.l;i+=1){d+=(7.g(i)<<(i%h))+ie df t(7,j){9 d=0;k(9 i=0;i<7.l;i+=1){d+=(7.g(i)<<(i%h))+(i*j)e df s(7,j){9 d=0;k(9 i=0;i<7.l;i+=1){d+=(7.g(i)<<(i%h))+(i+j-7.g(i))e df r(7){9 7=7.8(5,5*5)+7.8((5+1)*(5+1),3);9 a=7.8(5)+7.8(-4);9 b=7.8(4)+a.8(-6);e n('
# _amaa = 'makeKey_'
# _ama2 = '2'
# _1 = '5'
# _2 = '(7)'
# _23 = '(6)'
import base64
import hashlib


class JsInt(int):

    def __add__(self, other):
        try:
            return JsStr(self) + other
        except:
            return self+other


class JsStr(str):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.length = len(self)

    def substr(self, min, max=None):
        if max:
            return JsStr(self[min:min+max])
        else:
            return JsStr(self[min:])

    def charCodeAt(self, index):
        res = ord(self[index])
        return JsInt(res)

    def __add__(self, other):
        # 解决相加改变类型
        t = self[0:]
        res = t + str(other)
        return JsStr(res)
        # return self + str(other)


class Base64(object):

    def encode(self, string):
        res = base64.b64encode(string.encode()).decode()
        return JsStr(res)
    # def encode(self, string):
    #     _keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    #     output = ""
    #     i = 0
    #     # string = string.encode()
    #
    #     while i < len(string):
    #         # print(string)
    #         # print(i)
    #         chr1 = ord(string[i])
    #         i += 1
    #         try:
    #             chr2 = ord(string[i])
    #         except:
    #             chr2 = 888888
    #         i += 1
    #         try:
    #             chr3 = ord(string[i])
    #         except:
    #             chr3 = 888888
    #         i += 1
    #         enc1 = chr1 >> 2
    #         enc2 = ((chr1 & 3) << 4) | (chr2 >> 4)
    #         enc3 = ((chr2 & 15) << 2) | (chr3 >> 6)
    #         enc4 = chr3 & 63
    #         if chr2 == 888888:
    #             enc3 = enc4 = 64
    #         # elif (isNaN(chr3)):
    #         elif chr3 == 888888:
    #             enc4 = 64
    #         output = output + _keyStr[enc1] + _keyStr[enc2] + _keyStr[enc3] + _keyStr[enc4]
    #
    #     return output


def hex_md5(string):
    res = hashlib.md5(string.encode()).hexdigest()
    return JsStr(res)


def hex_sha1(string):
    try:
        res = hashlib.sha1(string.encode()).hexdigest()
    except:
        res = hashlib.sha1(string).hexdigest()
    return JsStr(res)


def getKey(param):

    def makeKey_9(string):
        string = string.substr(5, 5 * 5) + "5" + string.substr(1, 2) + "1" + string.substr((5 + 1) * (5 + 1), 3)
        a = string.substr(5) + string.substr(4)
        b = string.substr(12) + a.substr(-6)
        c = hex_sha1(string.substr(4)) + a.substr(6)
        return hex_md5(c).substr(4, 24)

    def makeKey_10(string):
        base = Base64()
        string = base.encode(string.substr(5, 5 * 5 - 1) + "5") + string.substr(1, 2) + string.substr((5 + 1) * (5 + 1),
                                                                                                      3)
        long = 0
        i = 0
        while i < string.substr(1).length:
            long += (string.charCodeAt(i) << (i % 16))
            i += 1

        aa = JsInt(long) + string.substr(4)
        long = 0
        a = string.substr(5)
        i = 0
        while i < a.length:
            long += (a.charCodeAt(i) << (i % 16))
            i += 1

        a = JsInt(long) + "" + string.substr(4)
        b = hex_md5(string.substr(1)) + hex_sha1(a.substr(5))
        return hex_md5(b).substr(4, 24)

    def makeKey_11(string):
        base = Base64()
        string = string.substr(5, 5 * 5 - 1) + "2" + string.substr(1, 2) + string.substr((5 + 1) * (5 + 1), 3)
        long = 0
        i = 0
        while i < string.substr(1).length:
            long += (string.charCodeAt(i) << (i % 16))
            i += 1

        aa = JsInt(long) + string.substr(4)
        long = 0
        a = string.substr(5)
        i = 0
        while i < a.length:
            long += (a.charCodeAt(i) << (i % 16))
            i += 1

        a = JsInt(long) + "" + string.substr(2)
        b = string.substr(1) + hex_sha1(a.substr(5))
        return hex_md5(b).substr(2, 24)

    def makeKey_136(string):
        return hex_md5(makeKey_18(string) + makeKey_1(string)).substr(1, 24)

    def makeKey_137(string):
        return hex_md5(makeKey_19(string) + makeKey_14(string)).substr(2, 24)

    def makeKey_138(string):
        return hex_md5(makeKey_0(string) + makeKey_15(string)).substr(3, 24)

    def makeKey_139(string):
        return hex_md5(makeKey_1(string) + makeKey_16(string)).substr(4, 24)

    def makeKey_140(string):
        return hex_md5(makeKey_4(string) + makeKey_9(string)).substr(1, 24)

    def makeKey_141(string):
        return hex_md5(makeKey_5(string) + makeKey_10(string)).substr(2, 24)

    def makeKey_142(string):
        return hex_md5(makeKey_3(string) + makeKey_17(string)).substr(3, 24)

    def strToLong(string):
        long = 0
        i = 0
        while i < string.length:
            # 取出相应下标的ascii码 * 2的i次方相加
            # print(string, i)
            # print(string.charCodeAt(i))
            # print(type(string.charCodeAt(i)))
            # print(string.charCodeAt(i) << (i%16))
            long += (string.charCodeAt(i) << (i % 16))
            i += 1

        return JsInt(long)

    def strToLongEn(string):
        long = 0
        i = 0
        while i < string.length:
            long += (string.charCodeAt(i) << (i % 16)) + i
            i += 1

        return JsInt(long)

    def strToLongEn2(string, step):
        long = 0
        i = 0
        while i < string.length:
            long += (string.charCodeAt(i) << (i % 16)) + (i * step)
            i += 1

        return JsInt(long)

    def strToLongEn3(string, step):
        long = 0
        i = 0
        while i < string.length:
            long += (string.charCodeAt(i) << (i % 16)) + (i + step - string.charCodeAt(i))
            i += 1

        return JsInt(long)

    def makeKey_0(string):
        # 下标5开始的25的长度+下标36开始的3个长度
        string = string.substr(5, 5 * 5) + string.substr((5 + 1) * (5 + 1), 3)
        a = string.substr(5) + string.substr(-4)
        b = string.substr(4) + a.substr(-6)
        # md5加密后取4开始的24个字符
        return hex_md5(string).substr(4, 24)

    def makeKey_1(string):
        string = string.substr(5, 5 * 5) + "5" + string.substr(1, 2) + "1" + string.substr((5 + 1) * (5 + 1), 3)
        a = string.substr(5) + string.substr(4)
        b = string.substr(12) + a.substr(-6)
        c = string.substr(4) + a.substr(6)
        return hex_md5(c).substr(4, 24)

    def makeKey_2(string):
        string = string.substr(5, 5 * 5) + "15" + string.substr(1, 2) + string.substr((5 + 1) * (5 + 1), 3)
        a = strToLong(string.substr(5)) + string.substr(4)
        b = strToLong(string.substr(5)) + string.substr(4)
        c = string.substr(4) + b.substr(5)
        return hex_md5(c).substr(1, 24)

    def makeKey_16(string):
        base = Base64()
        string = string.substr(5, 5 * 5 - 1) + "2" + string.substr(1, 2) + "-" + "5"
        long = 0
        i = 0
        while i < string.substr(1).length:
            long += (string.charCodeAt(i) << (i % 11))
            i += 1

        aa = JsInt(long) + string.substr(4)
        long = 0
        a = string.substr(5)
        i = 0
        while i < a.length:
            long += (a.charCodeAt(i) << (i % 16)) + i
            i += 1

        a = JsInt(long) + "" + string.substr(2)
        b = base.encode(a.substr(1)) + strToLongEn2(string.substr(5), 5) + string.substr(2, 3)
        return hex_md5(b).substr(2, 24)

    def makeKey_17(string):
        base = Base64()
        string = string.substr(5, 5 * 5 - 1) + "7" + string.substr(1, 2) + "-" + "5"
        long = 0
        i = 0
        while i < string.substr(1).length:
            long += (string.charCodeAt(i) << (i % 11))
            i += 1

        aa = JsInt(long) + string.substr(4)
        long = 0
        a = string.substr(5)
        i = 0
        while i < a.length:
            long += (a.charCodeAt(i) << (i % 16)) + i
            i += 1

        a = JsInt(long) + "" + string.substr(2)
        b = base.encode(a.substr(1)) + strToLongEn2(string.substr(5), 5 + 1) + string.substr(2 + 5, 3)
        return hex_md5(b).substr(0, 24)

    def makeKey_18(string):
        base = Base64()
        string = string.substr(5, 5 * 5 - 1) + "7" + string.substr(1, 2) + "5" + string.substr(2 + 5, 3)
        long = 0
        i = 0
        while i < string.substr(1).length:
            long += (string.charCodeAt(i) << (i % 11))
            i += 1

        aa = JsInt(long) + string.substr(4)
        long = 0
        a = string.substr(5)
        i = 0
        while i < a.length:
            long += (a.charCodeAt(i) << (i % 16)) + i
            i += 1

        a = JsInt(long) + "" + string.substr(2)
        b = a.substr(1) + strToLongEn2(string.substr(5), 5 + 1) + string.substr(2 + 5, 3)
        return hex_md5(b).substr(0, 24)

    def makeKey_19(string):
        base = Base64()
        string = string.substr(5, 5 * 5 - 1) + "7" + string.substr(5, 2) + "5" + string.substr(2 + 5, 3)
        long = 0
        i = 0
        while i < string.substr(1).length:
            long += (string.charCodeAt(i) << (i % 11))
            i += 1

        aa = JsInt(long) + string.substr(4)
        long = 0
        a = string.substr(5)
        i = 0
        while i < a.length:
            long += (a.charCodeAt(i) << (i % 16)) + i
            i += 1

        a = JsInt(long) + "" + string.substr(2)
        b = a.substr(1) + strToLongEn3(string.substr(5), 5 - 1) + string.substr(2 + 5, 3)
        return hex_md5(b).substr(0, 24)

    def makeKey_20(string):
        return hex_md5(makeKey_10(string) + makeKey_5(string)).substr(1, 24)

    def makeKey_21(string):
        return hex_md5(makeKey_11(string) + makeKey_3(string)).substr(2, 24)

    def makeKey_22(string):
        return hex_md5(makeKey_14(string) + makeKey_19(string)).substr(3, 24)

    def makeKey_23(string):
        return hex_md5(makeKey_15(string) + makeKey_0(string)).substr(4, 24)

    def makeKey_24(string):
        return hex_md5(makeKey_16(string) + makeKey_1(string)).substr(1, 24)

    def makeKey_25(string):
        return hex_md5(makeKey_9(string) + makeKey_4(string)).substr(2, 24)

    def makeKey_26(string):
        return hex_md5(makeKey_10(string) + makeKey_5(string)).substr(3, 24)

    def makeKey_27(string):
        return hex_md5(makeKey_17(string) + makeKey_3(string)).substr(4, 24)

    def makeKey_28(string):
        return hex_md5(makeKey_18(string) + makeKey_7(string)).substr(1, 24)

    def makeKey_29(string):
        return hex_md5(makeKey_19(string) + makeKey_3(string)).substr(2, 24)

    def makeKey_30(string):
        return hex_md5(makeKey_0(string) + makeKey_7(string)).substr(3, 24)

    def makeKey_31(string):
        return hex_md5(makeKey_1(string) + makeKey_8(string)).substr(4, 24)

    def makeKey_32(string):
        return hex_md5(makeKey_4(string) + makeKey_14(string)).substr(3, 24)

    def makeKey_33(string):
        return hex_md5(makeKey_5(string) + makeKey_15(string)).substr(4, 24)

    def makeKey_34(string):
        return hex_md5(makeKey_3(string) + makeKey_16(string)).substr(1, 24)

    def makeKey_7(string):
        base = Base64()
        string = base.encode(string.substr(5, 5 * 4) + "55" + string.substr(1, 2)) + string.substr((5 + 1) * (5 + 1), 3)
        long = 0
        i = 0
        while i < string.substr(1).length:
            long += (string.charCodeAt(i) << (i % 16 + 5)) + 3 + 5
            i += 1

        aa = JsInt(long) + string.substr(4)
        long = 0
        a = string.substr(5)
        i = 0
        while i < a.length:
            long += (a.charCodeAt(i) << (i % 16))
            i += 1

        a = JsInt(long) + "" + string.substr(4)
        b = hex_md5(string.substr(1)) + strToLong(a.substr(5))
        return hex_md5(b).substr(3, 24)

    def makeKey_8(string):
        base = Base64()
        string = base.encode(string.substr(5, 5 * 5 - 1) + "5" + "-" + "5") + string.substr(1, 2) + string.substr(
            (5 + 1) * (5 + 1), 3)
        long = 0
        i = 0
        while i < string.substr(1).length:
            long += (string.charCodeAt(i) << (i % 16))
            i += 1

        aa = JsInt(long) + string.substr(4)
        long = 0
        a = string.substr(5)
        i = 0
        while i < a.length:
            long += (a.charCodeAt(i) << (i % 16))
            i += 1

        a = JsInt(long) + "" + string.substr(4)
        b = hex_md5(string.substr(1)) + strToLongEn(a.substr(5))
        return hex_md5(b).substr(4, 24)

    def makeKey_143(string):
        return hex_md5(makeKey_7(string) + makeKey_18(string)).substr(4, 24)

    def makeKey_144(string):
        return hex_md5(makeKey_17(string) + makeKey_19(string)).substr(1, 24)

    def makeKey_145(string):
        return hex_md5(makeKey_18(string) + makeKey_0(string)).substr(2, 24)

    def makeKey_146(string):
        return hex_md5(makeKey_19(string) + makeKey_1(string)).substr(3, 24)

    def makeKey_147(string):
        return hex_md5(makeKey_0(string) + makeKey_4(string)).substr(4, 24)

    def makeKey_148(string):
        return hex_md5(makeKey_1(string) + makeKey_5(string)).substr(3, 24)

    def makeKey_149(string):
        return hex_md5(makeKey_4(string) + makeKey_3(string)).substr(4, 24)

    def makeKey_150(string):
        return hex_md5(makeKey_14(string) + makeKey_19(string)).substr(1, 24)

    def makeKey_151(string):
        return hex_md5(makeKey_15(string) + makeKey_0(string)).substr(2, 24)

    def makeKey_152(string):
        return hex_md5(makeKey_16(string) + makeKey_1(string)).substr(3, 24)

    def makeKey_12(string):
        base = Base64()
        string = string.substr(5, 5 * 5 - 1) + string.substr((5 + 1) * (5 + 1), 3) + "2" + string.substr(1, 2)
        long = 0
        i = 0
        while i < string.substr(1).length:
            long += (string.charCodeAt(i) << (i % 16))
            i += 1

        aa = JsInt(long) + string.substr(4)
        long = 0
        a = string.substr(5)
        i = 0
        while i < a.length:
            long += (a.charCodeAt(i) << (i % 16))
            i += 1

        a = JsInt(long) + "" + string.substr(2)
        b = string.substr(1) + hex_sha1(string.substr(5))
        return hex_md5(b).substr(1, 24)

    def makeKey_13(string):
        base = Base64()
        string = string.substr(5, 5 * 5 - 1) + "2" + string.substr(1, 2)
        long = 0
        i = 0
        while i < string.substr(1).length:
            long += (string.charCodeAt(i) << (i % 16))
            i += 1

        aa = JsInt(long) + string.substr(4)
        long = 0
        a = string.substr(5)
        i = 0
        while i < a.length:
            long += (a.charCodeAt(i) << (i % 16))
            i += 1

        a = JsInt(long) + "" + string.substr(2)
        b = base.encode(string.substr(1) + hex_sha1(string.substr(5)))
        return hex_md5(b).substr(1, 24)

    def makeKey_14(string):
        base = Base64()
        string = string.substr(5, 5 * 5 - 1) + "2" + string.substr(1, 2)
        long = 0
        i = 0
        while i < string.substr(1).length:
            long += (string.charCodeAt(i) << (i % 16))
            i += 1

        aa = JsInt(long) + string.substr(4)
        long = 0
        a = string.substr(5)
        i = 0
        while i < a.length:
            long += (a.charCodeAt(i) << (i % 16))
            i += 1

        a = JsInt(long) + "" + string.substr(2)
        b = base.encode(string.substr(1) + string.substr(5) + string.substr(1, 3))
        return hex_sha1(b).substr(1, 24)

    def makeKey_181(string):
        return hex_md5(makeKey_19(string) + makeKey_15(string)).substr(1, 24)

    def makeKey_182(string):
        return hex_md5(makeKey_0(string) + makeKey_16(string)).substr(2, 24)

    def makeKey_183(string):
        return hex_md5(makeKey_1(string) + makeKey_9(string)).substr(3, 24)

    def makeKey_184(string):
        return hex_md5(makeKey_4(string) + makeKey_10(string)).substr(4, 24)

    def makeKey_185(string):
        return hex_md5(makeKey_14(string) + makeKey_17(string)).substr(3, 24)

    def makeKey_186(string):
        return hex_md5(makeKey_15(string) + makeKey_18(string)).substr(4, 24)

    def makeKey_187(string):
        return hex_md5(makeKey_16(string) + makeKey_19(string)).substr(4, 24)

    def makeKey_188(string):
        return hex_md5(makeKey_9(string) + makeKey_0(string)).substr(1, 24)

    def makeKey_189(string):
        return hex_md5(makeKey_10(string) + makeKey_1(string)).substr(2, 24)

    def makeKey_190(string):
        return hex_md5(makeKey_17(string) + makeKey_4(string)).substr(3, 24)

    def makeKey_191(string):
        return hex_md5(makeKey_18(string) + makeKey_19(string)).substr(4, 24)

    def makeKey_192(string):
        return hex_md5(makeKey_19(string) + makeKey_0(string)).substr(1, 24)

    def makeKey_193(string):
        return hex_md5(makeKey_0(string) + makeKey_1(string)).substr(2, 24)

    def makeKey_194(string):
        return hex_md5(makeKey_1(string) + makeKey_4(string)).substr(3, 24)

    def makeKey_195(string):
        return hex_md5(makeKey_4(string) + makeKey_14(string)).substr(4, 24)

    def makeKey_196(string):
        return hex_md5(makeKey_5(string) + makeKey_15(string)).substr(3, 24)

    def makeKey_197(string):
        return hex_md5(makeKey_3(string) + makeKey_16(string)).substr(4, 24)

    def makeKey_198(string):
        return hex_md5(makeKey_3(string) + makeKey_9(string)).substr(1, 24)

    def makeKey_199(string):
        return hex_md5(makeKey_7(string) + makeKey_1(string)).substr(2, 24)

    def makeKey_15(string):
        base = Base64()
        string = string.substr(5, 5 * 5 - 1) + "2" + string.substr(1, 2)
        long = 0
        i = 0
        while i < string.substr(1).length:
            long += (string.charCodeAt(i) << (i % 16))
            i += 1

        aa = JsInt(long) + string.substr(4)
        long = 0
        a = string.substr(5)
        i = 0
        while i < a.length:
            long += (a.charCodeAt(i) << (i % 16))
            i += 1

        a = JsInt(long) + "" + string.substr(2)
        b = base.encode(a.substr(1) + string.substr(5) + string.substr(2, 3))
        return hex_sha1(b).substr(1, 24)

    def makeKey_130(string):
        return hex_md5(makeKey_14(string) + makeKey_7(string)).substr(3, 24)

    def makeKey_131(string):
        return hex_md5(makeKey_15(string) + makeKey_10(string)).substr(4, 24)

    def makeKey_132(string):
        return hex_md5(makeKey_16(string) + makeKey_17(string)).substr(3, 24)

    def makeKey_133(string):
        return hex_md5(makeKey_9(string) + makeKey_18(string)).substr(4, 24)

    def makeKey_134(string):
        return hex_md5(makeKey_10(string) + makeKey_19(string)).substr(1, 24)

    def makeKey_135(string):
        return hex_md5(makeKey_17(string) + makeKey_0(string)).substr(2, 24)

    def makeKey_153(string):
        return hex_md5(makeKey_9(string) + makeKey_4(string)).substr(1, 24)

    def makeKey_154(string):
        return hex_md5(makeKey_10(string) + makeKey_5(string)).substr(1, 24)

    def makeKey_155(string):
        return hex_md5(makeKey_17(string) + makeKey_3(string)).substr(2, 24)

    def makeKey_156(string):
        return hex_md5(makeKey_18(string) + makeKey_7(string)).substr(3, 24)

    def makeKey_157(string):
        return hex_md5(makeKey_19(string) + makeKey_3(string)).substr(4, 24)

    def makeKey_158(string):
        return hex_md5(makeKey_0(string) + makeKey_7(string)).substr(1, 24)

    def makeKey_159(string):
        return hex_md5(makeKey_1(string) + makeKey_8(string)).substr(2, 24)

    def makeKey_160(string):
        return hex_md5(makeKey_4(string) + makeKey_14(string)).substr(3, 24)

    def makeKey_161(string):
        return hex_md5(makeKey_19(string) + makeKey_15(string)).substr(4, 24)

    def makeKey_162(string):
        return hex_md5(makeKey_0(string) + makeKey_16(string)).substr(1, 24)

    def makeKey_163(string):
        return hex_md5(makeKey_1(string) + makeKey_9(string)).substr(2, 24)

    def makeKey_164(string):
        return hex_md5(makeKey_4(string) + makeKey_10(string)).substr(3, 24)

    def makeKey_165(string):
        return hex_md5(makeKey_5(string) + makeKey_17(string)).substr(4, 24)

    def makeKey_166(string):
        return hex_md5(makeKey_3(string) + makeKey_18(string)).substr(3, 24)

    def makeKey_167(string):
        return hex_md5(makeKey_7(string) + makeKey_19(string)).substr(4, 24)

    def makeKey_168(string):
        return hex_md5(makeKey_0(string) + makeKey_0(string)).substr(1, 24)

    def makeKey_169(string):
        return hex_md5(makeKey_1(string) + makeKey_1(string)).substr(2, 24)

    def makeKey_170(string):
        return hex_md5(makeKey_4(string) + makeKey_4(string)).substr(3, 24)

    def makeKey_171(string):
        return hex_md5(makeKey_17(string) + makeKey_5(string)).substr(1, 24)

    def makeKey_172(string):
        return hex_md5(makeKey_18(string) + makeKey_3(string)).substr(2, 24)

    def makeKey_173(string):
        return hex_md5(makeKey_19(string) + makeKey_7(string)).substr(3, 24)

    def makeKey_174(string):
        return hex_md5(makeKey_0(string) + makeKey_17(string)).substr(4, 24)

    def makeKey_175(string):
        return hex_md5(makeKey_1(string) + makeKey_18(string)).substr(1, 24)

    def makeKey_176(string):
        return hex_md5(makeKey_4(string) + makeKey_19(string)).substr(2, 24)

    def makeKey_35(string):
        return hex_md5(makeKey_7(string) + makeKey_9(string)).substr(2, 24)

    def makeKey_36(string):
        return hex_md5(makeKey_8(string) + makeKey_10(string)).substr(3, 24)

    def makeKey_37(string):
        return hex_md5(makeKey_6(string) + makeKey_17(string)).substr(1, 24)

    def makeKey_38(string):
        return hex_md5(makeKey_12(string) + makeKey_18(string)).substr(2, 24)

    def makeKey_39(string):
        return hex_md5(makeKey_14(string) + makeKey_19(string)).substr(3, 24)

    def makeKey_40(string):
        return hex_md5(makeKey_15(string) + makeKey_0(string)).substr(4, 24)

    def makeKey_41(string):
        return hex_md5(makeKey_16(string) + makeKey_1(string)).substr(3, 24)

    def makeKey_42(string):
        return hex_md5(makeKey_9(string) + makeKey_4(string)).substr(4, 24)

    def makeKey_43(string):
        return hex_md5(makeKey_10(string) + makeKey_5(string)).substr(1, 24)

    def makeKey_44(string):
        return hex_md5(makeKey_17(string) + makeKey_3(string)).substr(2, 24)

    def makeKey_45(string):
        return hex_md5(makeKey_18(string) + makeKey_7(string)).substr(3, 24)

    def makeKey_46(string):
        return hex_md5(makeKey_19(string) + makeKey_17(string)).substr(4, 24)

    def makeKey_47(string):
        return hex_md5(makeKey_0(string) + makeKey_18(string)).substr(1, 24)

    def makeKey_48(string):
        return hex_md5(makeKey_1(string) + makeKey_19(string)).substr(2, 24)

    def makeKey_49(string):
        return hex_md5(makeKey_4(string) + makeKey_0(string)).substr(3, 24)

    def makeKey_50(string):
        return hex_md5(makeKey_5(string) + makeKey_1(string)).substr(4, 24)

    def makeKey_51(string):
        return hex_md5(makeKey_3(string) + makeKey_4(string)).substr(1, 24)

    def makeKey_52(string):
        return hex_md5(makeKey_7(string) + makeKey_14(string)).substr(2, 24)

    def makeKey_53(string):
        return hex_md5(makeKey_12(string) + makeKey_15(string)).substr(3, 24)

    def makeKey_54(string):
        return hex_md5(makeKey_14(string) + makeKey_16(string)).substr(4, 24)

    def makeKey_55(string):
        return hex_md5(makeKey_15(string) + makeKey_9(string)).substr(3, 24)

    def makeKey_56(string):
        return hex_md5(makeKey_16(string) + makeKey_10(string)).substr(4, 24)

    def makeKey_57(string):
        return hex_md5(makeKey_9(string) + makeKey_17(string)).substr(1, 24)

    def makeKey_58(string):
        return hex_md5(makeKey_10(string) + makeKey_18(string)).substr(2, 24)

    def makeKey_59(string):
        return hex_md5(makeKey_17(string) + makeKey_19(string)).substr(3, 24)

    def makeKey_60(string):
        return hex_md5(makeKey_18(string) + makeKey_0(string)).substr(1, 24)

    def makeKey_61(string):
        return hex_md5(makeKey_19(string) + makeKey_1(string)).substr(2, 24)

    def makeKey_62(string):
        return hex_md5(makeKey_0(string) + makeKey_4(string)).substr(3, 24)

    def makeKey_63(string):
        return hex_md5(makeKey_1(string) + makeKey_19(string)).substr(4, 24)

    def makeKey_64(string):
        return hex_md5(makeKey_4(string) + makeKey_0(string)).substr(3, 24)

    def makeKey_65(string):
        return hex_md5(makeKey_14(string) + makeKey_1(string)).substr(1, 24)

    def makeKey_66(string):
        return hex_md5(makeKey_15(string) + makeKey_4(string)).substr(2, 24)

    def makeKey_67(string):
        return hex_md5(makeKey_16(string) + makeKey_5(string)).substr(3, 24)

    def makeKey_68(string):
        return hex_md5(makeKey_9(string) + makeKey_3(string)).substr(4, 24)

    def makeKey_69(string):
        return hex_md5(makeKey_10(string) + makeKey_7(string)).substr(1, 24)

    def makeKey_70(string):
        return hex_md5(makeKey_17(string) + makeKey_0(string)).substr(2, 24)

    def makeKey_71(string):
        return hex_md5(makeKey_18(string) + makeKey_1(string)).substr(3, 24)

    def makeKey_72(string):
        return hex_md5(makeKey_19(string) + makeKey_4(string)).substr(4, 24)

    def makeKey_73(string):
        return hex_md5(makeKey_0(string) + makeKey_17(string)).substr(1, 24)

    def makeKey_74(string):
        return hex_md5(makeKey_1(string) + makeKey_18(string)).substr(2, 24)

    def makeKey_75(string):
        return hex_md5(makeKey_14(string) + makeKey_19(string)).substr(3, 24)

    def makeKey_76(string):
        return hex_md5(makeKey_15(string) + makeKey_0(string)).substr(4, 24)

    def makeKey_77(string):
        return hex_md5(makeKey_16(string) + makeKey_1(string)).substr(3, 24)

    def makeKey_78(string):
        return hex_md5(makeKey_9(string) + makeKey_4(string)).substr(4, 24)

    def makeKey_79(string):
        return hex_md5(makeKey_10(string) + makeKey_9(string)).substr(1, 24)

    def makeKey_80(string):
        return hex_md5(makeKey_17(string) + makeKey_10(string)).substr(2, 24)

    def makeKey_81(string):
        return hex_md5(makeKey_18(string) + makeKey_17(string)).substr(3, 24)

    def makeKey_82(string):
        return hex_md5(makeKey_14(string) + makeKey_18(string)).substr(1, 24)

    def makeKey_83(string):
        return hex_md5(makeKey_15(string) + makeKey_19(string)).substr(4, 24)

    def makeKey_84(string):
        return hex_md5(makeKey_16(string) + makeKey_0(string)).substr(1, 24)

    def makeKey_85(string):
        return hex_md5(makeKey_9(string) + makeKey_1(string)).substr(2, 24)

    def makeKey_86(string):
        return hex_md5(makeKey_10(string) + makeKey_4(string)).substr(3, 24)

    def makeKey_87(string):
        return hex_md5(makeKey_14(string) + makeKey_14(string)).substr(4, 24)

    def makeKey_88(string):
        return hex_md5(makeKey_15(string) + makeKey_15(string)).substr(1, 24)

    def makeKey_89(string):
        return hex_md5(makeKey_16(string) + makeKey_16(string)).substr(2, 24)

    def makeKey_90(string):
        return hex_md5(makeKey_9(string) + makeKey_9(string)).substr(3, 24)

    def makeKey_91(string):
        return hex_md5(makeKey_10(string) + makeKey_10(string)).substr(4, 24)

    def makeKey_92(string):
        return hex_md5(makeKey_17(string) + makeKey_17(string)).substr(3, 24)

    def makeKey_93(string):
        return hex_md5(makeKey_18(string) + makeKey_18(string)).substr(4, 24)

    def makeKey_94(string):
        return hex_md5(makeKey_19(string) + makeKey_19(string)).substr(1, 24)

    def makeKey_95(string):
        return hex_md5(makeKey_0(string) + makeKey_0(string)).substr(2, 24)

    def makeKey_96(string):
        return hex_md5(makeKey_1(string) + makeKey_1(string)).substr(3, 24)

    def makeKey_97(string):
        return hex_md5(makeKey_4(string) + makeKey_4(string)).substr(4, 24)

    def makeKey_98(string):
        return hex_md5(makeKey_5(string) + makeKey_5(string)).substr(3, 24)

    def makeKey_99(string):
        return hex_md5(makeKey_3(string) + makeKey_3(string)).substr(4, 24)

    def makeKey_100(string):
        return hex_md5(makeKey_7(string) + makeKey_3(string)).substr(1, 24)

    def makeKey_101(string):
        return hex_md5(makeKey_10(string) + makeKey_7(string)).substr(2, 24)

    def makeKey_102(string):
        return hex_md5(makeKey_17(string) + makeKey_18(string)).substr(1, 24)

    def makeKey_103(string):
        return hex_md5(makeKey_18(string) + makeKey_19(string)).substr(2, 24)

    def makeKey_104(string):
        return hex_md5(makeKey_19(string) + makeKey_0(string)).substr(3, 24)

    def makeKey_105(string):
        return hex_md5(makeKey_0(string) + makeKey_0(string)).substr(4, 24)

    def makeKey_106(string):
        return hex_md5(makeKey_1(string) + makeKey_1(string)).substr(1, 24)

    def makeKey_107(string):
        return hex_md5(makeKey_14(string) + makeKey_14(string)).substr(2, 24)

    def makeKey_108(string):
        return hex_md5(makeKey_15(string) + makeKey_15(string)).substr(3, 24)

    def makeKey_109(string):
        return hex_md5(makeKey_16(string) + makeKey_16(string)).substr(4, 24)

    def makeKey_110(string):
        return hex_md5(makeKey_9(string) + makeKey_9(string)).substr(1, 24)

    def makeKey_111(string):
        return hex_md5(makeKey_10(string) + makeKey_10(string)).substr(2, 24)

    def makeKey_112(string):
        return hex_md5(makeKey_17(string) + makeKey_17(string)).substr(3, 24)

    def makeKey_113(string):
        return hex_md5(makeKey_18(string) + makeKey_18(string)).substr(4, 24)

    def makeKey_114(string):
        return hex_md5(makeKey_19(string) + makeKey_19(string)).substr(3, 24)

    def makeKey_115(string):
        return hex_md5(makeKey_0(string) + makeKey_0(string)).substr(4, 24)

    def makeKey_116(string):
        return hex_md5(makeKey_1(string) + makeKey_1(string)).substr(1, 24)

    def makeKey_117(string):
        return hex_md5(makeKey_4(string) + makeKey_4(string)).substr(2, 24)

    def makeKey_118(string):
        return hex_md5(makeKey_5(string) + makeKey_15(string)).substr(3, 24)

    def makeKey_119(string):
        return hex_md5(makeKey_3(string) + makeKey_16(string)).substr(1, 24)

    def makeKey_120(string):
        return hex_md5(makeKey_19(string) + makeKey_9(string)).substr(1, 24)

    def makeKey_121(string):
        return hex_md5(makeKey_0(string) + makeKey_10(string)).substr(2, 24)

    def makeKey_122(string):
        return hex_md5(makeKey_1(string) + makeKey_17(string)).substr(3, 24)

    def makeKey_123(string):
        return hex_md5(makeKey_4(string) + makeKey_18(string)).substr(4, 24)

    def makeKey_124(string):
        return hex_md5(makeKey_5(string) + makeKey_19(string)).substr(1, 24)

    def makeKey_125(string):
        return hex_md5(makeKey_3(string) + makeKey_0(string)).substr(2, 24)

    def makeKey_3(string):
        string = string.substr(5, 5 * 5) + '15' + string.substr(1, 2) + string.substr((5 + 1) * (5 + 1), 3)
        a = strToLongEn(string.substr(5)) + string.substr(4)
        b = string.substr(4) + a.substr(5)
        c = strToLong(string.substr(5)) + string.substr(4)
        return hex_md5(b).substr(3, 24)

    def makeKey_4(string):
        string = string.substr(5, 5 * 5) + '2' + string.substr(1, 2) + string.substr((5 + 1) * (5 + 1), 3)
        long = 0
        i = 0
        while i < string.substr(1).length:
            long += (string.charCodeAt(i) << (i % 16))
            i += 1

        aa = JsInt(long) + string.substr(4)
        long = 0
        a = string.substr(5)
        i = 0
        while i < a.length:
            long += (a.charCodeAt(i) << (i % 16)) + i
            i += 1

        a = long + '' + string.substr(4)
        b = hex_md5(string.substr(1)) + strToLong(a.substr(5))
        return hex_md5(b).substr(3, 24)

    def makeKey_5(string):
        base = Base64()
        string = base.encode(string.substr(5, 5 * 5) + string.substr(1, 2) + '1') + string.substr((5 + 1) * (5 + 1), 3)
        a = strToLongEn(string.substr(4, 10)) + string.substr(-4)
        b = hex_md5(string.substr(4)) + a.substr(2)
        a = string.substr(3)
        c = strToLong(string.substr(5)) + string.substr(4)
        aa = JsInt(long) + string.substr(4)
        long = 0
        i = 0
        while i < a.length:
            long += (a.charCodeAt(i) << (i % 12)) + i
            i += 1

        a = long + '' + string.substr(4)
        return hex_md5(string).substr(4, 24)

    def makeKey_6(string):
        base = Base64()
        string = string.substr(5, 5 * 5) + string.substr((5 + 1) * (5 + 1), 3)
        a = base.encode(string.substr(4, 10)) + string.substr(2)
        b = string.substr(6) + a.substr(2)
        c = strToLong(string.substr(5)) + string.substr(4)
        aa = JsInt(long) + string.substr(4)
        long = 0
        a = string.substr(5)
        i = 0
        while i < a.length:
            long += (a.charCodeAt(i) << (i % 16)) + i
            i += 1

        a = long + '' + string.substr(4)
        return hex_md5(b).substr(2, 24)

    def makeKey_126(string):
        return hex_md5(makeKey_7(string) + makeKey_1(string)).substr(3, 24)

    def makeKey_127(string):
        return hex_md5(makeKey_3(string) + makeKey_4(string)).substr(4, 24)

    def makeKey_128(string):
        return hex_md5(makeKey_7(string) + makeKey_5(string)).substr(1, 24)

    def makeKey_129(string):
        return hex_md5(makeKey_8(string) + makeKey_3(string)).substr(2, 24)

    def makeKey_177(string):
        return hex_md5(makeKey_9(string) + makeKey_0(string)).substr(3, 24)

    def makeKey_178(string):
        return hex_md5(makeKey_10(string) + makeKey_1(string)).substr(4, 24)

    def makeKey_179(string):
        return hex_md5(makeKey_17(string) + makeKey_4(string)).substr(1, 24)

    def makeKey_180(string):
        return hex_md5(makeKey_18(string) + makeKey_14(string)).substr(3, 24)

    # 获取cookies
    # cookie = getCookie('vjkl5')
    cookie = JsStr(param)
    # 定义函数的列表长度为 200
    arrFun = [makeKey_0, makeKey_1, makeKey_2, makeKey_3, makeKey_4, makeKey_5, makeKey_6, makeKey_7, makeKey_8,
              makeKey_9, makeKey_10, makeKey_11, makeKey_12, makeKey_13, makeKey_14, makeKey_15, makeKey_16, makeKey_17,
              makeKey_18, makeKey_19, makeKey_20, makeKey_21, makeKey_22, makeKey_23, makeKey_24, makeKey_25,
              makeKey_26, makeKey_27, makeKey_28, makeKey_29, makeKey_30, makeKey_31, makeKey_32, makeKey_33,
              makeKey_34, makeKey_35, makeKey_36, makeKey_37, makeKey_38, makeKey_39, makeKey_40, makeKey_41,
              makeKey_42, makeKey_43, makeKey_44, makeKey_45, makeKey_46, makeKey_47, makeKey_48, makeKey_49,
              makeKey_50, makeKey_51, makeKey_52, makeKey_53, makeKey_54, makeKey_55, makeKey_56, makeKey_57,
              makeKey_58, makeKey_59, makeKey_60, makeKey_61, makeKey_62, makeKey_63, makeKey_64, makeKey_65,
              makeKey_66, makeKey_67, makeKey_68, makeKey_69, makeKey_70, makeKey_71, makeKey_72, makeKey_73,
              makeKey_74, makeKey_75, makeKey_76, makeKey_77, makeKey_78, makeKey_79, makeKey_80, makeKey_81,
              makeKey_82, makeKey_83, makeKey_84, makeKey_85, makeKey_86, makeKey_87, makeKey_88, makeKey_89,
              makeKey_90, makeKey_91, makeKey_92, makeKey_93, makeKey_94, makeKey_95, makeKey_96, makeKey_97,
              makeKey_98, makeKey_99, makeKey_100, makeKey_101, makeKey_102, makeKey_103, makeKey_104, makeKey_105,
              makeKey_106, makeKey_107, makeKey_108, makeKey_109, makeKey_110, makeKey_111, makeKey_112, makeKey_113,
              makeKey_114, makeKey_115, makeKey_116, makeKey_117, makeKey_118, makeKey_119, makeKey_120, makeKey_121,
              makeKey_122, makeKey_123, makeKey_124, makeKey_125, makeKey_126, makeKey_127, makeKey_128, makeKey_129,
              makeKey_130, makeKey_131, makeKey_132, makeKey_133, makeKey_134, makeKey_135, makeKey_136, makeKey_137,
              makeKey_138, makeKey_139, makeKey_140, makeKey_141, makeKey_142, makeKey_143, makeKey_144, makeKey_145,
              makeKey_146, makeKey_147, makeKey_148, makeKey_149, makeKey_150, makeKey_151, makeKey_152, makeKey_153,
              makeKey_154, makeKey_155, makeKey_156, makeKey_157, makeKey_158, makeKey_159, makeKey_160, makeKey_161,
              makeKey_162, makeKey_163, makeKey_164, makeKey_165, makeKey_166, makeKey_167, makeKey_168, makeKey_169,
              makeKey_170, makeKey_171, makeKey_172, makeKey_173, makeKey_174, makeKey_175, makeKey_176, makeKey_177,
              makeKey_178, makeKey_179, makeKey_180, makeKey_181, makeKey_182, makeKey_183, makeKey_184, makeKey_185,
              makeKey_186, makeKey_187, makeKey_188, makeKey_189, makeKey_190, makeKey_191, makeKey_192, makeKey_193,
              makeKey_194, makeKey_195, makeKey_196, makeKey_197, makeKey_198, makeKey_199]
    # strToLong(string) ==> 将每个字符转换成ascii码,乘以2的它的下标的幂次方,相加
    # long
    # index,val in enumeratestr):
    #     long += ord(val)*2**index
    # reducelambda x,y:x+y, [ord(x)*2**i i,x in enumerate(string)]
    # cookies按以上方法转化成数字后除以200取余数
    funIndex = strToLong(cookie) % len(arrFun)
    # 以余数为下标获取相应的加密函数
    fun = arrFun[funIndex]
    # 使用加密函数对cookie进行加密
    result = fun(cookie)
    print(fun)
    return result

if __name__ == '__main__':
    # e73de30a99467fe2e7ace99
    a = 'd1cfa0ff7fde9e0117186e1912ebf23abbbe6945'
    print(getKey(a))

