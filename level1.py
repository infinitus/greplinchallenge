#!/usr/bin/env python
dataString = """FourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceivedinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedinagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"""
indexMin = 0
indexMax = 0
offset = 20 #longest length the palindrome might be
answerLen = 0


def isPalindrome(string):
    string = str(string)
    for index in range(len(string)/2):
        if (string[index] != string[-1-index]):
            return False
    return True


for indexMin in range(len(dataString)-offset):
    for indexMax in range(indexMin+1,indexMin+offset):
        slicedstring = dataString[indexMin:indexMax] 
        if isPalindrome(slicedstring):
            if len(slicedstring) > answerLen:
                answerLen = len(slicedstring)
                answer = slicedstring		


print("The longest palindrome is '" + answer + "'.")
