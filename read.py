data = [] #存放每筆留言的list
sum_len = 0

with open('reviews.txt', 'r') as f :
	for line in f :
		data.append(line)
		sum_len = sum_len + len(line) # 每筆留言的長度總和

avg_len = sum_len / len(data)
print('總共有', len(data), '筆資料')
print('平均留言長度為', avg_len)

#篩選留言數小於100字的留言
len_100 = []
for d in data :
	if len(d) < 100 :
		len_100.append(d)
print('有', len(len_100), '筆資料長度小於100')

#篩選留言內容有bad
bad = []
for d in data :
	if 'bad' in d :
		bad.append(d)
print('有', len(bad), '筆資料內容有bad')
print(bad[0])