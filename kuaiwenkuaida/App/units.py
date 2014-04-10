#-*- coding:utf-8 -*-

#工具集,为本项目提供工具
#作者：yfl<yerugemimi@gmail.com>
#最后修改时间：2014-04-10

#Cursor结果是元组，将转换为list
def tupleToList(yuanzu):
	rlist=[]
	#判断返回list的维度
	if len(yuanzu[0]) ==1 :
		rlist=[p[0] for p in yuanzu]
	else:
		rlist=[list(p) for p in yuanzu]

	return rlist 