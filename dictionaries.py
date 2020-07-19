mystuff = {"key1":"value1", "key2":"value2"}
print(mystuff['key1'])

mystuff2 = {"key1":123, "key2":"value2", "key3":{'123':[1,2,3]}}
print(mystuff2)

mystuff3 = {"key1":123, "key2":"value2", "key3":{'123':[1,2, 'grabMe']}}
print(mystuff3 ['key3']['123'][2])

mystuff4 = {"key1":123, "key2":"value2", "key3":{'123':[1,2, 'grabMe']}}
print(mystuff4 ['key3']['123'][2].upper())

mystuff5 = {"lunch":"pizza", "bfast":"eggs"}
mystuff5['lunch'] = 'burger'
mystuff5['dinner'] = 'pasta'
print(mystuff5['lunch'])
print(mystuff5)
