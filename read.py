data = []
sum_len = 0

with open('reviews.txt', 'r') as f :
	for line in f :
		data.append(line)
		sum_len = sum_len + len(line) # 每筆留言的長度總和

avg_len = sum_len / len(data)
print('總共有', len(data), '筆資料')
print('平均留言長度為', avg_len)