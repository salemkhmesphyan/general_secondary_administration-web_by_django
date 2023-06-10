from django.db import models

# Create your models here.
x=[('row2','row2'),('row3','row3')]
y=[('qran','qran'),('aslm','aslm'),('arbic','arbic'),('readeat','readeat'),('alom','alom'),('ajtm','ajtm'),('english','english')]
z=[('T','T'),('A','A')]
t=[('الفصل الاول','الفصل الاول'),('الفصل الثاني','الفصل الثاني')]

class Tmt(models.Model):
	namerow=models.CharField(max_length=50)
	def __str__(self):
		return self.namerow
	class Meta:
		verbose_name="الصفوف المضافة"
class Tmt2(models.Model):
	nameuser=models.CharField(max_length=50)
	namemtral=models.CharField(max_length=50,choices=y)
	namerow1=models.ForeignKey(Tmt,on_delete=models.CASCADE,null=True)
	typeperson=models.CharField(max_length=50,choices=z)
	def __str__(self):
		return self.nameuser
	class Meta:
		verbose_name="جدول المعلمين"	
class terms(models.Model):
	term=models.CharField(max_length=50,choices=t)
	def __str__(self):
		return self.term
	class Meta:
		verbose_name="الفصل الحالي"
class years(models.Model):
	year1=models.CharField(max_length=50,verbose_name='السنين')
	def __str__(self):
		return self.year1
	class Meta:
		verbose_name="الاعوام الدراسية"
class year(models.Model):
	yearr=models.ForeignKey(years,on_delete=models.CASCADE,null=True)
	def __str__(self):
		return str(self.yearr)
	class Meta:
		verbose_name="العام الدراسي الحالي"
class nameschool(models.Model):
	name=models.CharField(max_length=50,verbose_name='اسم المدرسة')
	def __str__(self):
		return self.name
	class Meta:
		verbose_name="اسم المدرسة"	
