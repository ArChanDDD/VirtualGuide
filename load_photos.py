from ImageParser import YandexImage
import requests

parser = YandexImage()

print(parser.about, parser.version)

counter = 4010
last_counter = 0
pointer = 0
answers = []
asks = ['Газпром Арена', 'Газпром арена сбоку', 'Газпром Арена Санкт-Петербург',
        'Gazprom arena', 'Gazprom arena Saint petersburg', 'Gazprom arena winter', 'Gazprom arena autumn',
        'Gazprom arena spring']
remember = {}
for i, ya_ask in enumerate(asks):
    print(i / len(asks))
    for item in parser.search(ya_ask, sizes=parser.size.small):
        print('ok')
        try:
            counter += 1
            try:
                if item.url in remember[item.width][item.height]:
                    continue
                else:
                    remember[item.width][item.height].append(item.url)
            except:
                if item.width not in remember.keys():
                    remember[item.width] = {item.height: [item.url]}
                elif item.height not in remember[item.width].keys():
                    remember[item.width][item.height] = [item.url]
            img_data = requests.get(item.url).content
            if len(img_data) < 200:
                counter -= 1
                continue
            with open('data/' + str(counter) + '.jpg', 'wb') as handler:
                handler.write(img_data)
        except:
            pass
    print('+1')
    for item in parser.search(ya_ask, sizes=parser.size.medium):
        print('ok')
        try:
            counter += 1
            try:
                if item.url in remember[item.width][item.height]:
                    continue
                else:
                    remember[item.width][item.height].append(item.url)
            except:
                if item.width not in remember.keys():
                    remember[item.width] = {item.height: [item.url]}
                elif item.height not in remember[item.width].keys():
                    remember[item.width][item.height] = [item.url]
            img_data = requests.get(item.url).content
            if len(img_data) < 200:
                counter -= 1
                continue
            with open('data/' + str(counter) + '.jpg', 'wb') as handler:
                handler.write(img_data)
        except:
            pass
    print('+2')
    for item in parser.search(ya_ask, sizes=parser.size.large):
        print('ok')
        try:
            counter += 1
            try:
                if item.url in remember[item.width][item.height]:
                    continue
                else:
                    remember[item.width][item.height].append(item.url)
            except:
                if item.width not in remember.keys():
                    remember[item.width] = {item.height: [item.url]}
                elif item.height not in remember[item.width].keys():
                    remember[item.width][item.height] = [item.url]
            img_data = requests.get(item.url).content
            if len(img_data) < 200:
                counter -= 1
                continue
            with open('data/' + str(counter) + '.jpg', 'wb') as handler:
                handler.write(img_data)
        except:
            pass
    if (i + 1) % 8 == 0:
        for j in range(last_counter, counter):
            answers.append(pointer)
        last_counter = counter
        remember = {}
print(answers)
