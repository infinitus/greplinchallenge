#!/usr/bin/env python
dataString = """FourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceivedinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedinagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"""
indexMin = 0
indexMax = 0
offset = 20 #longest length the anagram might be
unSymFlag = 0
content = ""
answer = ""
answerLen = 0

#first character
for indexMin in range(len(dataString)-offset):
	#last character
    for indexMax in range(indexMin+1,indexMin+offset):
		#slicing
        content = dataString[indexMin:indexMax] 

		#even number of characters
        if len(content) % 2 == 0:
            for i in range(len(content)/2+1):
                if content[i-1] != content [-i]:
                    unSymFlag=1

		#odd number of characters
        else:
            for i in range(((len(content)+1)/2)+1):
                if content[i-1] != content [-i]:
                    unSymFlag=1

		#check if sliced word is symmetrical
        if unSymFlag != 1:
			
			#check if symmetrical word is the longest
            if len(content) > answerLen:
				answerLen = len(content)
				answer = content		

		#reset flag
        unSymFlag = 0

print("The longest anagram is '" + answer + "'.")
