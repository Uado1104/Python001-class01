import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import ZdmProCom
from django.db.models import Avg


def index(request):
    start_date = request.GET.get('start_date')
    if start_date is None:
        # start_date = '2020/01/01'
        start_date = (datetime.datetime.now() + datetime.timedelta(days=-90)).strftime("%Y/%m/%d")
    end_date = request.GET.get('end_date')
    if end_date is None:
        # end_date = '2020/10/01'
        end_date = datetime.datetime.now().strftime("%Y/%m/%d")
    band_name = request.GET.get('band_name')
    if band_name is None:
        band_name = ''
    keyword = request.GET.get('keyword')
    if keyword is None:
        keyword = ''

    conditions = {}
    if band_name is not None and len(band_name.strip()) > 0:
        conditions['bandname__icontains'] = band_name.strip()
    if keyword is not None and len(keyword.strip()) > 0:
        conditions['comment__icontains'] = keyword.strip()
    if start_date is not None and len(start_date.strip()) > 0:
        conditions['datepublished__gte'] = datetime.datetime.strptime(start_date, "%Y/%m/%d")
    if end_date is not None and len(end_date.strip()) > 0:
        conditions['datepublished__lte'] = datetime.datetime.strptime(end_date, "%Y/%m/%d")
    # return HttpResponse(f"开始时间：{start_date};结束时间：{end_date};品牌名称：{band_name};评论关键字：{keyword};查询条件：{conditions};{len(conditions)}")

    comments = object
    if len(conditions) > 0:
        comments = ZdmProCom.objects.filter(**conditions).all().order_by('datepublished')
    else:
        comments = ZdmProCom.objects.all().order_by('datepublished')
    # 评论数量
    counter = comments.count()

    # 情感倾向
    sent_avg = f" {comments.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "

    # 正向数量
    queryset = comments.values('sentiment')
    condtions = {'sentiment__gte': 0.5}
    plus = queryset.filter(**condtions).count()

    # 负向数量
    queryset = comments.values('sentiment')
    condtions = {'sentiment__lt': 0.5}
    minus = queryset.filter(**condtions).count()

    return render(request, 'result.html', locals())