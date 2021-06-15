def basic_symp(fever,cough,fatigue,bodypain,appetite):
	total = 0
	if fever == '1':
		total+=4
	if cough == '1':
		total += 6
	if fatigue == '1':
		total+=7
	if bodypain == "1":
		total+= 8
	if appetite == "1":
		total+=7

	if total <25:
		return False
	return True


def mid_symptoms(nose,nausea,smell):
	total = 4
	if nose == "1":
		total+=5
	if nausea == "1":
		total+=4
	if smell == "1":
		total+=4
	if total > 6:
		return True
	return False


def danger_symptoms(a,b):
	if a == "1" or b == '1':
		return True
	return False