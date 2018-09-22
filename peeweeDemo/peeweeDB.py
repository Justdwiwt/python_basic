# ！ /usr/bin/python3
# -*-coding:UTF-8-*-

from peewee import *

db = SqliteDatabase("sampleDB.db")


class BaseModel(Model):
    class Meta:
        database = db


class Course(BaseModel):
    id = PrimaryKeyField()
    title = CharField(null='false')
    period = IntegerField()
    description = CharField()

    class Meta:
        order_by = ('title',)
        db_table = 'course'


class Teacher(BaseModel):
    id = PrimaryKeyField()
    name = CharField(null='false')
    gender = BooleanField()
    address = CharField()
    course_id = ForeignKeyField(Course, to_field="id", related_name="course")

    class Meta:
        order_by = ('name',)
        db_table = 'teacher'


Course.create_table()
Teacher.create_table()

Course.create(id=1, title='经济学', period=320, descrtption='文理兼修')
Course.create(id=2, title='大学英语', period=320, descrtption='文理兼修')
Course.create(id=3, title='高等数学', period=320, descrtption='文理兼修')

Teacher.create(name='111', gender=True, address='...', course_id=1)
Teacher.create(name='222', gender=False, address='...', course_id=2)
Teacher.create(name='333', gender=True, address='...', course_id=3)

record = Course.get(Course, title='大学英语')
print('课程：%s,学时:%d' % (record.title, record.period))

record.period = 200
record.save()

record.delete_instance()

courses = Course.select()

coursesDesc = Course.select().where(Course.id < 20).order_by(Course.period.desc())

total = Course.select(fn.Avg(Course.period).alias('avg_period'))

Course.update(period=300).where(Course.id > 100).excute()

Record = Course.select().join(Teacher).where(Teacher.gender == True)
