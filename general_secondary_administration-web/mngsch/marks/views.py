from django.shortcuts import render,get_object_or_404,redirect

from .models import Tmt2,Tmt,terms,year,nameschool
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
import sqlite3
g=year.objects.get(pk=1)
yearnow=str(g.yearr)
# Create your views here.
def sch1(request):
	#if not request.user.is_authenticated:
	db1=sqlite3.connect(yearnow+'.db')
	db1.row_factory=sqlite3.Row
	db1.execute('create table if not exists tabladdrow(ID integer primary Key autoincrement,namrow text,roww text)')
	
	ro1=db1.execute("select * from tabladdrow")
	#db1.execute('''insert into tabladdrow(namrow,roww) values(?,?)''',(namerow,namerow2))
	#db1.commit()
	
	return render(request,'sch/sc1.html',{'g':ro1,'yearnow':yearnow,'termnow':terms.objects.get(pk=1),'nameschool':nameschool.objects.get(pk=1)})

def adds(request):
	db1=sqlite3.connect(yearnow+'.db')
	#cb=db1.cursor()
	db1.row_factory=sqlite3.Row
	ro1=db1.execute("select * from tabladdrow")
	#ro1=cb.fetchall()
	#for n in ro1:
	#	print(n['roww'])
	return render(request,'sch/shoone.html',{'g':ro1,'f1':'1','yearnow':yearnow,'termnow':terms.objects.get(pk=1),'nameschool':nameschool.objects.get(pk=1)})
def addrow(request):
	if request.method=='POST':
		rownew=request.POST.get("rownew")
		rowname=request.POST.get("rowname")
		#if rowname[-1]=='1':
		if len(rownew)<5:
			messages.info(request,'خطاء في كتابة اسم الصف الرجاء اعادة الاسم مرة اخرى حسب معايير البرنامج')
			return redirect('adds')
		try:
				
			if rownew[0:4]==rowname and type(int(rownew[-1:]))==int:	
				db1=sqlite3.connect(yearnow+'.db')
				db1.row_factory=sqlite3.Row
				db1.execute("insert into tabladdrow(namrow,roww) values(?,?)",(rowname,rownew))
				db1.commit()
				messages.info(request,'complet adds')
			else:
				messages.info(request,'خطاء في كتابة اسم الصف الرجاء اعادة الاسم مرة اخرى حسب معايير البرنامج')
		except:
			messages.info(request,'خطاء في كتابة اسم الصف الرجاء اعادة الاسم مرة اخرى حسب معايير البرنامج')
			
		
	return redirect('adds')
def chrow(request):
	if request.method=='POST':
		rownew=request.POST.get("namrow")
		db1=sqlite3.connect(yearnow+'.db')
		db1.row_factory=sqlite3.Row
		ro1=db1.execute("select * from tabladdrow where namrow='{}'".format(rownew))
	return render(request,'sch/shoone.html',{'g':ro1,'f2':rownew,'yearnow':yearnow,'termnow':terms.objects.get(pk=1),'nameschool':nameschool.objects.get(pk=1)})
def matrel(namestudy,namrowstu):
	yt=terms.objects.get(pk=1)
	db1=sqlite3.connect(yearnow+'.db')
	db1.row_factory=sqlite3.Row
	if yt.term=='الفصل الاول':
			
		db1.execute('create table if not exists qran(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
		db1.execute('''insert into qran(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
		db1.commit()
		db1.execute('create table if not exists aslm(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
		db1.execute('''insert into aslm(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
		db1.commit()
		db1.execute('create table if not exists arbic(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
		db1.execute('''insert into arbic(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
		db1.commit()
		db1.execute('create table if not exists readeat(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
		db1.execute('''insert into readeat(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
		db1.commit()
		db1.execute('create table if not exists alom(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
		db1.execute('''insert into alom(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
		db1.commit()
		if int(namrowstu[-2])>=3:
			
			db1.execute('create table if not exists ajtm(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
			db1.execute('''insert into ajtm(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
			db1.commit()
		if int(namrowstu[-2])>=7:
			
			db1.execute('create table if not exists english(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
			db1.execute('''insert into english(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
			db1.commit()
	else:
		db1.execute('create table if not exists qran2(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
		db1.execute('''insert into qran2(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
		db1.commit()
		db1.execute('create table if not exists aslm2(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
		db1.execute('''insert into aslm2(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
		db1.commit()
		db1.execute('create table if not exists arbic2(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
		db1.execute('''insert into arbic2(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
		db1.commit()
		db1.execute('create table if not exists readeat2(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
		db1.execute('''insert into readeat2(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
		db1.commit()
		db1.execute('create table if not exists alom2(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
		db1.execute('''insert into alom2(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
		db1.commit()
		if int(namrowstu[-2])>=3:
			
			db1.execute('create table if not exists ajtm2(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
			db1.execute('''insert into ajtm2(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
			db1.commit()
		if int(namrowstu[-2])>=7:
			
			db1.execute('create table if not exists english2(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
			db1.execute('''insert into english2(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
			db1.commit()
		

def addstud(request):
	p1=[]
	if request.method=='POST':
		rownew=request.POST.get("namerow")
		namst=request.POST.get("namestu")
		namero=request.POST.get("row")
		db1=sqlite3.connect(yearnow+'.db')
		db1.row_factory=sqlite3.Row
		yt=terms.objects.get(pk=1)
		if yt.term=='الفصل الاول':
			ro1=db1.execute("select * from tabladdstudynt")
			for n in ro1:
				p1.append(n['namst'])
			if namst in p1:
				messages.info(request,'الاسم موجود')
				return redirect('adds')
				
			db1.execute('create table if not exists tabladdstudynt(ID integer primary Key autoincrement,namst text,rowst text)')
			db1.execute('''insert into tabladdstudynt(namst,rowst) values(?,?)''',(namst,namero))
			db1.commit()
		else:
			ro1=db1.execute("select * from tabladdstudynt2")
			for n in ro1:
				p1.append(n['namst'])
			if namst in p1:
				messages.info(request,'الاسم موجود')
				return redirect('adds')
			db1.execute('create table if not exists tabladdstudynt2(ID integer primary Key autoincrement,namst text,rowst text)')
			db1.execute('''insert into tabladdstudynt2(namst,rowst) values(?,?)''',(namst,namero))
			db1.commit()
		matrel(namst,namero)#######################################inclued function matreal 
		messages.info(request,'complet adds')
	return redirect('adds')
def shost(request):
	p=[]
	p1=[]
	db1=sqlite3.connect('db.sqlite3')
	db1.row_factory=sqlite3.Row
	#ro1=db1.execute("select * from marks_tmt2_namerow1 where tmt2_id='{}'".format(request.user.pk))
	f=Tmt2.objects.all().filter(nameuser=str(request.user))
	
	
	return render(request,'sch/shost.html',{'g':f,'yearnow':yearnow,'termnow':terms.objects.get(pk=1),'nameschool':nameschool.objects.get(pk=1)})#filter(nameuser=str(request.user))
	#f=Tmt.objects.all().filter(pk=w)
	#print(f)
	##print(i)
	##print(h.namerow1__pk)
	#t1=Tmt2.objects.filter(namerow1__id=)
	#print(t1)
		
def shost2(request):#####################################################################
	if request.method=='POST':
		yt=terms.objects.get(pk=1)
		nr=request.POST.get("nr")
		db1=sqlite3.connect(yearnow+'.db')
		db1.row_factory=sqlite3.Row
		if yt.term=='الفصل الاول':
			
			ro1=db1.execute("select * from tabladdstudynt where rowst='{}'".format(nr))
		else:
			ro1=db1.execute("select * from tabladdstudynt2 where rowst='{}'".format(nr))
	return render(request,'sch/shost.html',{'i':ro1,'u':'same','rn':nr,'yearnow':yearnow,'termnow':terms.objects.get(pk=1),'nameschool':nameschool.objects.get(pk=1)})

def shost3(request):
	y=[]
	p1=[]
	if request.method=='POST':
		yt=terms.objects.get(pk=1)
		nr=request.POST.get("gn")
		if nr=='none'or nr=='':
			return render(request,'sch/shost.html')
		db1=sqlite3.connect(yearnow+'.db')
		db1.row_factory=sqlite3.Row
		if yt.term=='الفصل الاول':
			
			ro1=db1.execute("select * from tabladdstudynt where namst='{}'".format(nr))
			for n in ro1:
				namrowstu=n['rowst']
			f=Tmt2.objects.all().filter(nameuser=str(request.user))
			for b in f:
				y.append(b.typeperson)
			if 'A' in y:
				
				ro2=db1.execute("select * from qran where namst='{}'".format(nr))
				ro3=db1.execute("select * from aslm where namst='{}'".format(nr))
				ro4=db1.execute("select * from arbic where namst='{}'".format(nr))
				ro5=db1.execute("select * from readeat where namst='{}'".format(nr))
				ro6=db1.execute("select * from alom where namst='{}'".format(nr))
				if int(namrowstu[-2])>=3:
					ro7=db1.execute("select * from ajtm where namst='{}'".format(nr))
				else:ro7=''
				if int(namrowstu[-2])>=7:
					
					ro8=db1.execute("select * from english where namst='{}'".format(nr))
				else:ro8=''
			else:
				ro2,ro3,ro4,ro5,ro6,ro7,ro8='','','','','','',''
				for u in f:
					p1.append(u.namemtral)
				if 'qran' in p1:
					ro2=db1.execute("select * from qran where namst='{}'".format(nr))
				if 'aslm' in p1:
					ro3=db1.execute("select * from aslm where namst='{}'".format(nr))
				if 'arbic' in p1:
					ro4=db1.execute("select * from arbic where namst='{}'".format(nr))
				if 'readeat' in p1:
					ro5=db1.execute("select * from readeat where namst='{}'".format(nr))
				if 'alom' in p1:
					ro6=db1.execute("select * from alom where namst='{}'".format(nr))
				if 'ajtm' in p1:
					ro7=db1.execute("select * from ajtm where namst='{}'".format(nr))
				if 'english' in p1:
					ro8=db1.execute("select * from english where namst='{}'".format(nr))
				
		else:#####################################################term2
			
			
			ro1=db1.execute("select * from tabladdstudynt2 where namst='{}'".format(nr))
			for n in ro1:
				namrowstu=n['rowst']
			f=Tmt2.objects.all().filter(nameuser=str(request.user))
			for b in f:
				y.append(b.typeperson)
			if 'A' in y:
				
				ro2=db1.execute("select * from qran2 where namst='{}'".format(nr))
				ro3=db1.execute("select * from aslm2 where namst='{}'".format(nr))
				ro4=db1.execute("select * from arbic2 where namst='{}'".format(nr))
				ro5=db1.execute("select * from readeat2 where namst='{}'".format(nr))
				ro6=db1.execute("select * from alom2 where namst='{}'".format(nr))
				if int(namrowstu[-2])>=3:
					ro7=db1.execute("select * from ajtm2 where namst='{}'".format(nr))
				else:ro7=''
				if int(namrowstu[-2])>=7:
					
					ro8=db1.execute("select * from english2 where namst='{}'".format(nr))
				else:ro8=''
			else:
				ro2,ro3,ro4,ro5,ro6,ro7,ro8='','','','','','',''
				for u in f:
					p1.append(u.namemtral)
				if 'qran' in p1:
					ro2=db1.execute("select * from qran2 where namst='{}'".format(nr))
				if 'aslm' in p1:
					ro3=db1.execute("select * from aslm2 where namst='{}'".format(nr))
				if 'arbic' in p1:
					ro4=db1.execute("select * from arbic2 where namst='{}'".format(nr))
				if 'readeat' in p1:
					ro5=db1.execute("select * from readeat2 where namst='{}'".format(nr))
				if 'alom' in p1:
					ro6=db1.execute("select * from alom2 where namst='{}'".format(nr))
				if 'ajtm' in p1:
					ro7=db1.execute("select * from ajtm2 where namst='{}'".format(nr))
				if 'english' in p1:
					ro8=db1.execute("select * from english2 where namst='{}'".format(nr))
			
		shro=db1.execute("select * from tabladdrow")
	return render(request,'sch/shost.html',{'srow':shro,'ii':ro2,'ii2':ro3,'ii3':ro4,'ii4':ro5,'ii5':ro6,'ii6':ro7,'ii7':ro8,'rn':nr,'nst':namrowstu,'yearnow':yearnow,'termnow':terms.objects.get(pk=1),'nameschool':nameschool.objects.get(pk=1)})
def update1(request):
	y=[]
	if request.method=='POST':#qran
		yt=terms.objects.get(pk=1)
		nru1=request.POST.get("nru")
		nsu1=request.POST.get("nsu")
		nru=request.POST.get("nrs")
		nsu=request.POST.get("nss")
		f=Tmt2.objects.all().filter(nameuser=str(request.user))
		for b in f:
			y.append(b.typeperson)
		
		if yt.term=='الفصل الاول':#######################################################term one
			
			if 'A' in y:
				
				nru1=request.POST.get("nru")
				nsu1=request.POST.get("nsu")
				nru=request.POST.get("nrs")
				nsu=request.POST.get("nss")
				mo1=request.POST.get("1mo1")
				mo2=request.POST.get("1mo2")
				#ss1=request.POST.get("1s1")
				#ss2=request.POST.get("1s2")
				sh1=request.POST.get("1sh1")
				sh2=request.POST.get("1sh2")
				test1=request.POST.get("1test1")
				test2=request.POST.get("1test2")
				work1=request.POST.get("1work1")
				work2=request.POST.get("1work2")
				#su20=request.POST.get("1su20")
				su30=request.POST.get("1su30")
				#sut50=request.POST.get("1su50")
				shr1=((int(mo1)+int(sh1)+int(test1)+int(work1))/5)
				s1=int(shr1/2)
				shr2=((int(mo2)+int(sh2)+int(test2)+int(work2))/5)
				s2=int(shr2/2)
				su20=s1+s2
				su50=int(su30)+s1+s2
				
				db1=sqlite3.connect(yearnow+'.db')
				db1.row_factory=sqlite3.Row
				db1.execute("update tabladdstudynt set rowst='{}', namst='{}' where namst='{}' and rowst='{}'".format(nru1,nsu1,nsu,nru))
				
				db1.execute("update qran set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}',namero='{}', namst='{}' where namst='{}' and namero='{}'".format(mo1,mo2,sh1,sh2,test1,test2,work1,work2,s1,s2,su20,su30,su50,nru1,nsu1,nsu,nru))
				db1.commit()
		################################################################aslm
				mo12=request.POST.get("2mo1")
				mo22=request.POST.get("2mo2")
				#s12=request.POST.get("2s1")
				#s22=request.POST.get("2s2")
				sh12=request.POST.get("2sh1")
				sh22=request.POST.get("2sh2")
				test12=request.POST.get("2test1")
				test22=request.POST.get("2test2")
				work12=request.POST.get("2work1")
				work22=request.POST.get("2work2")
				#su202=request.POST.get("2su20")
				su302=request.POST.get("2su30")
				#su502=request.POST.get("2su50")
				
				shr1=((int(mo12)+int(sh12)+int(test12)+int(work12))/5)
				s12=int(shr1/2)
				shr2=((int(mo22)+int(sh22)+int(test22)+int(work22))/5)
				s22=int(shr2/2)
				su202=s12+s22
				su502=int(su302)+s12+s22
				
				db1=sqlite3.connect(yearnow+'.db')
				db1.row_factory=sqlite3.Row
				db1.execute("update aslm set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}',namero='{}', namst='{}' where namst='{}' and namero='{}'".format(mo12,mo22,sh12,sh22,test12,test22,work12,work22,s12,s22,su202,su302,su502,nru1,nsu1,nsu,nru))
				db1.commit()
		################################################################arbic
				mo13=request.POST.get("3mo1")
				mo23=request.POST.get("3mo2")
				#s13=request.POST.get("3s1")
				#s23=request.POST.get("3s2")
				sh13=request.POST.get("3sh1")
				sh23=request.POST.get("3sh2")
				test13=request.POST.get("3test1")
				test23=request.POST.get("3test2")
				work13=request.POST.get("3work1")
				work23=request.POST.get("3work2")
				#su203=request.POST.get("3su20")
				su303=request.POST.get("3su30")
				#su503=request.POST.get("3su50")
				
				shr1=((int(mo13)+int(sh13)+int(test13)+int(work13))/5)
				s13=int(shr1/2)
				shr2=((int(mo23)+int(sh23)+int(test23)+int(work23))/5)
				s23=int(shr2/2)
				su203=s13+s23
				su503=int(su303)+s13+s23
				
				db1=sqlite3.connect(yearnow+'.db')
				db1.row_factory=sqlite3.Row
				db1.execute("update arbic set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}',namero='{}', namst='{}' where namst='{}' and namero='{}'".format(mo13,mo23,sh13,sh23,test13,test23,work13,work23,s13,s23,su203,su303,su503,nru1,nsu1,nsu,nru))
				db1.commit()
				################################################################redeat
				mo14=request.POST.get("4mo1")
				mo24=request.POST.get("4mo2")
				#s14=request.POST.get("4s1")
				#s24=request.POST.get("4s2")
				sh14=request.POST.get("4sh1")
				sh24=request.POST.get("4sh2")
				test14=request.POST.get("4test1")
				test24=request.POST.get("4test2")
				work14=request.POST.get("4work1")
				work24=request.POST.get("4work2")
				#su204=request.POST.get("4su20")
				su304=request.POST.get("4su30")
				#su504=request.POST.get("4su50")
				
				shr1=((int(mo14)+int(sh14)+int(test14)+int(work14))/5)
				s14=int(shr1/2)
				shr2=((int(mo24)+int(sh24)+int(test24)+int(work24))/5)
				s24=int(shr2/2)
				su204=s14+s24
				su504=int(su304)+s14+s24
				
				db1=sqlite3.connect(yearnow+'.db')
				db1.row_factory=sqlite3.Row
				db1.execute("update readeat set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}',namero='{}', namst='{}' where namst='{}' and namero='{}'".format(mo14,mo24,sh14,sh24,test14,test24,work14,work24,s14,s24,su204,su304,su504,nru1,nsu1,nsu,nru))
				db1.commit()
				################################################################alom
				mo15=request.POST.get("5mo1")
				mo25=request.POST.get("5mo2")
				#s15=request.POST.get("5s1")
				#s25=request.POST.get("5s2")
				sh15=request.POST.get("5sh1")
				sh25=request.POST.get("5sh2")
				test15=request.POST.get("5test1")
				test25=request.POST.get("5test2")
				work15=request.POST.get("5work1")
				work25=request.POST.get("5work2")
				#su205=request.POST.get("5su20")
				su305=request.POST.get("5su30")
				#su505=request.POST.get("5su50")
				
				shr1=((int(mo15)+int(sh15)+int(test15)+int(work15))/5)
				s15=int(shr1/2)
				shr2=((int(mo25)+int(sh25)+int(test25)+int(work25))/5)
				s25=int(shr2/2)
				su205=s15+s25
				su505=int(su305)+s15+s25
				
				
				db1=sqlite3.connect(yearnow+'.db')
				db1.row_factory=sqlite3.Row
				db1.execute("update alom set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}',namero='{}', namst='{}' where namst='{}' and namero='{}'".format(mo15,mo25,sh15,sh25,test15,test25,work15,work25,s15,s25,su205,su305,su505,nru1,nsu1,nsu,nru))
				db1.commit()
				################################################################ajtmaet
				if int(nru[-2])>=3:
					mo16=request.POST.get("6mo1")
					mo26=request.POST.get("6mo2")
					#s16=request.POST.get("6s1")
					#s26=request.POST.get("6s2")
					sh16=request.POST.get("6sh1")
					sh26=request.POST.get("6sh2")
					test16=request.POST.get("6test1")
					test26=request.POST.get("6test2")
					work16=request.POST.get("6work1")
					work26=request.POST.get("6work2")
					#su206=request.POST.get("6su20")
					su306=request.POST.get("6su30")
					#su506=request.POST.get("6su50")
					
					shr1=((int(mo16)+int(sh16)+int(test16)+int(work16))/5)
					s16=int(shr1/2)
					shr2=((int(mo26)+int(sh26)+int(test26)+int(work26))/5)
					s26=int(shr2/2)
					su206=s16+s26
					su506=int(su306)+s16+s26
					
					
					db1=sqlite3.connect(yearnow+'.db')
					db1.row_factory=sqlite3.Row
					db1.execute("update ajtm set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}',namero='{}', namst='{}' where namst='{}' and namero='{}'".format(mo16,mo26,sh16,sh26,test16,test26,work16,work26,s16,s26,su206,su306,su506,nru1,nsu1,nsu,nru))
					db1.commit()
				
				################################################################english
				if int(nru[-2])>=7:
					mo17=request.POST.get("7mo1")
					mo27=request.POST.get("7mo2")
					#s17=request.POST.get("7s1")
					#s27=request.POST.get("7s2")
					sh17=request.POST.get("7sh1")
					sh27=request.POST.get("7sh2")
					test17=request.POST.get("7test1")
					test27=request.POST.get("7test2")
					work17=request.POST.get("7work1")
					work27=request.POST.get("7work2")
					#su207=request.POST.get("7su20")
					su307=request.POST.get("7su30")
					#su507=request.POST.get("7su50")
					
					shr1=((int(mo17)+int(sh17)+int(test17)+int(work17))/5)
					s17=int(shr1/2)
					shr2=((int(mo27)+int(sh27)+int(test27)+int(work27))/5)
					s27=int(shr2/2)
					su207=s17+s27
					su507=int(su307)+s17+s27
					
					db1=sqlite3.connect(yearnow+'.db')
					db1.row_factory=sqlite3.Row
					db1.execute("update english set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}',namero='{}', namst='{}' where namst='{}' and namero='{}'".format(mo17,mo27,sh17,sh27,test17,test27,work17,work27,s17,s27,su207,su307,su507,nru1,nsu1,nsu,nru))
					db1.commit()
			else:
					p1=[]
					for u in f:
						p1.append(u.namemtral)
					if 'qran' in p1:###############qran
						nru1=request.POST.get("nru")
						nsu1=request.POST.get("nsu")
						nru=request.POST.get("nrs")
						nsu=request.POST.get("nss")
						mo1=request.POST.get("1mo1")
						mo2=request.POST.get("1mo2")
						#ss1=request.POST.get("1s1")
						#ss2=request.POST.get("1s2")
						sh1=request.POST.get("1sh1")
						sh2=request.POST.get("1sh2")
						test1=request.POST.get("1test1")
						test2=request.POST.get("1test2")
						work1=request.POST.get("1work1")
						work2=request.POST.get("1work2")
						#su20=request.POST.get("1su20")
						su30=request.POST.get("1su30")
						#sut50=request.POST.get("1su50")
						shr1=((int(mo1)+int(sh1)+int(test1)+int(work1))/5)
						s1=int(shr1/2)
						shr2=((int(mo2)+int(sh2)+int(test2)+int(work2))/5)
						s2=int(shr2/2)
						su20=s1+s2
						su50=int(su30)+s1+s2
						
						db1=sqlite3.connect(yearnow+'.db')
						db1.row_factory=sqlite3.Row
						db1.execute("update tabladdstudynt set rowst='{}', namst='{}' where namst='{}' and rowst='{}'".format(nru1,nsu1,nsu,nru))
						
						db1.execute("update qran set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}',namero='{}', namst='{}' where namst='{}' and namero='{}'".format(mo1,mo2,sh1,sh2,test1,test2,work1,work2,s1,s2,su20,su30,su50,nru1,nsu1,nsu,nru))
						db1.commit()
					if 'aslm' in p1:##############################aslm
						mo12=request.POST.get("2mo1")
						mo22=request.POST.get("2mo2")
						#s12=request.POST.get("2s1")
						#s22=request.POST.get("2s2")
						sh12=request.POST.get("2sh1")
						sh22=request.POST.get("2sh2")
						test12=request.POST.get("2test1")
						test22=request.POST.get("2test2")
						work12=request.POST.get("2work1")
						work22=request.POST.get("2work2")
						#su202=request.POST.get("2su20")
						su302=request.POST.get("2su30")
						#su502=request.POST.get("2su50")
						
						shr1=((int(mo12)+int(sh12)+int(test12)+int(work12))/5)
						s12=int(shr1/2)
						shr2=((int(mo22)+int(sh22)+int(test22)+int(work22))/5)
						s22=int(shr2/2)
						su202=s12+s22
						su502=int(su302)+s12+s22
						
						db1=sqlite3.connect(yearnow+'.db')
						db1.row_factory=sqlite3.Row
						db1.execute("update aslm set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}',namero='{}', namst='{}' where namst='{}' and namero='{}'".format(mo12,mo22,sh12,sh22,test12,test22,work12,work22,s12,s22,su202,su302,su502,nru1,nsu1,nsu,nru))
						db1.commit()
					if 'arbic' in p1:
						mo13=request.POST.get("3mo1")
						mo23=request.POST.get("3mo2")
						#s13=request.POST.get("3s1")
						#s23=request.POST.get("3s2")
						sh13=request.POST.get("3sh1")
						sh23=request.POST.get("3sh2")
						test13=request.POST.get("3test1")
						test23=request.POST.get("3test2")
						work13=request.POST.get("3work1")
						work23=request.POST.get("3work2")
						#su203=request.POST.get("3su20")
						su303=request.POST.get("3su30")
						#su503=request.POST.get("3su50")
						
						shr1=((int(mo13)+int(sh13)+int(test13)+int(work13))/5)
						s13=int(shr1/2)
						shr2=((int(mo23)+int(sh23)+int(test23)+int(work23))/5)
						s23=int(shr2/2)
						su203=s13+s23
						su503=int(su303)+s13+s23
						
						db1=sqlite3.connect(yearnow+'.db')
						db1.row_factory=sqlite3.Row
						db1.execute("update arbic set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}',namero='{}', namst='{}' where namst='{}' and namero='{}'".format(mo13,mo23,sh13,sh23,test13,test23,work13,work23,s13,s23,su203,su303,su503,nru1,nsu1,nsu,nru))
						db1.commit()
					if 'readeat' in p1:
						mo14=request.POST.get("4mo1")
						mo24=request.POST.get("4mo2")
						#s14=request.POST.get("4s1")
						#s24=request.POST.get("4s2")
						sh14=request.POST.get("4sh1")
						sh24=request.POST.get("4sh2")
						test14=request.POST.get("4test1")
						test24=request.POST.get("4test2")
						work14=request.POST.get("4work1")
						work24=request.POST.get("4work2")
						#su204=request.POST.get("4su20")
						su304=request.POST.get("4su30")
						#su504=request.POST.get("4su50")
						
						shr1=((int(mo14)+int(sh14)+int(test14)+int(work14))/5)
						s14=int(shr1/2)
						shr2=((int(mo24)+int(sh24)+int(test24)+int(work24))/5)
						s24=int(shr2/2)
						su204=s14+s24
						su504=int(su304)+s14+s24
						
						db1=sqlite3.connect(yearnow+'.db')
						db1.row_factory=sqlite3.Row
						db1.execute("update readeat set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}',namero='{}', namst='{}' where namst='{}' and namero='{}'".format(mo14,mo24,sh14,sh24,test14,test24,work14,work24,s14,s24,su204,su304,su504,nru1,nsu1,nsu,nru))
						db1.commit()
					if 'alom' in p1:
						mo15=request.POST.get("5mo1")
						mo25=request.POST.get("5mo2")
						#s15=request.POST.get("5s1")
						#s25=request.POST.get("5s2")
						sh15=request.POST.get("5sh1")
						sh25=request.POST.get("5sh2")
						test15=request.POST.get("5test1")
						test25=request.POST.get("5test2")
						work15=request.POST.get("5work1")
						work25=request.POST.get("5work2")
						#su205=request.POST.get("5su20")
						su305=request.POST.get("5su30")
						#su505=request.POST.get("5su50")
						
						shr1=((int(mo15)+int(sh15)+int(test15)+int(work15))/5)
						s15=int(shr1/2)
						shr2=((int(mo25)+int(sh25)+int(test25)+int(work25))/5)
						s25=int(shr2/2)
						su205=s15+s25
						su505=int(su305)+s15+s25
						
						
						db1=sqlite3.connect(yearnow+'.db')
						db1.row_factory=sqlite3.Row
						db1.execute("update alom set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}',namero='{}', namst='{}' where namst='{}' and namero='{}'".format(mo15,mo25,sh15,sh25,test15,test25,work15,work25,s15,s25,su205,su305,su505,nru1,nsu1,nsu,nru))
						db1.commit()
					if 'ajtm' in p1:
						mo16=request.POST.get("6mo1")
						mo26=request.POST.get("6mo2")
						#s16=request.POST.get("6s1")
						#s26=request.POST.get("6s2")
						sh16=request.POST.get("6sh1")
						sh26=request.POST.get("6sh2")
						test16=request.POST.get("6test1")
						test26=request.POST.get("6test2")
						work16=request.POST.get("6work1")
						work26=request.POST.get("6work2")
						#su206=request.POST.get("6su20")
						su306=request.POST.get("6su30")
						#su506=request.POST.get("6su50")
						shr1=((int(mo16)+int(sh16)+int(test16)+int(work16))/5)
						s16=int(shr1/2)
						shr2=((int(mo26)+int(sh26)+int(test26)+int(work26))/5)
						s26=int(shr2/2)
						su206=s16+s26
						su506=int(su306)+s16+s26
						db1=sqlite3.connect(yearnow+'.db')
						db1.row_factory=sqlite3.Row
						db1.execute("update ajtm set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}',namero='{}', namst='{}' where namst='{}' and namero='{}'".format(mo16,mo26,sh16,sh26,test16,test26,work16,work26,s16,s26,su206,su306,su506,nru1,nsu1,nsu,nru))
						db1.commit()
					if 'english' in p1:
						mo17=request.POST.get("7mo1")
						mo27=request.POST.get("7mo2")
						#s17=request.POST.get("7s1")
						#s27=request.POST.get("7s2")
						sh17=request.POST.get("7sh1")
						sh27=request.POST.get("7sh2")
						test17=request.POST.get("7test1")
						test27=request.POST.get("7test2")
						work17=request.POST.get("7work1")
						work27=request.POST.get("7work2")
						#su207=request.POST.get("7su20")
						su307=request.POST.get("7su30")
						#su507=request.POST.get("7su50")
						shr1=((int(mo17)+int(sh17)+int(test17)+int(work17))/5)
						s17=int(shr1/2)
						shr2=((int(mo27)+int(sh27)+int(test27)+int(work27))/5)
						s27=int(shr2/2)
						su207=s17+s27
						su507=int(su307)+s17+s27
						db1=sqlite3.connect(yearnow+'.db')
						db1.row_factory=sqlite3.Row
						db1.execute("update english set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}',namero='{}', namst='{}' where namst='{}' and namero='{}'".format(mo17,mo27,sh17,sh27,test17,test27,work17,work27,s17,s27,su207,su307,su507,nru1,nsu1,nsu,nru))
						db1.commit()
						
		else:####################################################term two
			if 'A' in y:
				
				nru1=request.POST.get("nru")
				nsu1=request.POST.get("nsu")
				nru=request.POST.get("nrs")
				nsu=request.POST.get("nss")
				mo1=request.POST.get("1mo1")
				mo2=request.POST.get("1mo2")
				#ss1=request.POST.get("1s1")
				#ss2=request.POST.get("1s2")
				sh1=request.POST.get("1sh1")
				sh2=request.POST.get("1sh2")
				test1=request.POST.get("1test1")
				test2=request.POST.get("1test2")
				work1=request.POST.get("1work1")
				work2=request.POST.get("1work2")
				#su20=request.POST.get("1su20")
				su30=request.POST.get("1su30")
				#sut50=request.POST.get("1su50")
				shr1=((int(mo1)+int(sh1)+int(test1)+int(work1))/5)
				s1=int(shr1/2)
				shr2=((int(mo2)+int(sh2)+int(test2)+int(work2))/5)
				s2=int(shr2/2)
				su20=s1+s2
				su50=int(su30)+s1+s2
				
				db1=sqlite3.connect(yearnow+'.db')
				db1.row_factory=sqlite3.Row
				db1.execute("update tabladdstudynt2 set rowst='{}', namst='{}' where namst='{}' and rowst='{}'".format(nru1,nsu1,nsu,nru))
				
				db1.execute("update qran2 set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}',namero='{}', namst='{}' where namst='{}' and namero='{}'".format(mo1,mo2,sh1,sh2,test1,test2,work1,work2,s1,s2,su20,su30,su50,nru1,nsu1,nsu,nru))
				db1.commit()
		################################################################aslm
				mo12=request.POST.get("2mo1")
				mo22=request.POST.get("2mo2")
				#s12=request.POST.get("2s1")
				#s22=request.POST.get("2s2")
				sh12=request.POST.get("2sh1")
				sh22=request.POST.get("2sh2")
				test12=request.POST.get("2test1")
				test22=request.POST.get("2test2")
				work12=request.POST.get("2work1")
				work22=request.POST.get("2work2")
				#su202=request.POST.get("2su20")
				su302=request.POST.get("2su30")
				#su502=request.POST.get("2su50")
				
				shr1=((int(mo12)+int(sh12)+int(test12)+int(work12))/5)
				s12=int(shr1/2)
				shr2=((int(mo22)+int(sh22)+int(test22)+int(work22))/5)
				s22=int(shr2/2)
				su202=s12+s22
				su502=int(su302)+s12+s22
				
				db1=sqlite3.connect(yearnow+'.db')
				db1.row_factory=sqlite3.Row
				db1.execute("update aslm2 set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}',namero='{}', namst='{}' where namst='{}' and namero='{}'".format(mo12,mo22,sh12,sh22,test12,test22,work12,work22,s12,s22,su202,su302,su502,nru1,nsu1,nsu,nru))
				db1.commit()
		################################################################arbic
				mo13=request.POST.get("3mo1")
				mo23=request.POST.get("3mo2")
				#s13=request.POST.get("3s1")
				#s23=request.POST.get("3s2")
				sh13=request.POST.get("3sh1")
				sh23=request.POST.get("3sh2")
				test13=request.POST.get("3test1")
				test23=request.POST.get("3test2")
				work13=request.POST.get("3work1")
				work23=request.POST.get("3work2")
				#su203=request.POST.get("3su20")
				su303=request.POST.get("3su30")
				#su503=request.POST.get("3su50")
				
				shr1=((int(mo13)+int(sh13)+int(test13)+int(work13))/5)
				s13=int(shr1/2)
				shr2=((int(mo23)+int(sh23)+int(test23)+int(work23))/5)
				s23=int(shr2/2)
				su203=s13+s23
				su503=int(su303)+s13+s23
				
				db1=sqlite3.connect(yearnow+'.db')
				db1.row_factory=sqlite3.Row
				db1.execute("update arbic2 set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}',namero='{}', namst='{}' where namst='{}' and namero='{}'".format(mo13,mo23,sh13,sh23,test13,test23,work13,work23,s13,s23,su203,su303,su503,nru1,nsu1,nsu,nru))
				db1.commit()
				################################################################redeat
				mo14=request.POST.get("4mo1")
				mo24=request.POST.get("4mo2")
				#s14=request.POST.get("4s1")
				#s24=request.POST.get("4s2")
				sh14=request.POST.get("4sh1")
				sh24=request.POST.get("4sh2")
				test14=request.POST.get("4test1")
				test24=request.POST.get("4test2")
				work14=request.POST.get("4work1")
				work24=request.POST.get("4work2")
				#su204=request.POST.get("4su20")
				su304=request.POST.get("4su30")
				#su504=request.POST.get("4su50")
				
				shr1=((int(mo14)+int(sh14)+int(test14)+int(work14))/5)
				s14=int(shr1/2)
				shr2=((int(mo24)+int(sh24)+int(test24)+int(work24))/5)
				s24=int(shr2/2)
				su204=s14+s24
				su504=int(su304)+s14+s24
				
				db1=sqlite3.connect(yearnow+'.db')
				db1.row_factory=sqlite3.Row
				db1.execute("update readeat2 set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}',namero='{}', namst='{}' where namst='{}' and namero='{}'".format(mo14,mo24,sh14,sh24,test14,test24,work14,work24,s14,s24,su204,su304,su504,nru1,nsu1,nsu,nru))
				db1.commit()
				################################################################alom
				mo15=request.POST.get("5mo1")
				mo25=request.POST.get("5mo2")
				#s15=request.POST.get("5s1")
				#s25=request.POST.get("5s2")
				sh15=request.POST.get("5sh1")
				sh25=request.POST.get("5sh2")
				test15=request.POST.get("5test1")
				test25=request.POST.get("5test2")
				work15=request.POST.get("5work1")
				work25=request.POST.get("5work2")
				#su205=request.POST.get("5su20")
				su305=request.POST.get("5su30")
				#su505=request.POST.get("5su50")
				
				shr1=((int(mo15)+int(sh15)+int(test15)+int(work15))/5)
				s15=int(shr1/2)
				shr2=((int(mo25)+int(sh25)+int(test25)+int(work25))/5)
				s25=int(shr2/2)
				su205=s15+s25
				su505=int(su305)+s15+s25
				
				
				db1=sqlite3.connect(yearnow+'.db')
				db1.row_factory=sqlite3.Row
				db1.execute("update alom2 set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}',namero='{}', namst='{}' where namst='{}' and namero='{}'".format(mo15,mo25,sh15,sh25,test15,test25,work15,work25,s15,s25,su205,su305,su505,nru1,nsu1,nsu,nru))
				db1.commit()
				################################################################ajtmaet
				if int(nru[-2])>=3:
					mo16=request.POST.get("6mo1")
					mo26=request.POST.get("6mo2")
					#s16=request.POST.get("6s1")
					#s26=request.POST.get("6s2")
					sh16=request.POST.get("6sh1")
					sh26=request.POST.get("6sh2")
					test16=request.POST.get("6test1")
					test26=request.POST.get("6test2")
					work16=request.POST.get("6work1")
					work26=request.POST.get("6work2")
					#su206=request.POST.get("6su20")
					su306=request.POST.get("6su30")
					#su506=request.POST.get("6su50")
					
					shr1=((int(mo16)+int(sh16)+int(test16)+int(work16))/5)
					s16=int(shr1/2)
					shr2=((int(mo26)+int(sh26)+int(test26)+int(work26))/5)
					s26=int(shr2/2)
					su206=s16+s26
					su506=int(su306)+s16+s26
					
					
					db1=sqlite3.connect(yearnow+'.db')
					db1.row_factory=sqlite3.Row
					db1.execute("update ajtm2 set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}',namero='{}', namst='{}' where namst='{}' and namero='{}'".format(mo16,mo26,sh16,sh26,test16,test26,work16,work26,s16,s26,su206,su306,su506,nru1,nsu1,nsu,nru))
					db1.commit()
				
				################################################################english
				if int(nru[-2])>=7:
					mo17=request.POST.get("7mo1")
					mo27=request.POST.get("7mo2")
					#s17=request.POST.get("7s1")
					#s27=request.POST.get("7s2")
					sh17=request.POST.get("7sh1")
					sh27=request.POST.get("7sh2")
					test17=request.POST.get("7test1")
					test27=request.POST.get("7test2")
					work17=request.POST.get("7work1")
					work27=request.POST.get("7work2")
					#su207=request.POST.get("7su20")
					su307=request.POST.get("7su30")
					#su507=request.POST.get("7su50")
					
					shr1=((int(mo17)+int(sh17)+int(test17)+int(work17))/5)
					s17=int(shr1/2)
					shr2=((int(mo27)+int(sh27)+int(test27)+int(work27))/5)
					s27=int(shr2/2)
					su207=s17+s27
					su507=int(su307)+s17+s27
					
					db1=sqlite3.connect(yearnow+'.db')
					db1.row_factory=sqlite3.Row
					db1.execute("update english2 set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}',namero='{}', namst='{}' where namst='{}' and namero='{}'".format(mo17,mo27,sh17,sh27,test17,test27,work17,work27,s17,s27,su207,su307,su507,nru1,nsu1,nsu,nru))
					db1.commit()
			else:
					p1=[]
					for u in f:
						p1.append(u.namemtral)
					if 'qran' in p1:###############qran
						nru1=request.POST.get("nru")
						nsu1=request.POST.get("nsu")
						nru=request.POST.get("nrs")
						nsu=request.POST.get("nss")
						mo1=request.POST.get("1mo1")
						mo2=request.POST.get("1mo2")
						#ss1=request.POST.get("1s1")
						#ss2=request.POST.get("1s2")
						sh1=request.POST.get("1sh1")
						sh2=request.POST.get("1sh2")
						test1=request.POST.get("1test1")
						test2=request.POST.get("1test2")
						work1=request.POST.get("1work1")
						work2=request.POST.get("1work2")
						#su20=request.POST.get("1su20")
						su30=request.POST.get("1su30")
						#sut50=request.POST.get("1su50")
						shr1=((int(mo1)+int(sh1)+int(test1)+int(work1))/5)
						s1=int(shr1/2)
						shr2=((int(mo2)+int(sh2)+int(test2)+int(work2))/5)
						s2=int(shr2/2)
						su20=s1+s2
						su50=int(su30)+s1+s2
						
						db1=sqlite3.connect(yearnow+'.db')
						db1.row_factory=sqlite3.Row
						db1.execute("update tabladdstudynt2 set rowst='{}', namst='{}' where namst='{}' and rowst='{}'".format(nru1,nsu1,nsu,nru))
						
						db1.execute("update qran2 set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}',namero='{}', namst='{}' where namst='{}' and namero='{}'".format(mo1,mo2,sh1,sh2,test1,test2,work1,work2,s1,s2,su20,su30,su50,nru1,nsu1,nsu,nru))
						db1.commit()
					if 'aslm' in p1:##############################aslm
						mo12=request.POST.get("2mo1")
						mo22=request.POST.get("2mo2")
						#s12=request.POST.get("2s1")
						#s22=request.POST.get("2s2")
						sh12=request.POST.get("2sh1")
						sh22=request.POST.get("2sh2")
						test12=request.POST.get("2test1")
						test22=request.POST.get("2test2")
						work12=request.POST.get("2work1")
						work22=request.POST.get("2work2")
						#su202=request.POST.get("2su20")
						su302=request.POST.get("2su30")
						#su502=request.POST.get("2su50")
						
						shr1=((int(mo12)+int(sh12)+int(test12)+int(work12))/5)
						s12=int(shr1/2)
						shr2=((int(mo22)+int(sh22)+int(test22)+int(work22))/5)
						s22=int(shr2/2)
						su202=s12+s22
						su502=int(su302)+s12+s22
						
						db1=sqlite3.connect(yearnow+'.db')
						db1.row_factory=sqlite3.Row
						db1.execute("update aslm2 set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}',namero='{}', namst='{}' where namst='{}' and namero='{}'".format(mo12,mo22,sh12,sh22,test12,test22,work12,work22,s12,s22,su202,su302,su502,nru1,nsu1,nsu,nru))
						db1.commit()
					if 'arbic' in p1:
						mo13=request.POST.get("3mo1")
						mo23=request.POST.get("3mo2")
						#s13=request.POST.get("3s1")
						#s23=request.POST.get("3s2")
						sh13=request.POST.get("3sh1")
						sh23=request.POST.get("3sh2")
						test13=request.POST.get("3test1")
						test23=request.POST.get("3test2")
						work13=request.POST.get("3work1")
						work23=request.POST.get("3work2")
						#su203=request.POST.get("3su20")
						su303=request.POST.get("3su30")
						#su503=request.POST.get("3su50")
						
						shr1=((int(mo13)+int(sh13)+int(test13)+int(work13))/5)
						s13=int(shr1/2)
						shr2=((int(mo23)+int(sh23)+int(test23)+int(work23))/5)
						s23=int(shr2/2)
						su203=s13+s23
						su503=int(su303)+s13+s23
						
						db1=sqlite3.connect(yearnow+'.db')
						db1.row_factory=sqlite3.Row
						db1.execute("update arbic2 set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}',namero='{}', namst='{}' where namst='{}' and namero='{}'".format(mo13,mo23,sh13,sh23,test13,test23,work13,work23,s13,s23,su203,su303,su503,nru1,nsu1,nsu,nru))
						db1.commit()
					if 'readeat' in p1:
						mo14=request.POST.get("4mo1")
						mo24=request.POST.get("4mo2")
						#s14=request.POST.get("4s1")
						#s24=request.POST.get("4s2")
						sh14=request.POST.get("4sh1")
						sh24=request.POST.get("4sh2")
						test14=request.POST.get("4test1")
						test24=request.POST.get("4test2")
						work14=request.POST.get("4work1")
						work24=request.POST.get("4work2")
						#su204=request.POST.get("4su20")
						su304=request.POST.get("4su30")
						#su504=request.POST.get("4su50")
						
						shr1=((int(mo14)+int(sh14)+int(test14)+int(work14))/5)
						s14=int(shr1/2)
						shr2=((int(mo24)+int(sh24)+int(test24)+int(work24))/5)
						s24=int(shr2/2)
						su204=s14+s24
						su504=int(su304)+s14+s24
						
						db1=sqlite3.connect(yearnow+'.db')
						db1.row_factory=sqlite3.Row
						db1.execute("update readeat2 set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}',namero='{}', namst='{}' where namst='{}' and namero='{}'".format(mo14,mo24,sh14,sh24,test14,test24,work14,work24,s14,s24,su204,su304,su504,nru1,nsu1,nsu,nru))
						db1.commit()
					if 'alom' in p1:
						mo15=request.POST.get("5mo1")
						mo25=request.POST.get("5mo2")
						#s15=request.POST.get("5s1")
						#s25=request.POST.get("5s2")
						sh15=request.POST.get("5sh1")
						sh25=request.POST.get("5sh2")
						test15=request.POST.get("5test1")
						test25=request.POST.get("5test2")
						work15=request.POST.get("5work1")
						work25=request.POST.get("5work2")
						#su205=request.POST.get("5su20")
						su305=request.POST.get("5su30")
						#su505=request.POST.get("5su50")
						
						shr1=((int(mo15)+int(sh15)+int(test15)+int(work15))/5)
						s15=int(shr1/2)
						shr2=((int(mo25)+int(sh25)+int(test25)+int(work25))/5)
						s25=int(shr2/2)
						su205=s15+s25
						su505=int(su305)+s15+s25
						
						
						db1=sqlite3.connect(yearnow+'.db')
						db1.row_factory=sqlite3.Row
						db1.execute("update alom2 set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}',namero='{}', namst='{}' where namst='{}' and namero='{}'".format(mo15,mo25,sh15,sh25,test15,test25,work15,work25,s15,s25,su205,su305,su505,nru1,nsu1,nsu,nru))
						db1.commit()
					if 'ajtm' in p1:
						mo16=request.POST.get("6mo1")
						mo26=request.POST.get("6mo2")
						#s16=request.POST.get("6s1")
						#s26=request.POST.get("6s2")
						sh16=request.POST.get("6sh1")
						sh26=request.POST.get("6sh2")
						test16=request.POST.get("6test1")
						test26=request.POST.get("6test2")
						work16=request.POST.get("6work1")
						work26=request.POST.get("6work2")
						#su206=request.POST.get("6su20")
						su306=request.POST.get("6su30")
						#su506=request.POST.get("6su50")
						shr1=((int(mo16)+int(sh16)+int(test16)+int(work16))/5)
						s16=int(shr1/2)
						shr2=((int(mo26)+int(sh26)+int(test26)+int(work26))/5)
						s26=int(shr2/2)
						su206=s16+s26
						su506=int(su306)+s16+s26
						db1=sqlite3.connect(yearnow+'.db')
						db1.row_factory=sqlite3.Row
						db1.execute("update ajtm2 set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}',namero='{}', namst='{}' where namst='{}' and namero='{}'".format(mo16,mo26,sh16,sh26,test16,test26,work16,work26,s16,s26,su206,su306,su506,nru1,nsu1,nsu,nru))
						db1.commit()
					if 'english' in p1:
						mo17=request.POST.get("7mo1")
						mo27=request.POST.get("7mo2")
						#s17=request.POST.get("7s1")
						#s27=request.POST.get("7s2")
						sh17=request.POST.get("7sh1")
						sh27=request.POST.get("7sh2")
						test17=request.POST.get("7test1")
						test27=request.POST.get("7test2")
						work17=request.POST.get("7work1")
						work27=request.POST.get("7work2")
						#su207=request.POST.get("7su20")
						su307=request.POST.get("7su30")
						#su507=request.POST.get("7su50")
						shr1=((int(mo17)+int(sh17)+int(test17)+int(work17))/5)
						s17=int(shr1/2)
						shr2=((int(mo27)+int(sh27)+int(test27)+int(work27))/5)
						s27=int(shr2/2)
						su207=s17+s27
						su507=int(su307)+s17+s27
						db1=sqlite3.connect(yearnow+'.db')
						db1.row_factory=sqlite3.Row
						db1.execute("update english2 set mo1='{}',mo2='{}',sh1='{}',sh2='{}',test1='{}',test2='{}',work1='{}',work2='{}',s1='{}',s2='{}',su20='{}',su30='{}',su50='{}',namero='{}', namst='{}' where namst='{}' and namero='{}'".format(mo17,mo27,sh17,sh27,test17,test27,work17,work27,s17,s27,su207,su307,su507,nru1,nsu1,nsu,nru))
						db1.commit()
						#######################################################################finshed term 2			
				
				
		messages.info(request,'complet update')
		return render(request,'sch/shost.html',{'yearnow':yearnow,'termnow':terms.objects.get(pk=1),'nameschool':nameschool.objects.get(pk=1)})
def shost5(request):
	if request.method=='POST':
		yt=terms.objects.get(pk=1)
		nr=request.POST.get("nr")
		db1=sqlite3.connect(yearnow+'.db')
		db1.row_factory=sqlite3.Row
		if yt.term=='الفصل الاول':
			
			ro1=db1.execute("select * from tabladdstudynt where rowst='{}'".format(nr))
		else:
			ro1=db1.execute("select * from tabladdstudynt2 where rowst='{}'".format(nr))
	return render(request,'sch/sc1.html',{'i':ro1,'u':'same','rn':nr,'yearnow':yearnow,'termnow':terms.objects.get(pk=1),'nameschool':nameschool.objects.get(pk=1)})
def shost6(request):
	if request.method=='POST':
		yt=terms.objects.get(pk=1)
		nr=request.POST.get("gn")
		if nr=='none'or nr=='':
			return render(request,'sch/sc1.html',{'yearnow':yearnow,'termnow':terms.objects.get(pk=1),'nameschool':nameschool.objects.get(pk=1)})
		db1=sqlite3.connect(yearnow+'.db')
		db1.row_factory=sqlite3.Row
		if yt.term=='الفصل الاول':
			
			ro1=db1.execute("select * from tabladdstudynt where namst='{}'".format(nr))
			for n in ro1:
				namrowstu=n['rowst']
			ro2=db1.execute("select * from qran where namst='{}'".format(nr))
			ro3=db1.execute("select * from aslm where namst='{}'".format(nr))
			ro4=db1.execute("select * from arbic where namst='{}'".format(nr))
			ro5=db1.execute("select * from readeat where namst='{}'".format(nr))
			ro6=db1.execute("select * from alom where namst='{}'".format(nr))
			if int(namrowstu[-2])>=3:
				ro7=db1.execute("select * from ajtm where namst='{}'".format(nr))
			else:ro7=''
			if int(namrowstu[-2])>=7:
				
				ro8=db1.execute("select * from english where namst='{}'".format(nr))
			else:ro8=''
		else:
			ro1=db1.execute("select * from tabladdstudynt2 where namst='{}'".format(nr))
			for n in ro1:
				namrowstu=n['rowst']
			ro2=db1.execute("select * from qran2 where namst='{}'".format(nr))
			ro3=db1.execute("select * from aslm2 where namst='{}'".format(nr))
			ro4=db1.execute("select * from arbic2 where namst='{}'".format(nr))
			ro5=db1.execute("select * from readeat2 where namst='{}'".format(nr))
			ro6=db1.execute("select * from alom2 where namst='{}'".format(nr))
			if int(namrowstu[-2])>=3:
				ro7=db1.execute("select * from ajtm2 where namst='{}'".format(nr))
			else:ro7=''
			if int(namrowstu[-2])>=7:
				
				ro8=db1.execute("select * from english2 where namst='{}'".format(nr))
			else:ro8=''
		
	return render(request,'sch/sc1.html',{'ii':ro2,'ii2':ro3,'ii3':ro4,'ii4':ro5,'ii5':ro6,'ii6':ro7,'ii7':ro8,'rn':nr,'nst':namrowstu,'yearnow':yearnow,'termnow':terms.objects.get(pk=1),'nameschool':nameschool.objects.get(pk=1)})
def login1(request):
	if request.method=='POST':
		emal=request.POST.get("gmail1")
		pas=request.POST.get("p2")
		if emal=='' or pas=='':
			messages.info(request,"خطا في تسجيل الدخول")
			return redirect("/")
		user = authenticate(request, username=emal, password=pas)
		if user is not None:
			login(request, user)
			messages.info(request,"تم تسجيل الدخول")
			return redirect("/")
		else:
			messages.info(request,"خطاء في كلمة المرور او اسم المستخدم")
			return redirect("/")
def logout1(request):
	
	logout(request)
	messages.info(request,"تم تسجبل الخروج")
	return redirect("/")
def setting1(request):##################################################setinggggggggsssssssssssssssssssss
	db1=sqlite3.connect(yearnow+'.db')
	db1.row_factory=sqlite3.Row
	ro1=db1.execute("select * from tabladdrow")
	if request.method=='POST':
		choos=request.POST.get("cho")
		terms.objects.filter(pk=1).update(term=choos)
		
	return render(request,'sch/sett1.html',{'rown':ro1,'set':terms.objects.all(),'set2':nameschool.objects.get(pk=1),'yearnow':yearnow,'termnow':terms.objects.get(pk=1),'nameschool':nameschool.objects.get(pk=1)})
def setting2(request):
	if request.method=='POST':
		choos=request.POST.get("newn")
		nameschool.objects.filter(pk=1).update(name=choos)
	return redirect("setting1")
def setting3(request):
	p1=[]
	nm=[]
	m=[]
	db1=sqlite3.connect(yearnow+'.db')
	db1.row_factory=sqlite3.Row
	ro1=db1.execute("select * from tabladdstudynt2")
	for n in ro1:
		p1.append(n['namst'])
	ro2=db1.execute("select * from tabladdstudynt")
	for g in ro2:
		if g['namst'] in p1:
			m.append(g['namst'])
		else:
			nm.append(g['namst'])
			namestudy=g['namst']
			namrowstu=g['rowst']
			db1.execute('create table if not exists tabladdstudynt2(ID integer primary Key autoincrement,namst text,rowst text)')
			db1.execute('''insert into tabladdstudynt2(namst,rowst) values(?,?)''',(g['namst'],g['rowst']))
			db1.commit()
			db1.execute('create table if not exists qran2(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
			db1.execute('''insert into qran2(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
			db1.commit()
			db1.execute('create table if not exists aslm2(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
			db1.execute('''insert into aslm2(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
			db1.commit()
			db1.execute('create table if not exists arbic2(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
			db1.execute('''insert into arbic2(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
			db1.commit()
			db1.execute('create table if not exists readeat2(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
			db1.execute('''insert into readeat2(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
			db1.commit()
			db1.execute('create table if not exists alom2(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
			db1.execute('''insert into alom2(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
			db1.commit()
			if int(namrowstu[-2])>=3:
				
				db1.execute('create table if not exists ajtm2(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
				db1.execute('''insert into ajtm2(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
				db1.commit()
			if int(namrowstu[-2])>=7:
				
				db1.execute('create table if not exists english2(ID integer primary Key autoincrement,namst text,namero text,mo1 text,work1 text,sh1 text,test1 text,mo2 text,work2 text,sh2 text,test2 text,s1 text,s2 text,su20 text,su30 text,su50 text)')
				db1.execute('''insert into english2(namst,namero,mo1,work1,sh1,test1,mo2,work2,sh2,test2,s1,s2,su20,su30,su50) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(namestudy,namrowstu,"0","0","0","0","0","0","0","0","0","0","0","0","0"))
				db1.commit()
	messages.info(request,"تم نقل <{}> اسم--وعدد الاسما الموجودة هي<{}>".format(str(len(nm)),str(len(m))))
	return redirect('setting1')
def renrow(request):
	if request.method=='POST':
		rownew=request.POST.get("rerow")
		rowname=request.POST.get("rownow")
		#if rowname[-1]=='1':
		if len(rownew)<5:
			messages.info(request,'خطاء في كتابة اسم الصف الرجاء اعادة الاسم مرة اخرى حسب معايير البرنامج')
			return redirect('setting1')
		try:
			
				
			if rownew[0:4]==rowname[0:4] and type(int(rownew[-1:]))==int:	
				db1=sqlite3.connect(yearnow+'.db')
				db1.row_factory=sqlite3.Row
				db1.execute("update tabladdrow set roww='{}' where roww='{}'".format(rownew,rowname))
				db1.commit()
				db1.execute("update tabladdstudynt set rowst='{}' where rowst='{}'".format(rownew,rowname))
				db1.commit()
				db1.execute("update tabladdstudynt2 set rowst='{}' where rowst='{}'".format(rownew,rowname))
				db1.commit()
				db1.execute("update qran set namero='{}' where namero='{}'".format(rownew,rowname))#term one
				db1.commit()
				db1.execute("update aslm set namero='{}' where namero='{}'".format(rownew,rowname))
				db1.commit()
				db1.execute("update arbic set namero='{}' where namero='{}'".format(rownew,rowname))
				db1.commit()
				db1.execute("update readeat set namero='{}' where namero='{}'".format(rownew,rowname))
				db1.commit()
				db1.execute("update alom set namero='{}' where namero='{}'".format(rownew,rowname))
				db1.commit()
				db1.execute("update ajtm set namero='{}' where namero='{}'".format(rownew,rowname))
				db1.commit()
				db1.execute("update english set namero='{}' where namero='{}'".format(rownew,rowname))
				db1.commit()
				####################################
				db1.execute("update qran2 set namero='{}' where namero='{}'".format(rownew,rowname))#term one
				db1.commit()
				db1.execute("update aslm2 set namero='{}' where namero='{}'".format(rownew,rowname))
				db1.commit()
				db1.execute("update arbic2 set namero='{}' where namero='{}'".format(rownew,rowname))
				db1.commit()
				db1.execute("update readeat2 set namero='{}' where namero='{}'".format(rownew,rowname))
				db1.commit()
				db1.execute("update alom2 set namero='{}' where namero='{}'".format(rownew,rowname))
				db1.commit()
				db1.execute("update ajtm2 set namero='{}' where namero='{}'".format(rownew,rowname))
				db1.commit()
				db1.execute("update english2 set namero='{}' where namero='{}'".format(rownew,rowname))
				db1.commit()
				Tmt.objects.filter(namerow=rowname).update(namerow=rownew)
				messages.info(request,'تم التعديل بنجاح')
			else:
				messages.info(request,'خطاء في كتابة اسم الصف الرجاء اعادة الاسم مرة اخرى حسب معايير البرنامج')
		except:
			messages.info(request,'خطاء في كتابة اسم الصف الرجاء اعادة الاسم مرة اخرى حسب معايير البرنامج')
			
		
	return redirect('setting1')
####function product helf and full years

def shomark(request):
	yt=terms.objects.get(pk=1)
	nr=request.POST.get("nr")
	db1=sqlite3.connect(yearnow+'.db')
	db1.row_factory=sqlite3.Row
	ro1=db1.execute("select * from tabladdrow")
	#if yt.term=='الفصل الاول':
	return render(request,'sch/shomarks.html',{'g':ro1,'set2':nameschool.objects.get(pk=1),'yearnow':yearnow,'termnow':terms.objects.get(pk=1),'nameschool':nameschool.objects.get(pk=1)})
def shoprod_helf(request):
	if request.method=='POST':
		yt=terms.objects.get(pk=1)
		nr=request.POST.get("nr")
		db1=sqlite3.connect(yearnow+'.db')
		db1.row_factory=sqlite3.Row
		if yt.term=='الفصل الاول':
			ro1=db1.execute("select * from tabladdstudynt where rowst='{}'".format(nr))
			ro2=db1.execute("select * from tabladdrow")
		else:
			ro2=db1.execute("select * from tabladdrow")
			ro1=db1.execute("select * from tabladdstudynt2 where rowst='{}'".format(nr))
	return render(request,'sch/shomarks.html',{'i':ro1,'u':'same','rn':nr,'g':ro2,'set2':nameschool.objects.get(pk=1),'yearnow':yearnow,'termnow':terms.objects.get(pk=1),'nameschool':nameschool.objects.get(pk=1)})			
def shoprod_helf2(request):
	stn=[]
	if request.method=='POST':
		yt=terms.objects.get(pk=1)
		nr=request.POST.get("gn")
		db1=sqlite3.connect(yearnow+'.db')
		db1.row_factory=sqlite3.Row
		if yt.term=='الفصل الاول':
			
			ro1=db1.execute("select * from tabladdstudynt where namst='{}'".format(nr))
			for n in ro1:
				namrowstu=n['rowst']
			ro2=db1.execute("select * from qran where namst='{}'".format(nr))
			ro3=db1.execute("select * from aslm where namst='{}'".format(nr))
			ro4=db1.execute("select * from arbic where namst='{}'".format(nr))
			ro5=db1.execute("select * from readeat where namst='{}'".format(nr))
			ro6=db1.execute("select * from alom where namst='{}'".format(nr))
			if int(namrowstu[-2])>=3:
				ro7=db1.execute("select * from ajtm where namst='{}'".format(nr))
			else:ro7=''
			if int(namrowstu[-2])>=7:
				
				ro8=db1.execute("select * from english where namst='{}'".format(nr))
			else:ro8=''
			return render(request,'sch/shomarks.html',{'ii':ro2,"v":"10",'ii2':ro3,'ii3':ro4,'ii4':ro5,'ii5':ro6,'ii6':ro7,'ii7':ro8,'rn':nr,'nst':namrowstu,'yearnow':yearnow,'termnow':terms.objects.get(pk=1),'nameschool':nameschool.objects.get(pk=1)})
		else:
			ro1=db1.execute("select * from tabladdstudynt where namst='{}'".format(nr))
			for n in ro1:
				namrowstu=n['rowst']
			db1.execute("create table if not exists termtwoqran(ID integer primary Key autoincrement,namst text,namero text,fs20 text,fs30 text,fs50 text,ss20 text,ss30 text,ss50 text,su100 text)")
			db1.execute("create table if not exists termtwoaslm(ID integer primary Key autoincrement,namst text,namero text,fs20 text,fs30 text,fs50 text,ss20 text,ss30 text,ss50 text,su100 text)")
			db1.execute("create table if not exists termtwoarbic(ID integer primary Key autoincrement,namst text,namero text,fs20 text,fs30 text,fs50 text,ss20 text,ss30 text,ss50 text,su100 text)")
			db1.execute("create table if not exists termtworeadeat(ID integer primary Key autoincrement,namst text,namero text,fs20 text,fs30 text,fs50 text,ss20 text,ss30 text,ss50 text,su100 text)")
			db1.execute("create table if not exists termtwoalom(ID integer primary Key autoincrement,namst text,namero text,fs20 text,fs30 text,fs50 text,ss20 text,ss30 text,ss50 text,su100 text)")
			db1.execute("create table if not exists termtwoajtm(ID integer primary Key autoincrement,namst text,namero text,fs20 text,fs30 text,fs50 text,ss20 text,ss30 text,ss50 text,su100 text)")
			db1.execute("create table if not exists termtwoenglish(ID integer primary Key autoincrement,namst text,namero text,fs20 text,fs30 text,fs50 text,ss20 text,ss30 text,ss50 text,su100 text)")
			
			chk=db1.execute("select namst from termtwoqran")
			for f in chk:
				stn.append(f["namst"])
			if nr in stn:#chik if name study is found in table_product
				
				db1=sqlite3.connect(yearnow+'.db')
				cb=db1.cursor()
				cb.execute("select * from qran where namst='{}'union all select * from qran2  where namst='{}'".format(nr,nr))
				df1=cb.fetchall()
				cb.execute("select * from aslm where namst='{}'union all select * from aslm2  where namst='{}'".format(nr,nr))
				df2=cb.fetchall()
				cb.execute("select * from arbic where namst='{}'union all select * from arbic2  where namst='{}'".format(nr,nr))
				df3=cb.fetchall()
				cb.execute("select * from readeat where namst='{}'union all select * from readeat2  where namst='{}'".format(nr,nr))
				df4=cb.fetchall()
				cb.execute("select * from alom where namst='{}'union all select * from alom2  where namst='{}'".format(nr,nr))
				df5=cb.fetchall()
				if int(namrowstu[-2])>=3:#chik if row big 3
					ll=1
					cb.execute("select * from ajtm where namst='{}'union all select * from ajtm2  where namst='{}'".format(nr,nr))
					df6=cb.fetchall()
					for n6 in df6:
						if ll==1:
							yu6=n6[15]
							db1.execute("update termtwoajtm set fs20='{}',fs30='{}',fs50='{}' where namst='{}'".format(n6[13],n6[14],n6[15],nr))
							db1.commit()
						if ll==2:
							rt6=int(yu6)+int(n6[15])
							db1.execute("update termtwoajtm set ss20='{}',ss30='{}',ss50='{}',su100='{}' where namst='{}'".format(n6[13],n6[14],n6[15],str(rt6),nr))
							db1.commit()
						ll+=1	
				if int(namrowstu[-2])>=7:#chik if row big 7
					ll=1
					cb.execute("select * from english where namst='{}'union all select * from english2  where namst='{}'".format(nr,nr))
					df7=cb.fetchall()
					for n7 in df7:
						if ll==1:
							yu7=n7[15]
							db1.execute("update termtwoenglish set fs20='{}',fs30='{}',fs50='{}' where namst='{}'".format(n7[13],n7[14],n7[15],nr))
							db1.commit()
						if ll==2:
							rt7=int(yu7)+int(n7[15])
							db1.execute("update termtwoenglish set ss20='{}',ss30='{}',ss50='{}',su100='{}' where namst='{}'".format(n7[13],n7[14],n7[15],str(rt7),nr))
							db1.commit()
						ll+=1
						
				ll=1
				for n1,n2,n3,n4,n5 in zip(df1,df2,df3,df4,df5):
					if ll==1:
						yu1,yu2,yu3,yu4,yu5=n1[15],n2[15],n3[15],n4[15],n5[15]
						db1.execute("update termtwoqran set fs20='{}',fs30='{}',fs50='{}' where namst='{}'".format(n1[13],n1[14],n1[15],nr))
						
						db1.execute("update termtwoaslm set fs20='{}',fs30='{}',fs50='{}' where namst='{}'".format(n2[13],n2[14],n2[15],nr))
						db1.execute("update termtwoarbic set fs20='{}',fs30='{}',fs50='{}' where namst='{}'".format(n3[13],n3[14],n3[15],nr))
						db1.execute("update termtworeadeat set fs20='{}',fs30='{}',fs50='{}' where namst='{}'".format(n4[13],n4[14],n4[15],nr))
						db1.execute("update termtwoalom set fs20='{}',fs30='{}',fs50='{}' where namst='{}'".format(n5[13],n5[14],n5[15],nr))
						db1.commit()
					if ll==2:
						rt1=int(n1[15])+int(yu1)
						rt2=int(n2[15])+int(yu2)
						rt3=int(n3[15])+int(yu3)
						rt4=int(n4[15])+int(yu4)
						rt5=int(n5[15])+int(yu5)
						
						db1.execute("update termtwoqran set ss20='{}',ss30='{}',ss50='{}',su100='{}' where namst='{}'".format(n1[13],n1[14],n1[15],str(rt1),nr))
						db1.execute("update termtwoaslm set ss20='{}',ss30='{}',ss50='{}',su100='{}' where namst='{}'".format(n2[13],n2[14],n2[15],str(rt2),nr))
						db1.execute("update termtwoarbic set ss20='{}',ss30='{}',ss50='{}',su100='{}' where namst='{}'".format(n3[13],n3[14],n3[15],str(rt3),nr))
						db1.execute("update termtworeadeat set ss20='{}',ss30='{}',ss50='{}',su100='{}' where namst='{}'".format(n4[13],n4[14],n4[15],str(rt4),nr))
						db1.execute("update termtwoalom set ss20='{}',ss30='{}',ss50='{}',su100='{}' where namst='{}'".format(n5[13],n5[14],n5[15],str(rt5),nr))
						db1.commit()
					ll+=1
					
						
			else:#chik if name is not found in table product
				
				
				db1=sqlite3.connect("mngschool1.db")
				cb=db1.cursor()
				cb.execute("select * from qran where namst='{}'union all select * from qran2  where namst='{}'".format(nr,nr))
				df1=cb.fetchall()
				cb.execute("select * from aslm where namst='{}'union all select * from aslm2  where namst='{}'".format(nr,nr))
				df2=cb.fetchall()
				cb.execute("select * from arbic where namst='{}'union all select * from arbic2  where namst='{}'".format(nr,nr))
				df3=cb.fetchall()
				cb.execute("select * from readeat where namst='{}'union all select * from readeat2  where namst='{}'".format(nr,nr))
				df4=cb.fetchall()
				cb.execute("select * from alom where namst='{}'union all select * from alom2  where namst='{}'".format(nr,nr))
				df5=cb.fetchall()
				if int(namrowstu[-2])>=3:#chik if row big 3
					ll=1
					cb.execute("select * from ajtm where namst='{}'union all select * from ajtm2  where namst='{}'".format(nr,nr))
					df6=cb.fetchall()
					for n6 in df6:
						if ll==1:
							yu6=n6[15]
							db1.execute('''insert into termtwoajtm(namst,namero,fs20,fs30,fs50,ss20,ss30,ss50,su100) values(?,?,?,?,?,?,?,?,?)''',(nr,namrowstu,n6[13],n6[14],n6[15],"0","0","0","0"))
							db1.commit()
						if ll==2:
							rt6=int(yu6)+int(n6[15])
							db1.execute("update termtwoajtm set ss20='{}',ss30='{}',ss50='{}',su100='{}' where namst='{}'".format(n6[13],n6[14],n6[15],str(rt6),nr))
							db1.commit()
						ll+=1	
				if int(namrowstu[-2])>=7:#chik if row big 7
					ll=1
					cb.execute("select * from english where namst='{}'union all select * from english2  where namst='{}'".format(nr,nr))
					df7=cb.fetchall()
					for n7 in df7:
						if ll==1:
							yu7=n7[15]
							db1.execute('''insert into termtwoenglish(namst,namero,fs20,fs30,fs50,ss20,ss30,ss50,su100) values(?,?,?,?,?,?,?,?,?)''',(nr,namrowstu,n7[13],n7[14],n7[15],"0","0","0","0"))
							db1.commit()
						if ll==2:
							rt7=int(yu7)+int(n7[15])
							db1.execute("update termtwoenglish set ss20='{}',ss30='{}',ss50='{}',su100='{}' where namst='{}'".format(n7[13],n7[14],n7[15],str(rt7),nr))
							db1.commit()
						ll+=1
				ll=1
				for n1,n2,n3,n4,n5 in zip(df1,df2,df3,df4,df5):
					if ll==1:
						yu1,yu2,yu3,yu4,yu5=n1[15],n2[15],n3[15],n4[15],n5[15]
						db1.execute('''insert into termtwoqran(namst,namero,fs20,fs30,fs50,ss20,ss30,ss50,su100) values(?,?,?,?,?,?,?,?,?)''',(nr,namrowstu,n1[13],n1[14],n1[15],"0","0","0","0"))
						db1.execute('''insert into termtwoaslm(namst,namero,fs20,fs30,fs50,ss20,ss30,ss50,su100) values(?,?,?,?,?,?,?,?,?)''',(nr,namrowstu,n2[13],n2[14],n2[15],"0","0","0","0"))
						db1.execute('''insert into termtwoarbic(namst,namero,fs20,fs30,fs50,ss20,ss30,ss50,su100) values(?,?,?,?,?,?,?,?,?)''',(nr,namrowstu,n3[13],n3[14],n3[15],"0","0","0","0"))
						db1.execute('''insert into termtworeadeat(namst,namero,fs20,fs30,fs50,ss20,ss30,ss50,su100) values(?,?,?,?,?,?,?,?,?)''',(nr,namrowstu,n4[13],n4[14],n4[15],"0","0","0","0"))
						db1.execute('''insert into termtwoalom(namst,namero,fs20,fs30,fs50,ss20,ss30,ss50,su100) values(?,?,?,?,?,?,?,?,?)''',(nr,namrowstu,n5[13],n5[14],n5[15],"0","0","0","0"))
						db1.commit()
					if ll==2:
						rt1=int(n1[15])+int(yu1)
						rt2=int(n2[15])+int(yu2)
						rt3=int(n3[15])+int(yu3)
						rt4=int(n4[15])+int(yu4)
						rt5=int(n5[15])+int(yu5)
						
						db1.execute("update termtwoqran set ss20='{}',ss30='{}',ss50='{}',su100='{}' where namst='{}'".format(n1[13],n1[14],n1[15],str(rt1),nr))
						db1.execute("update termtwoaslm set ss20='{}',ss30='{}',ss50='{}',su100='{}' where namst='{}'".format(n2[13],n2[14],n2[15],str(rt2),nr))
						db1.execute("update termtwoarbic set ss20='{}',ss30='{}',ss50='{}',su100='{}' where namst='{}'".format(n3[13],n3[14],n3[15],str(rt3),nr))
						db1.execute("update termtworeadeat set ss20='{}',ss30='{}',ss50='{}',su100='{}' where namst='{}'".format(n4[13],n4[14],n4[15],str(rt4),nr))
						db1.execute("update termtwoalom set ss20='{}',ss30='{}',ss50='{}',su100='{}' where namst='{}'".format(n5[13],n5[14],n5[15],str(rt5),nr))
						db1.commit()
					ll+=1
			db1=sqlite3.connect(yearnow+'.db')
			db1.row_factory=sqlite3.Row
			q1=db1.execute("select * from termtwoqran where namst='{}'".format(nr))
			q2=db1.execute("select * from termtwoaslm where namst='{}'".format(nr))
			q3=db1.execute("select * from termtwoarbic where namst='{}'".format(nr))
			q4=db1.execute("select * from termtworeadeat where namst='{}'".format(nr))
			q5=db1.execute("select * from termtwoalom where namst='{}'".format(nr))
			if int(namrowstu[-2])>=3:
				q6=db1.execute("select * from termtwoajtm where namst='{}'".format(nr))
			else:q6=''
			if int(namrowstu[-2])>=7:
				
				q7=db1.execute("select * from termtwoenglish where namst='{}'".format(nr))
			else:q7=''
			return render(request,'sch/shomarks.html',{'oo1':q1,"c":"10",'oo2':q2,'oo3':q3,'oo4':q4,'oo5':q5,'oo6':q6,'oo7':q7,'rn':nr,'nst':namrowstu,'yearnow':yearnow,'termnow':terms.objects.get(pk=1),'nameschool':nameschool.objects.get(pk=1)})
