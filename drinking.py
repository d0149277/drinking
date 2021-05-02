drinking = input('你有沒有喝過酒: ')
if drinking !='有' and drinking !='沒有':
    print('只能輸入"有"或"沒有"')
    raise SystemExit
age = input('你今年幾歲: ')
age = int(age)
if drinking == '有':
	if age >=18:
		print('可以飲酒,但是請注意飲酒過量傷身')
	else:
		print('未成年請勿飲酒,警察已在路上')
elif drinking == '沒有':
    if age >=18:
    	print('不喝酒很健康,不過小酌也可以強身')
    else:
        print('乖孩子,請繼續保持')