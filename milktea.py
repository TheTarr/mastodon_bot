import sys
import random
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

mylist = ['红茶', '绿茶', '水果茶', '乌龙茶', '茉莉花茶', '普洱茶', '鸭屎香（凤凰单丛茶）', '四季春茶', '白茶', '铁观音','可可','阿华田','花茶']
mylist2 = ['珍珠', '布丁', '仙草', '红豆', '椰果', '芋圆', '西米', '咖啡冻', '椰奶冻', '紫米', '燕麦', '不加料']

flag1 = random.randint(0, len(mylist)-1)
flag2 = random.randint(0, len(mylist2)-1)
print("操操的推荐是"+ mylist[flag1]+"或你想喝的茶底，加料："+ mylist2[flag2])