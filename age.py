drving = input ('請問你有沒有開過車?')
if drving != '有' and  drving != '沒有' :
	print('只能輸入有或沒有')
raise SystemExit

age = input ('請問你的年紀?')
age =int(age)
if drving =='有':
	if age >= 18:
		print ('你通過測試了!')
	else :
		print ('奇怪你怎麼開過車，你不能開車啊!')
elif drving =='沒有':
	if age >= 18:
	    print ('你可以考駕駛執照了，加油!')
	else :
		print ('再過幾年就可以考駕駛執照')
