# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class IndexName(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    stars = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'index_name'


class IndexType(models.Model):
    typename = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'index_type'


class T1(models.Model):
    id = models.BigAutoField(primary_key=True)
    n_star = models.IntegerField()
    short = models.CharField(max_length=400)
    sentiment = models.FloatField()

    class Meta:
        managed = False
        db_table = 't1'


class T2(models.Model):
    id = models.BigAutoField(primary_key=True)
    n_star = models.IntegerField()
    short = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 't2'


class Tb1(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb1'


class ZdmBand(models.Model):
    id = models.CharField(primary_key=True, max_length=128)
    band = models.CharField(max_length=255, blank=True, null=True)
    bandenglish = models.CharField(max_length=255, blank=True, null=True)
    bandchinese = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zdm_band'


class ZdmComment(models.Model):
    pid = models.CharField(max_length=128, blank=True, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    datepublished = models.DateTimeField(db_column='datePublished', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zdm_comment'


class ZdmCommentClean(models.Model):
    pid = models.TextField(blank=True, null=True)
    publisher = models.TextField(blank=True, null=True)
    datepublished = models.DateTimeField(db_column='datePublished', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zdm_comment_clean'


class ZdmProCom(models.Model):
    index = models.BigIntegerField(primary_key=True)
    id = models.TextField(blank=True, null=True)
    datepublished = models.DateTimeField(db_column='datePublished', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    bandname = models.TextField(blank=True, null=True)
    platform = models.TextField(blank=True, null=True)
    publisher = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zdm_pro_com'


class ZdmProduct(models.Model):
    id = models.CharField(primary_key=True, max_length=128)
    title = models.TextField(blank=True, null=True)
    link = models.CharField(max_length=1000, blank=True, null=True)
    zhi = models.IntegerField(blank=True, null=True)
    buzhi = models.IntegerField(blank=True, null=True)
    collectcount = models.IntegerField(blank=True, null=True)
    commentcount = models.IntegerField(blank=True, null=True)
    platform = models.CharField(max_length=200, blank=True, null=True)
    publishtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zdm_product'
